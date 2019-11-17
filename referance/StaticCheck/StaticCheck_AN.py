
"""
 * @author nhphung
 * modified by Nguyen Hoang Nam
"""

from AST import *
from StaticError import *
from Utils import Utils
from Visitor import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
                   Symbol("getint",     MType([],IntType())),
                   Symbol("putint",     MType([IntType()],VoidType())),
                   Symbol("putintln",   MType([IntType()],VoidType())),
                   Symbol("getfloat",   MType([],FloatType())),
                   Symbol("putfloat",   MType([FloatType()],VoidType())),
                   Symbol("putfloatln", MType([FloatType()],VoidType())),
                   Symbol("putbool",    MType([BoolType()],VoidType())),
                   Symbol("putboolln",  MType([BoolType()],VoidType())),
                   Symbol("putstring",  MType([StringType()],VoidType())),
                   Symbol("putstringln",MType([StringType()],VoidType())),
                   Symbol("putln",      MType([],VoidType()))
                   ]
    __currentInLoop = 0
    __funcType = None
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        self.visit(self.ast, [StaticChecker.global_envi[:]])
        return []

    def visitProgram(self, ast, c):
        for i in ast.decl:
            if type(i) is VarDecl:
                c[0] += [self.visit(i,c[:])]
            else:
                if self.lookup(i.name.name.lower(), c[0], lambda q: q.name):
                    if type(i.returnType) is VoidType:
                        raise Redeclared(Procedure(),i.name.name)
                    else: raise Redeclared(Function(),i.name.name)
                c[0] += [Symbol(i.name.name.lower(),MType([j.varType for j in i.param],i.returnType))]
        foundMain = False
        for i in c[0]:
            if i.name.lower() == "main":
                if not (type(i.mtype) is MType):
                    raise NoEntryPoint()
                elif i.mtype.partype == [] and type(i.mtype.rettype) is VoidType:
                    pass
                else:
                    raise NoEntryPoint()
                foundMain = True
        if not foundMain: raise NoEntryPoint()
        for i in ast.decl:
            if type(i) is FuncDecl:
                self.visit(i,c[:])

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name.lower(), c[0], lambda q: q.name):
            raise Redeclared(Variable(), ast.variable.name)
        return Symbol(ast.variable.name.lower(),ast.varType)

    def visitFuncDecl(self, ast, c):
        c = [[]] + c
        for i in ast.param:
            try: c[0] += [self.visit(i, c[:])]
            except Redeclared as e: raise Redeclared(Parameter(),e.n)
        for i in ast.local: c[0] += [self.visit(i, c[:])]
        self.__funcType = ast.returnType
        checkBody = False
        for i in ast.body:
            checkBody = checkBody or self.visit(i,c[:])
        if not(type(self.__funcType) is VoidType):
            if not checkBody:
                raise FunctionNotReturn(ast.name.name)
            pass
        self.__funcType = None
        return None

    def visitAssign(self, ast, c):
        lhs = self.visit(ast.lhs,c[:])
        rhs = self.visit(ast.exp,c[:])
        if type(lhs) != type(rhs):
            if type(lhs) is FloatType and type(rhs) is IntType:
                pass
            else:
                raise TypeMismatchInStatement(ast)
        if type(lhs) is StringType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        return False

    def visitIf(self, ast, c):
        expr = self.visit(ast.expr,c[:])
        if not (type(expr) is BoolType):
            raise TypeMismatchInStatement(ast)
        checkThen = False
        checkElse = False
        for i in ast.thenStmt: checkThen = self.visit(i,c[:]) or checkThen
        for i in ast.elseStmt: checkElse = self.visit(i,c[:]) or checkElse
        return checkElse and checkThen

    def visitWhile(self, ast, c):
        self.__currentInLoop += 1
        exp = self.visit(ast.exp,c[:])
        if not (type(exp) is BoolType):
            raise TypeMismatchInStatement(ast)
        for i in ast.sl: self.visit(i,c[:])
        self.__currentInLoop -= 1
        return False

    def visitFor(self, ast, c):
        self.__currentInLoop += 1
        for i in c:
            id = self.lookup(ast.id.name.lower(), i, lambda x: x.name)
            if id: break
        if id is None: raise Undeclared(Identifier(),ast.id.name)
        expr1 = self.visit(ast.expr1,c[:])
        expr2 = self.visit(ast.expr2,c[:])
        if not (type(id.mtype) is IntType and type(expr1) is IntType and type(expr2) is IntType):
            raise TypeMismatchInStatement(ast)
        for i in ast.loop: self.visit(i,c[:])
        self.__currentInLoop -= 1
        return False

    def visitBreak(self,ast,c):
        if self.__currentInLoop == 0:
            raise BreakNotInLoop()
        return False

    def visitContinue(self, ast, c):
        if self.__currentInLoop == 0:
            raise ContinueNotInLoop()
        return False

    def visitReturn(self, ast, c):
        if ast.expr is None:
            if not(type(self.__funcType) is VoidType):
                raise TypeMismatchInStatement(ast)
        else:
            if type(self.__funcType) is VoidType: raise TypeMismatchInStatement(ast)
            if type(self.__funcType) is ArrayType:
                if type(ast.expr) is Id:
                    for i in c:
                        res = self.lookup(ast.expr.name.lower(),i,lambda x: x.name)
                        if res:
                            a = res.mtype
                            b = self.__funcType
                            if type(a) is ArrayType and a.lower == b.lower and a.upper == b.upper and type(a.eleType) == type(b.eleType):
                                break
                            else:
                                raise TypeMismatchInStatement(ast)
                else:
                    raise TypeMismatchInStatement(ast)
            returnExprType = type(self.visit(ast.expr,c[:]))
            if returnExprType == type(self.__funcType):
                pass
            elif returnExprType is IntType and type(self.__funcType) is FloatType:
                pass
            else:
                raise TypeMismatchInStatement(ast)
        return True

    def visitWith(self, ast, c):
        c = [[]] + c
        for i in ast.decl: c[0] += [self.visit(i, c[:])]
        checkStmt = False
        for i in ast.stmt: checkStmt = checkStmt or self.visit(i,c[:])
        return checkStmt

    def visitCallStmt(self, ast, c):
        callParam=[]
        for i in ast.param:
            callParam+=[self.visit(i,c[:])]
        for i in c:
            res = self.lookup(ast.method.name.lower(),i,lambda x: x.name)
            if res:
                if type(res.mtype) is MType:
                    if len(callParam) != len(res.mtype.partype):
                        raise TypeMismatchInStatement(ast)
                    Pair = list(zip(callParam, res.mtype.partype))
                    for pair in Pair:
                        if type(pair[0]) != type(pair[1]):
                            if type(pair[0]) is IntType and type(pair[1]) is FloatType:
                                pass
                            else:
                                raise TypeMismatchInStatement(ast)
                        else:
                            if type(pair[0]) is ArrayType:
                                if pair[0].lower == pair[1].lower and pair[0].upper == pair[1].upper and type(pair[0].eleType) == type(pair[1].eleType):
                                    pass
                                else:
                                    raise TypeMismatchInStatement(ast)
                    return False
                else:
                    raise TypeMismatchInStatement(ast)
        raise Undeclared(Procedure(),ast.method.name)

    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)
        if type(left) != type(right):
            if   type(left) is IntType and type(right) is FloatType: left, right = right, left
            elif type(left) is FloatType and type(right) is IntType: pass
            else: raise TypeMismatchInExpression(ast)

        if type(left) is BoolType:
            if ast.op.lower() in ['and','andthen','or','orelse']:
                return BoolType()
            raise TypeMismatchInExpression(ast)

        if type(left) is IntType:
            if ast.op == '/':
                return FloatType()
            if ast.op in ['<','<=','>','>=','<>','=']:
                return BoolType()
            if ast.op in ['+','-','*']:
                return IntType()
            if ast.op.lower() in ['div','mod']:
                return IntType()
            raise TypeMismatchInExpression(ast)

        if type(left) is FloatType:
            if ast.op in ['+','-','*','/']:
                return FloatType()
            if ast.op in ['<','<=','>','>=','<>','=']:
                return BoolType()
            raise TypeMismatchInExpression(ast)

        if type(left) is StringType:
            raise TypeMismatchInExpression(ast)

        print("WTF BinaryOp this is?",left,ast.op,right)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        body = self.visit(ast.body,c[:])
        if ast.op == '-':
            if type(body) is IntType:
                return IntType()
            if type(body) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        if ast.op.lower() == 'not':
            if type(body) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)

        print("What UnaryOp is this?",ast.op,body)
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        callParam=[]
        for i in ast.param:
            callParam+=[self.visit(i,c[:])]
        for i in c:
            res = self.lookup(ast.method.name.lower(),i,lambda x: x.name)
            if res:
                if type(res.mtype) is MType:
                    if len(callParam) != len(res.mtype.partype):
                        raise TypeMismatchInExpression(ast)
                    Pair = list(zip(callParam, res.mtype.partype))
                    for pair in Pair:
                        if type(pair[0]) != type(pair[1]):
                            if type(pair[0]) is IntType and type(pair[1]) is FloatType:
                                pass
                            else:
                                raise TypeMismatchInExpression(ast)
                        else:
                            if type(pair[0]) is ArrayType:
                                if pair[0].lower == pair[1].lower and pair[0].upper == pair[1].upper and type(pair[0].eleType) == type(pair[1].eleType):
                                    pass
                                else:
                                    raise TypeMismatchInExpression(ast)
                    return res.mtype.rettype
                else:
                    raise TypeMismatchInExpression(ast)
        raise Undeclared(Function(),ast.method.name)

    def visitId(self, ast, c):
        for i in c:
            res = self.lookup(ast.name.lower(),i,lambda x: x.name)
            if res:
                if type(res.mtype) is MType: return res.mtype.rettype
                else: return res.mtype
        raise Undeclared(Identifier(),ast.name)

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr,c[:])
        idx = self.visit(ast.idx,c[:])
        if type(ast.arr) is Id: pass
        elif type(ast.arr) is CallExpr: pass
        else: raise TypeMismatchInExpression(ast)

        if not (type(arr) is ArrayType): raise TypeMismatchInExpression(ast)
        if not(type(idx) is IntType):   raise TypeMismatchInExpression(ast)
        return arr.eleType

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self,ast, c):
        return FloatType()

    def visitStringLiteral(self,ast, c):
        return StringType()

    def visitBooleanLiteral(self,ast, c):
        return BoolType()