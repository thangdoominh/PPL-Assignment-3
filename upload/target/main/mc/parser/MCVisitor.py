# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardeclaration.
    def visitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#singletype.
    def visitSingletype(self, ctx:MCParser.SingletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idlist.
    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idtail.
    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idarray.
    def visitIdarray(self, ctx:MCParser.IdarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idsingle.
    def visitIdsingle(self, ctx:MCParser.IdsingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdeclaration.
    def visitFuncdeclaration(self, ctx:MCParser.FuncdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paralist_decla.
    def visitParalist_decla(self, ctx:MCParser.Paralist_declaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paradecla.
    def visitParadecla(self, ctx:MCParser.ParadeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block.
    def visitBlock(self, ctx:MCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statement.
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ifstmt.
    def visitIfstmt(self, ctx:MCParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#forstmt.
    def visitForstmt(self, ctx:MCParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#breakstmt.
    def visitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continuestmt.
    def visitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#returnstmt.
    def visitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expressionstmt.
    def visitExpressionstmt(self, ctx:MCParser.ExpressionstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp1.
    def visitExp1(self, ctx:MCParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp2.
    def visitExp2(self, ctx:MCParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp3.
    def visitExp3(self, ctx:MCParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp4.
    def visitExp4(self, ctx:MCParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp5.
    def visitExp5(self, ctx:MCParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp6.
    def visitExp6(self, ctx:MCParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp7.
    def visitExp7(self, ctx:MCParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp8.
    def visitExp8(self, ctx:MCParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp9.
    def visitExp9(self, ctx:MCParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#exp10.
    def visitExp10(self, ctx:MCParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operand.
    def visitOperand(self, ctx:MCParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funccall.
    def visitFunccall(self, ctx:MCParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paralist_call.
    def visitParalist_call(self, ctx:MCParser.Paralist_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_call.
    def visitPara_call(self, ctx:MCParser.Para_callContext):
        return self.visitChildren(ctx)



del MCParser