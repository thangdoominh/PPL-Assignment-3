
"""
 * Do Minh Thang
 * 1713217
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

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
        for x in ast.decl:
            if type(x) is VarDecl:
                self.visit(x, (g, Variable()))
            else:
                self.visit(x, (g, Function()))

        mainFunc = self.findSymbol('main', g)
        if mainFunc is None:
            raise NoEntryPoint();

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

    def visitFuncDecl(self, ast, params):
        localEnvironment = []
        check = self.findSymbol(ast.name.name, params[0])
        param = [self.visit(x, (localEnvironment, Parameter())) for x in ast.param]
        if check is None:
            res = Symbol(ast.name.name, MType(param, ast.returnType))
            params[0].append(res)

            return res
        else:
            raise Redeclared(Function(), ast.name.name)

    def visitArrayPointerType(self, ast, params):
        pass

    def visitBinaryOp(self, ast, params):
        pass

    def visitUnaryOp(self, ast, params):
        pass

    def visitCallExpr(self, ast, params):
        pass

    def visitId(self, ast, params):
        pass

    def visitArrayCell(self, ast, params):
        pass

    def visitBlock(self, ast, params):
        pass

    def visitIf(self, ast, params):
        pass

    def visitFor(self, ast, params):
        pass

    def visitContinue(self, ast, params):
        pass

    def visitBreak(self, ast, params):
        pass

    def visitReturn(self, ast, params):
        pass

    def visitDowhile(self, ast, params):
        pass

    def visitIntLiteral(self, ast, params):
        pass

    def visitFloatLiteral(self, ast, params):
        pass

    def visitBooleanLiteral(self, ast, params):
        pass

    def visitStringLiteral(self, ast, params):
        pass
















