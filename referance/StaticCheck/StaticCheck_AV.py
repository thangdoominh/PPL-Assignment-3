
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
	def __init__(self,partype,rettype):
		self.partype = partype
		self.rettype = rettype

	def __str__(self):
		return 'MType[' + ','.join(str(i) for i in self.partype) + '],' + str(self.rettype)

class Symbol:
	def __init__(self,name,mtype,value = None):
		self.name = name
		self.mtype = mtype
		self.value = value

	def __str__(self):
		return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):
	global_envi = [Symbol("getInt",MType([],IntType())),
				   Symbol("putInt",MType([IntType()],VoidType())),
				   Symbol("putIntLn",MType([IntType()],VoidType())),
				   Symbol("getFloat",MType([],FloatType())),
				   Symbol("putFloat",MType([FloatType()],VoidType())),
				   Symbol("putFloatLn",MType([FloatType()],VoidType())),
				   Symbol("putBool",MType([BoolType()],VoidType())),
				   Symbol("putBoolLn",MType([BoolType()],VoidType())),
				   Symbol("putString",MType([StringType()],VoidType())),
				   Symbol("putStringLn",MType([StringType()],VoidType())),
				   Symbol("putLn",MType([],VoidType()))]

	unreached = []

	def __init__(self,ast):
		self.ast = ast

	def check(self):
		return self.visit(self.ast,StaticChecker.global_envi)

	# True if y can parse to x in CallStmt, CallExpr, Return of FuncDecl
	def typeCheck(self,x,y):
		if type(x) == type(y):
			if type(x) is ArrayType and not (x.lower == y.lower and x.upper == y.upper and type(x.eleType) == type(y.eleType)):
				return False
			else:
				return True
		else:
			if type(x) is FloatType and type(y) is IntType:
				return True
			else:
				return False

	# return Symbol of the specified name in the environment if it is exists, default by None
	def findSymbol(self,name,env):
		r = None
		if type(env) is tuple:
			for e in env[::-1]:
				if r is None:
					r = self.lookup(name.lower(),e,lambda x: x.name.lower())
		else:
			r = self.lookup(name.lower(),env,lambda x: x.name.lower())
		return r

	# c[0] is the environment or tuple of environments
	# c[1] is kind of the visit
	def visitProgram(self,ast,c):
		g = c[:]
		StaticChecker.unreached = []
		for x in ast.decl:
			self.visit(x,(g,Variable()))
		m = self.findSymbol('main',g)
		if m is None or not (type(m.mtype) is MType and len(m.mtype.partype) == 0 and type(m.mtype.rettype) is VoidType):
			raise NoEntryPoint()
		for x in ast.decl:
			if type(x) is FuncDecl:
				self.visit(x,(g,'FuncDecl'))
		# if len(StaticChecker.unreached) > 0:
			# k = (Procedure() if type(StaticChecker.unreached[0].mtype.rettype) is VoidType else Function())
			# raise Unreachable(k,StaticChecker.unreached[0].name)
		return ['Correct']#no error

	# params[0] is the environment. params[1] can be anything, in this case Variable or Parameter
	def visitVarDecl(self,ast,params):
		res = Symbol(ast.variable.name,ast.varType)
		check = self.findSymbol(ast.variable.name,params[0])
		if check is None:
			params[0].append(res)
			return res
		else:
			raise Redeclared(params[1],res.name)

	def visitFuncDecl(self,ast,params):
		local_env = []
		check = self.findSymbol(ast.name.name,params[0])
		param = [self.visit(x,(local_env,Parameter())).mtype for x in ast.param]
		if check is None:
			res = Symbol(ast.name.name,MType(param,ast.returnType))
			params[0].append(res)
			if res.name != 'main': StaticChecker.unreached.append(res)
			return res
		elif params[1] == 'FuncDecl':
			for x in ast.local:
				self.visit(x,(local_env,Variable()))
			if self.visitandGetReturned(ast.body,((params[0],local_env),ast.returnType,None)) is None:
				raise FunctionNotReturn(ast.name.name)
			return None
		elif type(ast.returnType) is VoidType:
			raise Redeclared(Procedure(),ast.name.name)
		else:
			raise Redeclared(Function(),ast.name.name)

	# Return the returnType if there is returnType returned somewhere in stmtlist
	def visitandGetReturned(self,stmtlist,params):
		rcheck = []
		for x in stmtlist:
			r = self.visit(x,params)
			if not r is None: rcheck.append('Returned')
			else: rcheck.append(r)
		if type(params[1]) is VoidType: return params[1]
		return None if not 'Returned' in rcheck else params[1]

	# If a statement contains Return Statement in all its flow, it must return the returnType, otherwise None
	# Since there params[1] is the returnType of the current function/procedure
	# params[2] can be missing or None, or set to 'loop' when visit statements inside a loop
	
	######################################
	# Statements that can contain others #
	######################################

	def visitIf(self,ast,params):
		if not type(self.visit(ast.expr,params[0])) is BoolType:
			raise TypeMismatchInStatement(ast)
		checkThen = self.visitandGetReturned(ast.thenStmt,params)
		checkElse = self.visitandGetReturned(ast.elseStmt,params)
		return params[1] if not (checkThen is None or checkElse is None) else None

	def visitFor(self,ast,params):
		i = self.findSymbol(ast.id.name,params[0])
		if i is None:
			raise Undeclared(Identifier(),ast.id.name)
		if not type(self.visit(ast.id,params[0])) is IntType\
		or not type(self.visit(ast.expr1,params[0])) is IntType\
		or not type(self.visit(ast.expr2,params[0])) is IntType:
			raise TypeMismatchInStatement(ast)
		for x in ast.loop:
			self.visit(x,(params[0],params[1],'loop'))
		return None

	def visitWhile(self,ast,params):
		if not type(self.visit(ast.exp,params[0])) is BoolType:
			raise TypeMismatchInStatement(ast)
		for x in ast.sl:
			self.visit(x,(params[0],params[1],'loop'))
		return None

	#####################
	# Single statements #
	#####################

	def visitAssign(self,ast,params):
		ltype = type(self.visit(ast.lhs,params[0]))
		if ltype is StringType or ltype is ArrayType:
			raise TypeMismatchInStatement(ast)
		rtype = type(self.visit(ast.exp,params[0]))
		if ltype is rtype or (ltype is FloatType and rtype is IntType):
			return None
		else:
			raise TypeMismatchInStatement(ast)

	def visitCallStmt(self,ast,params):
		check = self.visitCall(ast,params[0],Procedure())
		if check is None: raise TypeMismatchInStatement(ast)
		return None

	def visitBreak(self,ast,params):
		if len(params) < 3 or params[2] != 'loop': raise BreakNotInLoop()
		return None

	def visitContinue(self,ast,params):
		if len(params) < 3 or params[2] != 'loop': raise ContinueNotInLoop()
		return None

	def visitReturn(self,ast,params):
		if ast.expr is None:
			if not type(params[1]) is VoidType:
				raise TypeMismatchInStatement(ast)
			return None
		else:
			r = self.visit(ast.expr,params[0])
			if self.typeCheck(params[1],r) == False:
				raise TypeMismatchInStatement(ast)
			return r

	#################################################
	# Expressions only use params[0] as environment #
	#################################################

	def visitId(self,ast,env):
		r = self.findSymbol(ast.name,env)
		if r is None or type(r.mtype) is MType: raise Undeclared(Identifier(),ast.name)
		else: return r.mtype

	def visitArrayCell(self,ast,env):
		index = self.visit(ast.idx,env)
		if not type(index) is IntType:
			raise TypeMismatchInExpression(ast)
		array = self.visit(ast.arr,env)
		if type(array) is ArrayType:
			return array.eleType
		else:
			raise TypeMismatchInExpression(ast)

	def visitBinaryOp(self,ast,env):
		ltype = type(self.visit(ast.left,env))
		rtype = type(self.visit(ast.right,env))
		
		if ltype in (IntType,FloatType) and rtype in (IntType,FloatType):
			if ast.op == '/':
				return FloatType()
			if ast.op in ('+','-','*'):
				return FloatType() if FloatType in (ltype,rtype) else IntType()
			if ast.op in ('<','>','<=','>=','=','<>'):
				return BoolType()
		
		if ast.op.lower() in ('and','andthen','or','orelse')\
		and ltype is BoolType and rtype is BoolType:
			return BoolType()
		
		if ast.op.lower() in ('div','mod')\
		and ltype is IntType and rtype is IntType:
			return IntType()
		
		raise TypeMismatchInExpression(ast)

	def visitUnaryOp(self,ast,env):
		check = self.visit(ast.body,env)
		if ast.op.lower() == 'not' and type(check) is BoolType\
		or ast.op == '-' and type(check) in (IntType,FloatType):
			return check
		raise TypeMismatchInExpression(ast)

	def visitIntLiteral(self,ast,env):
		return IntType()

	def visitFloatLiteral(self,ast,env):
		return FloatType()

	def visitBooleanLiteral(self,ast,env):
		return BoolType()

	def visitStringLiteral(self,ast,env):
		return StringType()

	def visitCallExpr(self,ast,env):
		check = self.visitCall(ast,env,Function())
		if check is None: raise TypeMismatchInExpression(ast)
		return check

	# core function for CallExpr and CallStmt
	def visitCall(self,ast,env,kind):
		method = self.findSymbol(ast.method.name,env)
		if method is None or type(method.mtype) != MType\
		or (type(method.mtype.rettype) is VoidType and type(kind) is Function)\
		or (type(method.mtype.rettype) != VoidType and type(kind) is Procedure):
			raise Undeclared(kind,ast.method.name)
		if method in StaticChecker.unreached:
			StaticChecker.unreached.remove(method)
		def_param = method.mtype.partype
		use_param = [self.visit(x,env) for x in ast.param]
		if len(def_param) != len(use_param):
			return None
		for i in range(0,len(def_param)):
			if self.typeCheck(def_param[i],use_param[i]) == False:
				return None
		return method.mtype.rettype

	# def visitIntType(self,ast,env):
		# return None

	# def visitFloatType(self,ast,env):
		# return None

	# def visitBoolType(self,ast,env):
		# return None

	# def visitStringType(self,ast,env):
		# return None

	# def visitVoidType(self,ast,env):
		# return None

	# def visitArrayType(self,ast,env):
		# return None