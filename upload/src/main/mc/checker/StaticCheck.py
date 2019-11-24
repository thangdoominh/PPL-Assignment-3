
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
        Symbol("getInt", MType([], IntType()), 0),
        Symbol("putInt", MType([IntType()], VoidType()),0),
        Symbol("putIntLn", MType([IntType()], VoidType()), 0),
        Symbol("getFloat", MType([], FloatType()), 0),
        Symbol("putFloat", MType([FloatType()], VoidType()), 0),
        Symbol("putFloatLn",MType([FloatType()], VoidType()), 0),
        Symbol("putBool", MType([BoolType()], VoidType()), 0),
        Symbol("putBoolLn", MType([BoolType()], VoidType()), 0),
        Symbol("putString", MType([StringType()], VoidType()), 0)
    ]

    # list of name function unreachable
    unreached = []
    __currentFunction = None
    __funcType = None
    __curTypeFunc = None
    __currentInLoop = 0
    def __init__(self,ast):
        self.ast = ast

    #default return None.
    #If it has exists, return Symbol of the sepecified name in the environment.
    # name: String
    # env: List or tuple of Symbol
    def findSymbol(self, name, env):
        result = None
        if type(env) is tuple or list:
            for i in env:
                if result is None:
                    result = self.lookup(name, i, lambda x: x.name)
        else:
            result = self.lookup(name, env, lambda x: x.name)
        return result

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi[:])

    def typeCheck(self, x, y):
        if type(x) == type(y):
            if type(x) is ArrayType and x.eleType != y.eleType:
                return False
            else:
                return True
        else:
            if type(x) is FloatType and type(y) is IntType:
                return True
            else:
                return False

    # c[0] is the environment or tuple of environment
    # c[1] is kind of the visit
    def visitProgram(self, ast, c):
        # g = c[:]
        g = [c]

        # This loop will visit all of variable global and function and save it into g
        for x in ast.decl:
            if type(x) is VarDecl:
                g[0] += [self.visit(x, g)]
            else:
                if self.lookup(x.name,g[0], lambda x: x.name):
                    raise Redeclared(Function(), x.name.name)
                g[0] += [Symbol(x.name.name, MType([j.varType for j in x.param], x.returnType))]

        for i in g[0]:
            if type(i.mtype) is MType:
                if i.value is None:
                    if i.name != "main":
                        raise UnreachableFunction(i.name)

        cMain = False
        for i in g[0]:
            if i.name == "main":
                if type(i.mtype) is not MType:
                    raise NoEntryPoint()
                cMain = True
        if not cMain:
            raise NoEntryPoint()
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, g)

        return None

    # param is a list of list
    # param[0] is the environment
    def visitVarDecl(self, ast, params):
        res = Symbol(ast.variable, ast.varType)
        check = self.lookup(ast.variable, params[0], lambda x: x.name)
        if check is None:
            params[0].append(res)
            return res
        else:
            raise Redeclared(Variable(), res.name)

    # param: list of parameter type in current function
    def visitFuncDecl(self, ast, params):

        localEnvironment = [[]] + params
        for i in ast.param:
            if self.lookup(i.variable, localEnvironment[0], lambda x: x.name):
                raise Redeclared(Parameter(), i.variable)
            localEnvironment[0] += [self.visit(i, localEnvironment)]
        self.__funcType = ast.returnType
        self.__currentFunction = ast.name.name
        self.__curTypeFunc = Symbol(ast.name.name, MType([ast.param], ast.returnType),False)
        checkReturn = False
        for i in ast.body.member:
            if type(i) is VarDecl:
                localEnvironment[0] += [self.visit(i, localEnvironment)]
            else:
                checkReturn = (self.visit(i, localEnvironment) or checkReturn)

        if type(ast.returnType) is not VoidType:
            if checkReturn is not True:

                raise FunctionNotReturn(ast.name.name)
        self.__funcType = None
        self.__currentFunction = None

    ######################################
    # Statements that can contain others #
    ######################################

    def visitIf(self, ast, params):
        exprIf = self.visit(ast.expr, params)
        if type(exprIf) is not BoolType:
            raise TypeMismatchInStatement(ast.expr.name)
        checkThen = False
        checkElse = False
        checkThen = self.visit(ast.thenStmt, params) or checkThen
        print("check Then", checkThen)
        if ast.elseStmt is not None:
            checkElse = self.visit(ast.elseStmt, params) or checkElse
            print("check Else", checkElse)
            if checkElse is True and checkThen is True:
                return True
            else:
                return False
        return False

    def visitFor(self, ast, params):
        self.__currentInLoop += 1
        expr1 = self.visit(ast.expr1, params)
        expr2 = self.visit(ast.expr2, params)
        expr3 = self.visit(ast.expr3, params)

        if type(expr1) is IntType and type(expr3) is IntType and type(expr2) is BoolType:
            pass
        else:
            raise TypeMismatchInStatement(ast)
        loop = self.visit(ast.loop, params)
        self.__currentInLoop -= 1
        return False

    def visitDowhile(self, ast, params):
        self.__currentInLoop += 1
        exp = self.visit(ast.exp, params)

        if not type(exp) is BoolType:
            raise TypeMismatchInStatement(ast)
        checkRet = False
        for stmt in ast.sl:
            checkRet = self.visit(stmt, params) or checkRet
        self.__currentInLoop -= 1
        print("checkRet ", checkRet)
        return checkRet


    #####################
    # Single statements #
    #####################

    def visitContinue(self, ast, params):
        if self.__currentInLoop == 0:
            raise ContinueNotInLoop()
        return False

    def visitBreak(self, ast, params):
        if self.__currentInLoop == 0:
            raise BreakNotInLoop()
        return False

    def visitReturn(self, ast, params):

        if ast.expr is None:
            if type(self.__funcType) is not VoidType:
                raise TypeMismatchInStatement(ast)
        else:
            expr = self.visit(ast.expr, params)
            if type(self.__funcType) is VoidType:
                return TypeMismatchInStatement(ast)
            if type(self.__funcType) is ArrayType or type(self.__funcType) is ArrayPointerType:
                if type(ast.expr) is Id:
                    for i in params:
                        res = self.lookup(ast.expr.name, i, lambda  x:x.name)
                        if res:
                            typeRes = res.mtype
                            typeFunc = self.__funcType
                            if (type(expr) is ArrayType or type(expr) is ArrayPointerType) and type(typeRes.eleType) == type(typeFunc.eleType):
                                return True
                            else:
                                raise TypeMismatchInStatement(ast)
                elif type(ast.expr) is CallExpr:
                    for i in params:
                        res = self.lookup(ast.expr.method.name, i, lambda  x:x.name)
                        if res:
                            typeRes = res.mtype
                            typeFunc = self.__funcType
                            if (type(expr) is ArrayType or type(expr) is ArrayPointerType) and type(typeRes.rettype.eleType) is type(typeFunc.eleType):
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            returnExprType = type(self.visit(ast.expr, params[:]))
            if returnExprType == type(self.__funcType):
                pass
            elif returnExprType is IntType and type(self.__funcType) is FloatType:
                pass
            else:
                raise TypeMismatchInStatement(ast)
        return True



    #################################################
    # Expressions only use params[0] as environment #
    #################################################

    def visitCallExpr(self, ast, c):
        paramList = []
        for i in ast.param:
            paramList += [self.visit(i, c)]
        for i in c:
            checkId = self.lookup(ast.method.name, i, lambda x: x.name)
            if checkId:
                if type(checkId.mtype) is MType:
                    if len(paramList) == len(checkId.mtype.partype):
                        for j in range(0,len(paramList)):
                            if type(paramList[j]) is type(checkId.mtype.partype[j]):

                                if type(paramList[j]) is ArrayPointerType:
                                    if type(paramList[j].eleType) == type(checkId.mtype.partype[j].eleType):
                                        pass
                                    else:
                                        raise TypeMismatchInExpression(ast)
                                else:
                                    pass
                            elif type(paramList[j]) is IntType and type(checkId.mtype.partype[j]) is FloatType:
                                pass
                            elif type(paramList[j]) is ArrayType and type(checkId.mtype.partype[j]) is ArrayPointerType and type(paramList[j].eleType) == type(checkId.mtype.partype[j].eleType):
                                pass
                            else:
                                raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)
        if checkId is None:
            raise Undeclared(Function(), ast.method.name)
        # if (self.__curTypeFunc.name != checkId.name):
        #     checkId.value = True
        if (self.__currentFunction != checkId.name):
            checkId.value = 0

        return checkId.mtype.rettype



    def visitBinaryOp(self, ast, enviroment):

        left = self.visit(ast.left, enviroment)
        right = self.visit(ast.right, enviroment)
        if type(ast.left) not in (Id, ArrayCell) and ast.op == "=":
             raise NotLeftValue(ast.left)

        if type(left) != type(right):
            if (ast.op in ["+", "-", "*", "/", ">", "<", ">=", "<="]):
                if type(left) is IntType and type(right) is FloatType:
                    left, right = right, left
                elif type(left) is FloatType and type(right) is IntType:
                    pass
                else:
                    raise TypeMismatchInExpression(ast)
        if type(left) == type(right) or (type(left) is FloatType and type(right) is IntType):
            if type(left) is BoolType:
                if ast.op in ("==", "!=", "&&", "||", "="):
                    return BoolType()
                raise TypeMismatchInExpression(ast)

            if type(left) is IntType:
                if ast.op == "/":
                    return FloatType()
                if ast.op in ("+", "-", "*", "%", "="):
                    if type(right) is FloatType:
                        raise TypeMismatchInExpression(ast)
                    if type(right) is IntType:
                        return IntType()
                if ast.op in ("<", "<=", ">", ">=", "==", "!="):
                    return BoolType()
                raise TypeMismatchInExpression(ast)

            if type(left) is FloatType:
                if ast.op in ("+", "-", "*", "/", "=", "*"):
                    return FloatType()
                if ast.op in ("<", "<=", ">", ">="):
                    return BoolType()
                raise TypeMismatchInExpression(ast)

            if type(left) is StringType:
                if ast.op == "=":
                    return StringType()
                raise TypeMismatchInExpression(ast)
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, enviroment):
        exp = self.visit(ast.body, enviroment)
        if (ast.op == "!" and type(exp) is BoolType)\
            or (ast.op == "-" and type(exp) in (IntType, FloatType)):
            return exp
        raise TypeMismatchInExpression(ast)


    # type ast is symbol
    def visitId(self, ast, enviroment):
        for i in enviroment:
            checkId = self.lookup(ast.name, i,lambda x: x.name )
            if checkId:
                return checkId.mtype
        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast, enviroment):
        array = self.visit(ast.arr, enviroment)
        index = self.visit(ast.idx, enviroment)
        if not type(index) is IntType:
            raise TypeMismatchInExpression(ast)
        if not type(array) is ArrayType and not type(array) is ArrayPointerType:
            raise TypeMismatchInExpression(ast)
        return array.eleType

    def visitBlock(self, ast, enviroment):
        checkRet = False
        enviroment = [[]] + enviroment
        for x in ast.member:
            if type(x) is VarDecl:
                enviroment[0] += [self.visit(x, enviroment)]
            else:
                checkRet = self.visit(x, enviroment) or checkRet
        return checkRet

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
