import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_undeclared_function(self):
        input = """int a; int a;"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_01(self):
        input = """
int a;
int b;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_function_10(self):
        input = """
int a;
int b;
void main(){
    int a;
}
int b()
{}
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_function_11(self):
        input = """
void main(){
    int a;
}
void a()
{}
int a()
{}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_function_12(self):
        input = """
int x,y;
void main(){
    int a;
}
float x()
{
    boolean y;
}
        """
        expect = "Redeclared Function: x"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_function_12(self):
        input = """
void main(){
    int a;
}
float y()
{
    boolean x;
}
boolean y()
{}
        """
        expect = "Redeclared Function: y"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_function_13(self):
        input = """
void main(int a, float b){
    return a;
}
float[] a(int b)
{
    int c;
}
boolean a()
{
    int x;
}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_NoEntryPoint_20(self):
        input = """
int a(int a, int b)
{}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_NoEntryPoint_21(self):
        input = """
float x;
int Main(int a, int b)
{}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_NoEntryPoint_22(self):
        input = """
float x;
int MAIN(int a, int b)
{}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 422))


'''
    def test_diff_numofparam_stmt(self):
        """More complex program"""
        input = """int main () {
            putIntLn();
        }"""
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_diff_numofparam_expr(self):
        """More complex program"""
        input = """int main () {
            putIntLn(getInt(4));
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_undeclared_function_use_ast(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],IntType(),Block([
            CallExpr(Id("foo"),[])]))])
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_diff_numofparam_stmt_use_ast(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],IntType(),Block([
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,405))
'''

