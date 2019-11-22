
"""
 * Do Minh Thang
 * 1713217
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [

    #Built in Function
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn",MType([FloatType()], VoidType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("putString", MType([StringType()], VoidType()))
    ]

    # list of name function unreachable
    unreached = []

    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    #default return None.
    #If it has exists, return Symbol of the sepecified name in the environment.
    # name: String
    # env: List or tuple of Symbol
    def findSymbol(self, name, env):
        result = None
        if type(env) is tuple:
            for i in env:
                if result is None:
                    result = self.lookup(name, i, lambda x: x.name)
        else:
            result = self.lookup(name, env, lambda x: x.name)
        return result

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    # c[0] is the environment or tuple of environment
    # c[1] is kind of the visit
    def visitProgram(self, ast, c):
        g = c[:]

        # This loop will visit all of variable global and function and save it into g
        for x in ast.decl:
            self.visit(x, (g, Variable()))

        mainFunc = self.findSymbol('main', g)
        if mainFunc is None or (type(mainFunc.mtype) != MType):
            raise NoEntryPoint();

        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, (g, 'FuncDecl'))
        #no error (Test print)
        return ['Correct']

    # param[0] is the environment
    # param[1] can be anything,
    # in this case Variable or Parameter
    def visitVarDecl(self, ast, params):
        res = Symbol(ast.variable, ast.varType)
        check = self.findSymbol(ast.variable, params[0])
        if check is None:
            params[0].append(res)
            return res
        else:
            raise Redeclared(params[1], res.name)

    # param: list of parameter type in current function
    def visitFuncDecl(self, ast, params):
        localEnvironment = []
        check = self.findSymbol(ast.name.name, params[0])
        param = [self.visit(x, (localEnvironment, Parameter())).mtype for x in ast.param]

        if check is None:
            res = Symbol(ast.name.name, MType(param, ast.returnType))
            params[0].append(res)
            if res.name != 'main' and type(res.mtype) is MType: StaticChecker.unreached.append(res)
            return res

        elif params[1] is 'FuncDecl':
            checkReturn = self.visitAndGetReturnType(ast.body.member, (localEnvironment, ast.returnType, None))
            # print("Check return ", checkReturn)
            if checkReturn is None:
                raise FunctionNotReturn(ast.name.name)
        else:
            raise Redeclared(Function(), ast.name.name)

    # If a statement contains Return Statement in all its flow, it must return the returnType, otherwise None
    # Since there params[1] is the returnType of the current function.
    # params[2]: can be missing or None, or set to 'loop' when visit statements inside a loop
    def visitAndGetReturnType(self, stmtList, params):
        returnCheck = []

        if type(stmtList) == list:
            for stmt in stmtList:
                temp = self.visit(stmt, params)
                print("params list :   ", params)
                if temp is None or type(temp) is Symbol:
                    returnCheck.append(temp)
                else:
                    returnCheck.append('Returned')
        else:
            temp = self.visit(stmtList, params)
            print("params single :   ", params)
            if temp is None:
                returnCheck.append(temp)
            else:
                returnCheck.append('Returned')
        # print(" returnCheck ------------ ", returnCheck)
        if type(params[1]) is VoidType: return params[1]
        return None if not 'Returned' in returnCheck else params[1]

    ######################################
    # Statements that can contain others #
    ######################################

    def visitIf(self, ast, params):
        exprIf = self.visit(ast.expr, params[0])

        if not type(exprIf) is BoolType:
            raise TypeMismatchInStatement(ast.expr.name)

        checkThen = self.visitAndGetReturnType(ast.thenStmt, params)
        if not ast.elseStmt is None:
            checkElse = self.visitAndGetReturnType(ast.elseStmt, params)
            return params[1] if (checkThen and checkElse) is None else None
        return None if checkThen is None else params[1]

    def visitFor(self, ast, params):
        expr1 = self.visit(ast.expr1, params)
        expr2 = self.visit(ast.expr2, params)
        expr3 = self.visit(ast.expr3, params)

        if type(expr1) is IntType and type(expr3) is IntType and type(expr2) is BoolType:
            return self.visit(ast.loop, (params[0], params[1], 'loop'))
        else:
            raise TypeMismatchInStatement(ast)

    def visitDowhile(self, ast, params):
        exp = self.visit(ast.exp, params[0])

        if not type(exp) is BoolType:
            raise TypeMismatchInStatement(ast)

        for stmt in ast.sl:
            self.visit(stmt, (params[0], params[1], 'loop'))
        return None


    #####################
    # Single statements #
    #####################

    def visitContinue(self, ast, params):
        if len(params) < 3 or params[2] != 'loop': raise ContinueNotInLoop()
        return None

    def visitBreak(self, ast, params):
        print("vao break neeeee")
        if len(params) < 3 or params[2] != 'loop': raise BreakNotInLoop()
        return None

    def visitReturn(self, ast, params):
        pass

    #################################################
    # Expressions only use params[0] as environment #
    #################################################

    def visitCallExpr(self, ast, enviroment):
        pass

    def visitBinaryOp(self, ast, enviroment):
        pass

    def visitUnaryOp(self, ast, enviroment):
        pass


    # type ast is symbol
    def visitId(self, ast, enviroment):
        checkId = self.findSymbol(ast.name, enviroment)
        if checkId is None or (type(checkId.mtype) is MType):
            raise Undeclared(Identifier(), ast.name)
        return checkId.mtype

    def visitArrayCell(self, ast, enviroment):
        pass

    def visitBlock(self, ast, enviroment):
        pass

    ##############
    # visit Type #
    ##############

    def visitArrayPointerType(self, ast, params):
        pass

    def visitIntLiteral(self, ast, params):
        return IntType()

    def visitFloatLiteral(self, ast, params):
        return FloatType()

    def visitBooleanLiteral(self, ast, params):
        return BoolType()

    def visitStringLiteral(self, ast, params):
        return StringType()
