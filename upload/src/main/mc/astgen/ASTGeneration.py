# Name: Ho Minh Hoang
# Student's ID: 1710094
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


class ASTGeneration(MCVisitor):
	def visitProgram(self, ctx: MCParser.ProgramContext):
		decl = [self.visit(i) for i in ctx.manydeclares().declare()]
		result = []
		for i in decl:
			if type(i) is not list:
				result.append(i)
			else:
				for j in i:
					result.append(j)
		return Program(result)

	def visitDeclare(self, ctx: MCParser.DeclareContext):
		return self.visit(ctx.vardec()) if ctx.vardec() \
			else self.visit(ctx.funcdec())

	def visitVardec(self, ctx: MCParser.VardecContext):
		result = []

		for i in ctx.manyvar().var():
			if i.ID():
				result.append(VarDecl(i.ID().getText(), self.visit(ctx.primetype())))
			if i.array():
				result.append(VarDecl(i.array().ID().getText(),
				                      ArrayType(int(i.array().INTLIT().getText()), self.visit(ctx.primetype()))))
		return result

	def visitFuncdec(self, ctx: MCParser.FuncdecContext):
		if ctx.paralist():
			return FuncDecl(Id(ctx.ID().getText()), self.visit(ctx.paralist()), self.visit(ctx.mctype()),
			                self.visit(ctx.stmtblock()))
		return FuncDecl(Id(ctx.ID().getText()), [], self.visit(ctx.mctype()), self.visit(ctx.stmtblock()))

	def visitMctype(self, ctx: MCParser.MctypeContext):
		if ctx.primetype():
			return self.visit(ctx.primetype())
		elif ctx.arraypointer():
			return self.visit(ctx.arraypointer())
		else:
			return VoidType()

	def visitArraypointer(self, ctx: MCParser.ArraypointerContext):
		if ctx.BOOLTYPE():
			return ArrayPointerType(BoolType())
		if ctx.INTTYPE():
			return ArrayPointerType(IntType())
		if ctx.FLOATTYPE():
			return ArrayPointerType(FloatType())
		if ctx.STRTYPE():
			return ArrayPointerType(StringType())

	def visitParalist(self, ctx: MCParser.ParalistContext):
		result = []
		for i in ctx.para():
			if i.getChildCount() == 2:
				result.append(VarDecl(i.ID().getText(), self.visit(i.primetype())))
			else:
				result.append(VarDecl(i.ID().getText(), ArrayPointerType(self.visit(i.primetype()))))
		return result

	def visitMemblock(self, ctx: MCParser.MemblockContext):
		return self.visit(ctx.vardec()) if ctx.vardec() \
			else self.visit(ctx.stmts())

	def visitStmtblock(self, ctx: MCParser.StmtblockContext):
		stmt = [self.visit(i) for i in ctx.memblock()]
		result = []
		for i in stmt:
			if type(i) is not list:
				result.append(i)
			else:
				for j in i:
					result.append(j)
		return Block(result)

	def visitStmts(self, ctx: MCParser.StmtsContext):
		if ctx.do_whilestmt():
			return self.visit(ctx.do_whilestmt())
		if ctx.ifstmt():
			return self.visit(ctx.ifstmt())
		if ctx.forstmt():
			return self.visit(ctx.forstmt())
		if ctx.retstmt():
			return self.visit(ctx.retstmt())
		if ctx.exp():
			return self.visit(ctx.exp())
		if ctx.stmtblock():
			return self.visit(ctx.stmtblock())
		if ctx.breakstmt():
			return self.visit(ctx.breakstmt())
		return self.visit(ctx.continuestmt())

	def visitIfstmt(self, ctx: MCParser.IfstmtContext):
		return If(self.visit(ctx.exp()), self.visit(ctx.stmts(0)), self.visit(ctx.stmts(1))) if ctx.ELSE() \
			else If(self.visit(ctx.exp()), self.visit(ctx.stmts(0)))

	def visitDo_whilestmt(self, ctx: MCParser.Do_whilestmtContext):
		res = [self.visit(i) for i in ctx.stmts()]
		return Dowhile(res, self.visit(ctx.exp()))

	def visitForstmt(self, ctx: MCParser.ForstmtContext):
		return For(self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), self.visit(ctx.stmts()))

	def visitBreakstmt(self, ctx: MCParser.BreakstmtContext):
		return Break()

	def visitContinuestmt(self, ctx: MCParser.ContinuestmtContext):
		return Continue()

	def visitRetstmt(self, ctx: MCParser.RetstmtContext):
		return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

	def visitExp(self, ctx: MCParser.ExpContext):
		if ctx.ASSOP():
			return BinaryOp(ctx.ASSOP().getText(), self.visit(ctx.exp1()), self.visit(ctx.exp()))
		return self.visit(ctx.exp1())

	def visitExp1(self, ctx: MCParser.Exp1Context):
		if ctx.OROP():
			return BinaryOp(ctx.OROP().getText(), self.visit(ctx.exp1()), self.visit(ctx.exp2()))
		return self.visit(ctx.exp2())

	def visitExp2(self, ctx: MCParser.Exp2Context):
		if ctx.ANDOP():
			return BinaryOp(ctx.ANDOP().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
		return self.visit(ctx.exp3())

	def visitExp3(self, ctx: MCParser.Exp3Context):
		if ctx.getChildCount() == 3:
			return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp4(0)), self.visit(ctx.exp4(1)))
		return self.visit(ctx.exp4(0))

	def visitExp4(self, ctx: MCParser.Exp4Context):
		if ctx.getChildCount() == 3:
			return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5(0)), self.visit(ctx.exp5(1)))
		return self.visit(ctx.exp5(0))

	def visitExp5(self, ctx: MCParser.Exp5Context):
		if ctx.getChildCount() == 3:
			return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp5()), self.visit(ctx.exp6()))
		return self.visit(ctx.exp6())

	def visitExp6(self, ctx: MCParser.Exp6Context):
		if ctx.getChildCount() == 3:
			return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.exp6()), self.visit(ctx.exp7()))
		return self.visit(ctx.exp7())

	def visitExp7(self, ctx: MCParser.Exp7Context):
		if (ctx.getChildCount() == 2):
			return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp7()))
		return self.visit(ctx.exp8())

	def visitExp8(self, ctx: MCParser.Exp8Context):
		if (ctx.getChildCount() == 4):
			return ArrayCell(self.visit(ctx.exp8()), self.visit(ctx.exp()))
		return self.visit(ctx.exp9())

	def visitExp9(self, ctx: MCParser.Exp9Context):
		if ctx.exp():
			return self.visit(ctx.exp())
		return self.visit(ctx.operand())

	def visitOperand(self, ctx: MCParser.OperandContext):
		if ctx.INTLIT():
			return IntLiteral(int(ctx.INTLIT().getText()))
		elif ctx.BOOLLIT():
			return BooleanLiteral(True if ctx.BOOLLIT().getText() == "true" else False)
		elif ctx.FLOATLIT():
			return FloatLiteral(float(ctx.FLOATLIT().getText()))
		elif ctx.ID():
			return Id(ctx.ID().getText())
		elif ctx.STRINGLIT():
			return StringLiteral(ctx.STRINGLIT().getText())
		return self.visit(ctx.funcall())

	def visitFuncall(self, ctx: MCParser.FuncallContext):
		return CallExpr(Id(ctx.ID().getText()), [self.visit(i) for i in ctx.exp() if ctx.exp()])

	def visitPrimetype(self, ctx: MCParser.PrimetypeContext):
		if ctx.BOOLTYPE():
			return BoolType()
		if ctx.INTTYPE():
			return IntType()
		if ctx.FLOATTYPE():
			return FloatType()
		return StringType()

