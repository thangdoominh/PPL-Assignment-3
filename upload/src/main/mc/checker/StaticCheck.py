
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
    def __init__(self,name,mtype,value = None):
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
            self.visit(x, (g, Variable()))

        #no error (Test print)
        return ['Correct']

    # param[0] is the environment
    # param[1] can be anything, in this case Variable or Parameter
    def visitVarDecl(self, ast, param):
        res = Symbol(ast.variable, param[0])
        check = self.findSymbol(ast.variable, param[0])
        if check is None:
            param[0].append(res)
        else:
            raise Redeclared(param[1], res.name)















