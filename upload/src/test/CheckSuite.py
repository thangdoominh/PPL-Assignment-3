import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_undeclared_function(self):
        input = """int a; int a;
        void main(){}"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_01(self):
        input = """
int a;
int b;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_parameter_05(self):
        input = """
void main(string a, string a)
{
    string s;
}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_function_not_return_06(self):
        input = """
    void main()
    {}
    int thang()
    {
        int x;
    }
        """
        expect = "Function thang Not Return"
        self.assertTrue(TestChecker.test(input, expect, 406))


    def test_redeclared_function_10(self):
        input = """
int a;
void main(){
    int a;
}
int b()
{}
        """
        expect = "Function b Not Return"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_function_11(self):
        input = """
void main(){
    int a;
}
void a()
{}
int a()
{ return 0;}
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
    return 1.4;
}
        """
        expect = "Redeclared Function: x"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_function_13(self):
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
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_function_14(self):
        input = """
void main(int a, float b){
}
float a(int b)
{
    int c;
}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

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

