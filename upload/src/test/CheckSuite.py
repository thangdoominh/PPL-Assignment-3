import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

    def test_break_not_in_loop_28(self):
        input = """
    int a;
    void main()
    {
        int i;
        int a;
        boolean xyz;
        do
        {
            float temp;
            
        }
        while(xyz);
        
    }
    boolean haiz(int a)
    {
        boolean xyz;
        int i;
        
        for (a; xyz; i)
        {
        
            if(xyz)
            {
                float thang;
            }

        }
        if(xyz)
            {
                boolean abc;
                return abc;
                break;
            }
            else
            {
                boolean qwe;
                return qwe;
                
            }
    }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 428))
'''
    def test_continue_not_in_loop_27(self):
        input = """
    int a;
    void main()
    {
        int i;
        int a;
        boolean xyz;
        do
        {
            float temp;
            
        }
        while(xyz);
        continue;
    }
    boolean haiz(int a)
    {
        boolean xyz;
        int i;
        for (a; xyz; i)
        {
            if(xyz)
            {
                float thang;
            }
        }
        if(xyz)
            {
                boolean abc;
                return abc;
            }
            else
            {
                boolean qwe;
                return qwe;
            }
    }
            """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 427))


    def test_do_while_26(self):
        input = """
    int a;
    void main()
    {
        int i;
        int a;
        boolean xyz;
        do
        {
            float temp;
        }
        while(a);
    }
    boolean haiz(int a)
    {
        boolean xyz;
        int i;
        for (a; xyz; i)
        {
            if(xyz)
            {
                float thang;
            }
        }
        if(xyz)
            {
                boolean abc;
                return abc;
            }
            else
            {
                boolean qwe;
                return qwe;
            }

    }
            """
        expect = "Type Mismatch In Statement: Dowhile([Block([VarDecl(temp,FloatType)])],Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 426))


    def test_Correct_Return_if_25(self):
        input = """
    int a;
    void main()
    {
        int i;
        int a;
        boolean xyz;
        for (xyz; xyz; i)
        {
            if(xyz)
            {
                float thang;
            }
        }
    }
    boolean haiz(int a)
    {
        boolean xyz;
        if(xyz)
            {
                boolean abc;
                return abc;
            }
            else
            {
                boolean qwe;
                return qwe;
            }

    }
            """
        expect = "Type Mismatch In Statement: For(Id(xyz);Id(xyz);Id(i);Block([If(Id(xyz),Block([VarDecl(thang,FloatType)]))]))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_Correct_Return_if_24(self):
        input = """
    int a;
    void main()
    {
        int a;
        boolean xyz;
    }
    boolean haiz(int a)
    {
        boolean xyz;
        if(xyz)
            {
                boolean abc;
                return abc;
            }
            else
            {
                boolean qwe;
                return qwe;
            }
        
    }
            """
        expect = "['Correct']"
        self.assertTrue(TestChecker.test(input, expect, 424))

  
    def test_Not_Return_if_23(self):
        input = """
    int a;
    void main()
    {
        int a;
        boolean xyz;
    }
    boolean haiz(int a)
    {
        boolean xyz;
        if(xyz)
            {
                int thang;
            }
    }
            """
        expect = "Function haiz Not Return "
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_Not_Return_if_18(self):
        input = """
    int a;
    void main()
    {
        int a;
        boolean xyz;
    }
    boolean haiz(int a)
    {
        boolean xyz;
        return xyz;
    }
            """
        expect = "Function haiz Not Return "
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_Not_Return_if_17(self):
        input = """
    int a;
    void main()
    {
        int a;
        boolean xyz;
    }
    boolean haiz(int a)
    {
        boolean xyz;
    }
            """
        expect = "Function haiz Not Return "
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared_variable_03(self):
        input = """
    int a;
    int b;
    void main()
    {
        int b;
    }
    float sub(float x, float y)
    {}
            """
        expect = "Function sub Not Return "
        self.assertTrue(TestChecker.test(input, expect, 403))


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

    def test_redeclared_variable_02(self):
        input = """
int a;
int b;
int sum(int a, int b)
{

}
void main()
{
    int a;
}
        """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 402))


    def test_redeclared_variable_03(self):
        input = """
int a;
int b;
void main()
{
    int b;
}
float sub(float x, float y)
{}
        """
        expect = "Function sub Not Return "
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared_variable_04(self):
        input = """
int main;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))

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
    int a;
    void main()
    {}
    int c()
    {}
        """
        expect = "Function c Not Return "
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_undeclared_id_07(self):
        input = """
            int a;
            void main()
            {
                int a;
            }
            int sum(int a, int b)
            {
                return 3;
            }

                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_if_correct_08(self):
        input = """
            int a;

            void main()
            {
                boolean x;
                if (x)
                {
                    int b;
                }
                    
            }
                """
        expect = "['Correct']"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_undeclared_identifier_09(self):
        input = """
        int a;
        void main()
        {
            if (x)
            {
                int b;
            }
        }
            """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 409))


    def test_redeclared_function_10(self):
        input = """
void main(){
}
int b()
{}
        """
        expect = "Function b Not Return "
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
float thang()
{}
void main()
{
    int a;
}
        """
        expect = "Function thang Not Return "
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_return_in_if_15(self):
        input = """
int a;
void main()
{
    int a;
    boolean xyz;
    if (xyz)
    {
        return 3;
    }
}
        """
        expect = "['Correct']"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_return_in_if_16(self):
        input = """
int a;
void main()
{
    int a;
    boolean xyz;
    if (xyz)
    {
        return 3;
    }
}
boolean haiz(int a)
{
    int xyz;
    if (xyz)
    {
        int y;
        return true;
    }
}
        """
        expect = "Type Mismatch In Statement: xyz"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test__in_if_19(self):
        input = """
int a;
void main()
{
    int a;
    boolean xyz;
    if (xyz)
    {
        return 3;
    }
}
boolean haiz(int a)
{
    int xyz;
    if (xyz)
    {
        int y;
        return true;
    }
}
        """
        expect = "Type Mismatch In Statement: xyz"
        self.assertTrue(TestChecker.test(input, expect, 419))



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