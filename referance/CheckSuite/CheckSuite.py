import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

	###------------------- 1. Redeclared Variable/Function/Parameter ---------------------------###
    # From test 1 -> 8: 9 test

	#test 1
    def test_redeclared_variable_at_global_otherside_int_arrayint(self):
        input = """
        int a;
        void main() {
        	return;
        }
        int a[2];
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

	#test 2
    def test_redeclared_variable_at_global_string_boolean(self):
        input = """
        int a1, a2, a3[5];
        boolean b1,b2[5];
        string b1;
        void main() {
            int a; a = 1;
        	return;
        }
        """
        expect = "Redeclared Variable: b1"
        self.assertTrue(TestChecker.test(input,expect,401))

    #test 3
    def test_redeclared_variable_at_global_vardecl_funcdecl(self):
        input = """
        int a1, a2, a3[5];
        void mety() {
            int a1, a2, a3[5];
            return;
        }
        string mety;
        void main() {
            mety();
            return;
        }
        """
        expect = "Redeclared Variable: mety"
        self.assertTrue(TestChecker.test(input,expect,402)) 

    #test 4
    def test_redeclared_function_at_global_voidfuncdecl_vardecl(self):
        input = """
        string mety;
        void main() {
            mety();
            return;
        }
        void mety() {
            return;
        }
        """
        expect = "Redeclared Function: mety"
        self.assertTrue(TestChecker.test(input,expect,403))

    #test 5
    def test_redeclared_function_at_global_intfuncdecl_vardecl(self):
        input = """
        boolean mety;
        
        int mety() {
            return 1;
        }

        void main() {
            int a;
            a = mety();
            return;
        }
        """
        expect = "Redeclared Function: mety"
        self.assertTrue(TestChecker.test(input,expect,404))

    #test 6
    def test_redeclared_parameter_in_function(self):
        input = """
        int a1,a2[5];
        boolean b1,b2,b3[5];
        void mety1(int a, int b) {
            a = a + b;
            return;
        }
        int[] mety2(int a, float a) {
            mety1();
            return a2;
        }
        void main() {
            int a[2];
            return;
        }
        
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    #test 7
    def test_redeclared_varible_in_function_variable(self):
        input = """
        float d1,d2,d3;
        void mety1(int a1, boolean a2[], float a3) {
            return;
        }
        void mety2(int a, float b) {
            int vy1,vy2,vy3;

            vy1 = 1;
            vy2 = 2;
            vy3 = 3;

            float vy1[5];

            return;
        }
        void main() {
            mety1();
            mety2();
            return;
        }
        """
        expect = "Redeclared Variable: vy1"
        self.assertTrue(TestChecker.test(input,expect,406))

    # test 8
    # This test also tests does scope work well
    def test_redeclared_varible_in_function_variable_2(self):
        input = """
        boolean vy2[2];
        void mety1(int a1, boolean a2[], float a3) {
            boolean b1,b2,b3;
            {
                boolean b1,b2;
                int a1,a2,a3;
            }
            float a3[5];
            return;
        }

        void main() {
            mety1(1, vy2, 1.1e1);
            return;
        }
        """
        expect = "Redeclared Variable: a3"
        self.assertTrue(TestChecker.test(input,expect,407))      
    
	###------------------- 2. Undeclared Identifier/Function -----------------------------------###
    # From test 9 -> 16: 8 test


    # test 9
    def test_undeclared_identifier_in_function(self):
        input = """
        int a1,a2,a3;
        void main() {
            a1 = 5;
            a5 = 9;
            return;
        }
        """
        expect = "Undeclared Identifier: a5"
        self.assertTrue(TestChecker.test(input,expect,408))

    # test 10
    # This test also tests does scope work well
    def test_undeclared_identifier_in_scope(self):
        input = """
        int a1,a2,a3;
        boolean b1,b2,b3;
        void main() {
            a1 = 5;
            {
                a2 = 6;
                b3 = true;
                float d1;
            }

            d1 = 1.1;
            return;
        }
        """
        expect = "Undeclared Identifier: d1"
        self.assertTrue(TestChecker.test(input,expect,409))

    #test 11
    #This test also tests does scope work well
    def test_undeclared_function_in_function(self):
        input = """
        void main() {
            int a1,a2,a3;
            a1 = 5;
            a3 = 10;
            {
                a2 = 6;
                float d1,d2;
                d2 = 1.5e2;
            }
            putInt(a3);
            mety(a3);
            return;
        }
        """
        expect = "Undeclared Function: mety"
        self.assertTrue(TestChecker.test(input,expect,410))

    #test 12
    #This test also tests does scope work well
    def test_undeclared_identifier_in_functioncall(self):
        input = """
        int mety(int a1, int a2, int a3) {
            return a1 + a2 + a3;
        }

        void main() {
            int a1,a2,a3;
            a1 = 2; a2 = 3; a3 = 4;
            {
                if (a1 == 2) {
                    a2 = 6;
                }   
                else a3 = 6;
            }
            a1 = mety(a1,a2,a3);
            a2 = mety(a1 + 1,a2 + 2,a4 + 4);
            return;
        }
        """
        expect = "Undeclared Identifier: a4"
        self.assertTrue(TestChecker.test(input,expect,411))

    #test 13
    #This test also tests does scope work well
    def test_undeclared_function_in_functioncall(self):
        input = """
        float vy1,vy2,vy3[5];
        int mety(int a1, int a2, int a3) {
            return a1 + a2 + a3;
        }

        void main() {
            int a1,a2,a3;
            a1 = 2; a2 = 3; a3 = 4;
            {
                for (a1 = 1; a1 < 5; a1 = a1 + 1) {
                    vy3[a1] = 1;
                }
            }
            a1 = mety(a1,a2,a3);
            a1 = mety(mety(a1,a2,a3),a2,a3);
            a2 = mety(mety1(),a2,a3);
            return;
        }
        """
        expect = "Undeclared Function: mety1"
        self.assertTrue(TestChecker.test(input,expect,412))

    #test 14
    def test_undeclared_function_in_arraycell(self):
        input = """
        float vy1,vy2,vy3[5];
        boolean mety(int a1, int a2, int a3) {
            return a1 == a2;
        }
        boolean[] mety1(int a1, int a2, int a3) {
            boolean b[3];
            b[0] = a1 == 1;
            b[1] = a2 == 2;
            b[2] = a3 == 3;
            return b;
        }

        void main() {
            boolean b1,b2,b3,b4[3];
            b1 = mety1(1,3,4)[0];
            b2 = mety1(1,5,3)[1];
            b3 = mety1(1,2,3)[2];

            b4[0] = mety(1,2,3);
            b4[1] = mety2(1,2,3)[2];

            return;
        }
        """
        expect = "Undeclared Function: mety2"
        self.assertTrue(TestChecker.test(input,expect,413)) 

    #test 15
    def test_undeclared_identifier_in_arraycell(self):
        input = """
        float vy1,vy2,vy3[5];
        int[] mety(int a1) {
            int a2[5];
            a2[0] = a1;
            a2[1] = a1 + 1;
            a2[2] = a1 + mety1(a2);
            a2[3] = a1 * 2;
            a2[3] = a1 % 3;

            return a2;
        }

        int mety1(int a[]) {
            return a[1];
        }

        void main() {
            int a,b,c;
            {
                a = mety1(mety(1));
                b = mety1(mety(2));
                vy1 = 1.1e1;
                {
                    vy2 = 2.2e2;
                    vy3[0] = 3.3e3;
                }
            }
            {
                a = 1; b = 2; c = 3;
                a = mety(5)[a + b + c + d];
            }
            return;
        }
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,414))    

    #test 16
    def test_call_function_redeclared_variable(self):
        input = """

        int mety(int a1, int a2) {
            return a1 + a2;
        }

        void main() {
            int vy1,vy2,vy3;
            vy2 = 1; vy3 = 1;
            vy1 = mety(vy2,5);
            vy2 = mety(vy3,10);
            {
                int mety;
                mety = vy1 + vy2;
                vy3 = mety(1,2);
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(mety),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,415))

	###------------------- 3. Type Mismatch In Statement ---------------------------------------###

    #test 17
    # it also test true case: ==, !=, && return booltype
    def test_typemismatchinstatement_If_IntType(self):
        input = """

        int main() {
            int a1,a2,a3,a4;
            a1 = 1; a2 = 2; a3 = 3;
            if (a1 == 1) {
                a4 = 1;
            }
            else a4 = 10;
            if (a2 != 1) {
                a4 = a4 + 1;
            }

            float d1,d2,d3;

            if (a3 != 1 && a4 != 2) d1 = 1.1;
            else d1 = 0.1;


            //error here
            if (a1) a1 = a1 + 1;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a1),BinaryOp(=,Id(a1),BinaryOp(+,Id(a1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,416))

    #test 18
    # it also test true case: >, <, <=, >=, || return booltype
    def test_typemismatchinstatement_If_FloatType(self):
        input = """

        int main() {
            int a1,a2,a3,a4;
            a1 = 1; a2 = 2; a3 = 3;
            if (a1 > 1) {
                a4 = 1;
            }
            else a4 = 10;

            if (a2 < 1) {
                a4 = a4 + 1;
            }

            float d1,d2,d3;

            if (a3 >= 1 || a4 <= 2) d1 = 1.1;
            else d1 = 0.1;

            //error here
            if (d2 = 2.5e3) a1 = a1 + 1;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(=,Id(d2),FloatLiteral(2500.0)),BinaryOp(=,Id(a1),BinaryOp(+,Id(a1),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,417))


    #test 19
    # this test also test: boolean func; int func; break,continue in for
    def test_typemismatchinstatement_For_IntType_as_Exp3(self):
        input = """
        boolean mety() {
            return true;
        }
        int mety1() {
            return 1;
        }
        int main() {
            int a,b,c;
            float f;
            if(mety()) a = 1;
            else a = 2;


            for (b = 1; b < 10; b = b + 1) {
                a = a + 1;
                if (a >= 5) break;
            } 
            for (c = 2; c < 20; c = c + 1) {
                a = mety1();
                if (c % 10 == 0) continue;
            }
            for (mety1(); mety(); mety1()) a = a + 1;
            //error here
            for (mety1(); mety(); mety()) a = a + 2;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(CallExpr(Id(mety1),[]);CallExpr(Id(mety),[]);CallExpr(Id(mety),[]);BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,418))

    #test 20
    def test_typemismatchinstatement_For_BoolType_as_Exp2(self):
        input = """
        boolean[] mety() {
            boolean a[2];
            a[0] = true;
            a[1] = false;
            return a;
        }
        int[] mety1() {
            int a[2];
            a[0] = 1;
            a[1] = 0;
            return a;
        }
        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            for (mety1()[0]; b != 10; mety1()[1]) {
                b = b + 1;
            } 
            for (mety1()[0]; c != 10; mety1()[1]) {
                c = c + 1;
            }
        
            //error here
            for (mety1()[0]; mety1()[0]; mety1()[0]) a = a + 2;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(ArrayCell(CallExpr(Id(mety1),[]),IntLiteral(0));ArrayCell(CallExpr(Id(mety1),[]),IntLiteral(0));ArrayCell(CallExpr(Id(mety1),[]),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,419))


    #test 21
    # this test also test: !
    def test_typemismatchinstatement_For_IntType_as_Exp1(self):
        input = """

        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            boolean vy;
            vy = !(a >= 10);
            if (!vy) a = 10;
            //error here
            for (a == 1; b != 10; c = c + 1) b = b + 2;
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(==,Id(a),IntLiteral(1));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,420))

    #test 22
    # this test also test: block visit
    def test_typemismatchinstatement_Dowhile_BoolType_as_Condition(self):
        input = """

        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                b = b + 2;
                c = c + 3;
                {
                    int a,b;
                    a = 1; b = 1; c = 1;
                }
            while (a <= 10 && b <= 10 || c <= 20);
            //error
            do
            {
                a = a + 1;
            }
            while (a = a + 1);
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,421))

    #test 23
    # this test also test: continue, break in dowhile
    def test_typemismatchinstatement_return_inttype_voidtype(self):
        input = """
        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                b = b + 2;
                c = c + 3;
                if (c % 10 != 0) continue;
                if (c % 10 == 0) break;
            while (a <= 10 && b <= 10 || c <= 20);
            //error
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,422))

    #test 24
    def test_typemismatchinstatement_return_voidtype_floattype(self):
        input = """
        void main() {
            mety();
            return;
        }
        void mety() {
            return 1.1;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,423))

    #test 25
    def test_typemismatchinstatement_return_arraypointertype_inttype(self):
        input = """
        int mety() {
            return 1;
        }
        void main() {
            int a,b;
            a = mety();
            b = mety1()[0];
            return;
        }
        int[] mety1() {
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,424))

    #test 26
    def test_typemismatchinstatement_return_arraypointertype_eletype(self):
        input = """
        int[] mety() {
            int vy[2];
            vy[0] = 1;
            vy[1] = 2;
            return vy;
        }
        boolean[] mety1() {
            boolean vy1[2];
            vy1[0] = true;
            vy1[1] = false;
            return vy1;
        }
        float[] mety2() {
            float vy2[2];
            vy2[0] = 1.1;
            vy2[1] = 2.2;
            return vy2;
        }
        string[] mety3() {
            string vy3[2];
            vy3[0] = "a";
            vy3[1] = "b";
            return vy3;
        }
        int[] mety4() {
            float vy4[2];
            vy4[0] = 1.1;
            vy4[1] = 2.2;
            return vy4;
        }
        void main() {
            int a,e; boolean b; float c; string d;
            a = mety()[0];
            b = mety1()[0];
            c = mety2()[0];
            d = mety3()[0];
            e = mety4()[0];
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(vy4))"
        self.assertTrue(TestChecker.test(input,expect,425))

    #test 27
    def test_typemismatchinstatement_return_arraypointertype_floattype(self):
        input = """
        int mety1(boolean a[]) {
            int b[3];
            if (a[0]) b[0] = 1; else b[0] = 10;
            if (a[1]) b[1] = 10; else b[1] = 100;
            if (a[2]) b[2] = 100; else b[2] = 1000;
            return b[0] + b[1] + b[2]; 
        } 
        float[] mety() {
            int a[2];
            a[0] = 1; a[1] = 2;
            return a;
        }
        void main() {
            int a;
            a = mety();
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,426))

	###------------------- 4. Type Mismatch In Expression --------------------------------------###

    #test 28
    # this test also tests case: type coerce float and int, arraycell
    def test_typemismatchinexpr_arraycell_E2isFloattype(self):
        input = """
        void main() {
            int a1,a2,a3[10];
            a1 = 1;
            float b1,b2,b3[10];
            a2 = 1000;
            a3[5] = 10;
            a3[6] = 100;
            a3[a1 + a2 + a3[5]] = 100;
            b3[1] = 10.0;
            //type coerce
            b1 = 1.1; b2 = a1;
            b3[2] = 10 + 1.1e1;
            b3[a3[1] + (a3[2] + a3[3])] = b1 * 2 + b2 / 10;
            //error
            a3[b1] = 10;
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a3),Id(b1))"
        self.assertTrue(TestChecker.test(input,expect,427))

    #test 29
    # this test also tests case: arraycell E1 is arraypointertype, arraytype, E2 is Intype
    def test_typemismatchinexpr_arraycell_E1isnotArrayType(self):
        input = """
        void main() {
            int a1,a2,a3[5];
            a1 = 1; a2 = 2;
            a3[0] = a1;
            a3[1] = 1; a3[2] = 2;
            a3[3] = a3[1] + a3[2];

            a1[1] = 1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,428))

    #test 30
    # this test also tests case: arraycell for eletype: string,float,int,boolean
    def test_typemismatchinexpr_arraycell_E2isStringType(self):
        input = """
        int[] mety(int a) {
            int vy[2];
            vy[0] = a / 2;
            vy[1] = a * 2;
            return vy;
        }
        void main() {
            string a[2];
            boolean b[2];
            float c[2];
            int d[2];

            d[0] = 1; d[1] = 0;
            c[0] = 1.1; c[1] = d[1] + 1 + 1.1 + 2.2 * 3;
            a[0] = "hello"; a[d[0]] = "hi";
            b[1] = true; b[d[1]] = c[0] > 2;

            d[0] = mety(3)[1] + mety(2)[a[0]];
            return;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(mety),[IntLiteral(2)]),ArrayCell(Id(a),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(input,expect,429))

    #test 31
    # this test also tests case: type coerce
    def test_typemismatchinexpr_biop_float_string(self):
        input = """
        void main() {
            int a1,a2,a3[2];
            a1 = 1; a2 = 2;
            float b1,b2,b3[2];
            b1 = 1.1; b2 = 2.2 * 2 + 3;
            a3[a1] = 1; a3[a2 - 2] = 10;
            b3[a3[0] / 10] = a1 * a2;
            //error
            b2 = "hello" + 1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(hello),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,430))

    #test 32
    def test_typemismatchinexpr_biop_mod_float(self):
        input = """
        void main() {
            int a1,a2;
            float b1,b2;
            
            a1 = 10 % 2;
            a2 = 10000 % 3;
            b1 = 10 % 3;
            b2 = 100 % 7;
            //error
            a1 = 10 % 2.2;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLiteral(10),FloatLiteral(2.2))"
        self.assertTrue(TestChecker.test(input,expect,431))       

    #test 33
    # this test also tests case: operation of boolean
    def test_typemismatchinexpr_biop_boolean(self):
        input = """
        boolean b1,b2;
        int a1,a2,a3;
        void main() {
            boolean b3,b4;
            a1 = 10; a2 = 200; a3 = 3000;
            b1 = 1 == 2;
            b2 = a1 > a2 || a2 >= a3 || a3 < a1;
            b3 = b1 && b2;

            b1 = a1 != a2;
            b2 = !b1;
            b3 = !(b2 && b1);
            //error
            b4 = b1 || a1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(b1),Id(a1))"
        self.assertTrue(TestChecker.test(input,expect,432))

    #test 34
    def test_typemismatchinexpr_assignment_voidtype(self):
        input = """
        int mety(int a) {
            return a;
        }
        boolean mety1(boolean a) {
            return a;
        }
        float mety2(float a) {
            return a;
        }
        string mety3(string a) {
            return a;
        }
        void mety4(int a) {
            return;
        }
        void main() {
            int a; boolean b; float c;string d;
            a = mety(10); b = mety1(true); c = mety2(2.2e10); d = mety3("hi");

            //error
            a = mety4(111);
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),CallExpr(Id(mety4),[IntLiteral(111)]))"
        self.assertTrue(TestChecker.test(input,expect,433))

    #test 35
    def test_typemismatchinexpr_funcall_missing_para(self):
        input = """
        int mety(int a, string b, int c[]) {
            return 1;
        }
        void main() {
            int a,b,c[2];
            b = 1; c[0] = 1; c[1] = 2;
            a = mety(1,"hello",c);
            //error
            a = mety(1,"hi");
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(mety),[IntLiteral(1),StringLiteral(hi)])"
        self.assertTrue(TestChecker.test(input,expect,434))

    #test 36
    def test_typemismatchinexpr_funcall_wrong_typepara(self):
        input = """
        int mety(int a, string b, int c[]) {
            return 1;
        }
        void main() {
            int a,b,c[2];
            b = 1; c[0] = 1; c[1] = 2;
            a = mety(1,"hello",c);
            string str; str = "hello";
            a = mety(b,str,c);
            //error
            a = mety(1,"hi",b);
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(mety),[IntLiteral(1),StringLiteral(hi),Id(b)])"
        self.assertTrue(TestChecker.test(input,expect,435))

    #test 37
    def test_typemismatchinexpr_funcall_missing_typepara_arraypointertype(self):
        input = """
        int mety(int a, string b, int c[]) {
            return 1;
        }
        void main() {
            int a,b,c[2];
            b = 1; c[0] = 1; c[1] = 2;
            string str; str = "hello";
            float a1[2];
            a1[0] = 1.1; a1[1] = 2.2;
            //error
            a = mety(1,"hi",a1);
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(mety),[IntLiteral(1),StringLiteral(hi),Id(a1)])"
        self.assertTrue(TestChecker.test(input,expect,436))      

    #test 38
    def test_typemismatchinexpr_function_but_used_like_variable(self):
        input = """
        int mety() {
            return 1;
        }
        int mety1() {
            return 2;
        }
        void main() {
            int a; a = mety();
            int mety;
            mety = 1;
            //error
            a = mety1 + 1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(mety1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,437))

    #test 39
    def test_typemismatchinexpr_variable_but_used_like_funcall(self):
        input = """
        int mety() {
            return 1;
        }
        int mety1(int a, int b) {
            return 2;
        }
        void main() {
            int a; a = mety();
            int mety;
            mety = 1;

            int mety1;
            //error
            a = mety1(1,2) + 1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(mety1),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,438))

	###------------------- 5. Function not return ----------------------------------------------###

    #test 40
    # this test also tests for case: return in if, else; return in another block
    def test_functionnotreturn_intfucntion(self):
        input = """
        int mety(boolean a) {
            if (a == true) {
                return 0;
            }
            else
            {
                return 1;
            }
        }
        int mety1(boolean a) {
            {
                return 1;
            }
        }
        //error
        int mety2() {

        }
        void main() {
            int a;
            boolean b;
            b = true;
            a = mety(b);
            a = mety1(b);
            a = mety2();
            return;
        }
        """
        expect = "Function mety2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,439))

    #test 41
    # this test also tests for case: return in if, else in if; multiif
    def test_functionnotreturn_for(self):
        input = """
        int mety(boolean a, int b) {
            if (a == true) {
                if (b >= 1) return 10;
                else return 20;
            }
            else
            {
                return 1;
            }
        }
        int mety1() {
            int a;
            for (a = 1; a < -1; a = a + 1) {
                return 1;
            }

            {
                int a;
                a = 1;
            }
            return 1;
        }
        //error
        int mety2() {
            int a;
            for (a = 1; a < -1; a = a + 1) {
                return 1;
            }
        }
        void main() {
            int a;
            boolean b;
            b = true;
            a = mety(b,1);
            a = mety1();
            a = mety2();
            return;
        }
        """
        expect = "Function mety2 Not Return "
        self.assertTrue(TestChecker.test(input,expect,440))

    #test 42
    # this test also tests for case: return in if missing else but have outside; if in dowhile
    def test_functionnotreturn_if_missing_else(self):
        input = """
        int mety(boolean a, int b) {
            if (a == true) {
                return 1;
            }
            b = 3;
            b = 4;
            return b;
        }
        int mety2(int a) {
            int b;
            do
                b = 2;
                a = a + 1;
                return 1;
            while a < 10;
        }

        int mety3(int a) {
            do
                a = a + 1;
                if (a > 10) return 1;
                else return 2;
            while a < 100;
        }
        //error
        int mety1(int c) {
            if (c > 10) return c;
        }
        void main() {
            int a;
            boolean b;
            b = true;
            a = mety(b,1);
            a = mety1(1);
            a = mety2(1);
            a = mety3(1);
            return;
        }
        """
        expect = "Function mety1 Not Return "
        self.assertTrue(TestChecker.test(input,expect,441))

    #test 43
    # this test also tests for case: return in if missing else but have outside; if in dowhile
    def test_functionnotreturn_if_missing_else_in_dowhile(self):
        input = """
        void mety(int a, float b, string c, boolean d) {
            int vy1; vy1 = getInt();
            putInt(vy1);
            putInt(vy1);
            float vy2;
            vy2 = getFloat();
            putFloat(vy2);
            putFloatLn(vy2);
            putBool(d);
            putBoolLn(d);
            putString(c);
            putStringLn(c);
            putLn();
        }
        void mety2(int b, int c[]) {
            int a,d,e;
        }
        int mety1() {
            do {
                if (true) return 1;
            }
            while(true);
        }
        void main() {
            mety(); mety2();
            int a; a = mety1();
            return;
        }
        """
        expect = "Function mety1 Not Return "
        self.assertTrue(TestChecker.test(input,expect,442))

	###------------------- 6. Break/Continue not in loop ---------------------------------------###

    #test 44
    def test_functionnotreturn_break_not_in_loop(self):
        input = """
        int mety(int a) {
            int b;
            for(b = 0; b < a; b = b + 1) {
                if (b > a / 2) break;
                else continue;
            }
            int c; c = 1;
            for(b = 0; b < a; b = b + 1) {
                c = c + b;
                continue;
            }
            return c;
        }

        int mety1(int a) {
            //error
            if(a > 1) break;
            return 1;
        }
        void main() {
            int a; 
            a = mety(10);
            a = mety(10);
            return;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,443))

    #test 45
    # this test also tests for case: return in if missing else but have outside; if in dowhile
    def test_functionnotreturn_continue_not_in_loop(self):
        input = """
        int mety(int a) {
            int b;
            b = 0;
            do
                b = 0;
                b = b + 1;
                if (b > a / 2) break;
            while b < a;

            int c; c = 0;

            do
                c = c + b;
                if (c % 3 == 0) continue;
                c = c + 1;
            while c < 1000;

            return c;
        }
        int mety1(int a) {
            //error
            if(a > 1) continue;
            return 1;
        }

        void main() {
            int a; 
            a = mety(10);
            a = mety1(10);
            return;
        }

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))

	###------------------- 7. No Entry Point ---------------------------------------------------###

    #test 46
    def test_noentrypoint_missing_main_function(self):
        input = """
        int vy1,vy2,vy3;
        void mety() {
            return;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,445))

    #test 47
    def test_noentrypoint_having_main_variable(self):
        input = """
        int vy1,vy2,vy3;
        float main;
        void main2() {
            main1();
        }
        void main1() {
            main2();
            return;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,446))


	###------------------- 8. Unreachable function ---------------------------------------------###

    #test 48
    def test_unreachable_function_mety1_call_mety1(self):
        input = """
        void mety() {
            return;
        }
        int mety1(){
            mety1();
            return 1;
        }
        void main() {
            float vy;
            vy = mety2();
            mety();
        }
        float mety2() {
            return 0.1;
        }
        """
        expect = "Unreachable Function: mety1"
        self.assertTrue(TestChecker.test(input,expect,447))

    #test 49
    def test_unreachable_function_mety2_hide_funcdecl(self):
        input = """
        void mety() {
            mety1();
            return;
        }
        int mety1(){
            mety();
            return 1;
        }
        int mety2(int a) {
            if (a == 0) return 1;
            int b,c;
            b = 1; c = 10;
            return (a + b) * c * mety2(a - 1);
        }
        void main() {
            int mety2;
            mety2 = 2;
            mety2;
        }
        """
        expect = "Unreachable Function: mety2"
        self.assertTrue(TestChecker.test(input,expect,448))


    #test 50
    def test_unreachable_function_mety3_not_call_testbuiltin_function(self):
        input = """

        int mety(int a) {
            int vy1; vy1 = getInt();
            putInt(vy1);
            putInt(vy1);
            float vy2;
            vy2 = getFloat();
            putFloat(vy2);
            putFloatLn(vy2);
            boolean d; d = true;
            putBool(d);
            putBoolLn(d);
            string c; c = "hello";
            putString(c);
            putStringLn(c);
            putLn();
            return a;
        }
        void main() {
            return;
        }
        int[] mety3(int a[]) {
            a[0] = mety(1);
            return a;
        }
        """
        expect = "Unreachable Function: mety3"
        self.assertTrue(TestChecker.test(input,expect,449))

    #test 51
    def test_unreachable_function_mety_not_call(self):
        input = """
        int mety(int a) {
            return a + mety1(a);
        }
        int mety2(int a) {
            return a * mety3(a);
        }
        void main() {
            int a; a = mety1(10);
            return;
        }
        int mety1(int a) {
            return 2 * a + mety2(a);
        }
        int mety3(int a) {
            return a * a + mety4(a);
        }
        int mety4(int a) {
            return a / 2;
        }
        """
        expect = "Unreachable Function: mety"
        self.assertTrue(TestChecker.test(input,expect,450))

    #test 52
    def test_unreachable_function_mety_not_call_2(self):
        input = """
        int menu(int stage) {
            //stage
            //1: print
            //2: load
            //else: save
            if (stage == 1) {
                print(5);
                return 1;
            }
            else if (stage == 2) {
                load(6);
                return 2;
            }
            else {
                save(7);
                return 3;
            }
        }

        void main() {
            int a; 
            a = menu(2);
            a = menu(1);
            a = menu(3);
            a = menu(100);
            return;
        }
        void print(int a) {
            putInt(a);
        }
        void load(int a) {
            putInt(a);
        }
        void save(int a) {
            putInt(a);
        }
        int mety() {
            menu(1);
            return 1;
        }
        """
        expect = "Unreachable Function: mety"
        self.assertTrue(TestChecker.test(input,expect,451))

	###------------------- 9. Not Left Value ---------------------------------------------------###   

    #test 53
    def test_notleftvalue_assign_left_binop(self):
        input = """

        void main() {
            int a1,a2,a3,a4[3];
            float f1,f2,f3,f4[3];
            a2 = 1;
            a3 = 1;
            a4[0] = 1; a4[1] = 2;
            a1 = 1;
            a4[a3 + 1] = a4[a3 - a3];
            f1 = 1.0;
            f2 = f1 * 2.3; f2 = f2 / 1.2;
            f3 = f2 * 2 * 100.0;
            f4[1] = 1.3 * f1;
            //error
            f1 + f2 = f3;

            return;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(f1),Id(f2))"
        self.assertTrue(TestChecker.test(input,expect,452))

    #test 54
    def test_notleftvalue_assign_left_intlit(self):
        input = """
        void main() {
            int getInt;
            float getFloat;
            getInt = 1000;
            getFloat = getInt;

            if (getInt == 0900) {
                //error
                9 = getInt;
            }
            return;
        }
        """
        expect = "Not Left Value: IntLiteral(9)"
        self.assertTrue(TestChecker.test(input,expect,453))

    #test 55
    def test_notleftvalue_assign_left_uop(self):
        input = """
        int[] mety(int a) {
            int b[2];
            b[0] = 10 * a;
            b[1] = 100 * a;
            return b;
        }
        void main() {
            int a;
            a = 10;

            if (true) -a = mety(5)[0] + 100;
        }
        """
        expect = "Not Left Value: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,454))

    #test 56
    def test_notleftvalue_assign_left_callexp(self):
        input = """
        int mety(int abc) {
            int vy[2];
            vy[0] = 10 * abc;
            vy[1] = 100 * abc;
            return vy[0] * vy[1];
        }
        void main() {
            int a;
            a = getInt();
            if (a == 5) mety(2) = a;
        }
        """
        expect = "Not Left Value: CallExpr(Id(mety),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,455))

    #test 57
    def test_notleftvalue_assign_left_binop_arrpointertype(self):
        input = """
        int main() {
            int a;
            int b[10]; 
            a = getInt();
            if (a == 1) {
                a + 4 = 10;
            }
            else {
                b[0] = 100;
            }
            return 1;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(4))"
        self.assertTrue(TestChecker.test(input,expect,456))

	###------------------- 10. Unreachable statement -------------------------------------------###

    #test 58
    def test_unreachable_statement_normal_return(self):
        input = """
        int main() {
            return 1;
            int a;
        }
        """
        expect = "Unreachable Statement: VarDecl(a,IntType)"
        self.assertTrue(TestChecker.test(input,expect,457))

    #test 59
    def test_unreachable_statement_normal_return_check_if(self):
        input = """
        int main() {
            int a; a = getInt();
            if (a < 10) return a;

            a = 100;
            return a;
            a = getInt();
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),CallExpr(Id(getInt),[]))"
        self.assertTrue(TestChecker.test(input,expect,458))

    #test 60
    def test_unreachable_statement_break_continue(self):
        input = """
        void mety(int a, int b) {
            int c; c = getInt();
            int i;
            for (i = 0; i < c; i = i + 1) {
                putInt(a); putInt(b);
                a = a + c; 
                if (a % 2 == 0) continue;
                b = b + i;
            }

            for (i = 0; i < c; i = i + 1) {
                putInt(a); putInt(b);
                a = a + 3 * c;
                if (a < 20) continue;
                else break;
                //error
                b = b + i;
            }
        }
        int main() {
            mety(10,20);
            return 1;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(b),BinaryOp(+,Id(b),Id(i)))"
        self.assertTrue(TestChecker.test(input,expect,459))


    #test 61
    def test_unreachable_statement_if_else(self):
        input = """
        int mety(int a, int b) {
            int c; c = getInt();
            int i;
            for (i = 0; i < c; i = i + 1) {
                putInt(a); putInt(b);
                if (a % 2 == 0) continue;

                a = a + 1;
                if (b % 3 == 0) break;

                b = b + 2;
                if (a < 100 && b > 50) return a + b;

                a = b;
                return 1;
            }

            if (a > 1) {
                if (b > 1) return 1;
                else b = 1;
            }
            else
            {
                a = 1;
                return 1;
            }

            return  1;
        }
        int main() {
            mety(10,20);
            int a; a = getInt();
            if (a > 1) {
                if (a < 10) return 1;
                else return 2;
            }
            else return 3;

            a = 1;
            return a;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,460))

    #test 62
    def test_unreachable_statement_continue(self):
        input = """
        void main() {
            int vy; vy = getInt();
            int i;
            for (i = 0; i < 100; i=i+1) {
                putInt(i);
                if (i == 50) return;

                if (i % 35 == 0) {
                    i = i + 5;
                    break;
                }
                i = i / 2;
                continue;
                i = 1;
            }
            return ;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(i),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,461))

    #test 63
    def test_unreachable_statement_break(self):
        input = """
        void main() {
            int vy; vy = getInt();
            int i;
            for (i = 0; i < 100; i=i+1) {
                putInt(i);
                if (i == 50) return;

                if (i % 35 == 0) {
                    i = i + 5;
                    continue;
                }
                i = i / 2;
                break;
                i = 1;
            }
            return ;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(i),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,462))

    #test 64
    def test_unreachable_statement_dowhile(self):
        input = """
        void main() {
            int a;
            a = getInt();
            do
                a = a + 1;
                putInt(a);
                a = a * 2;
                putInt(a);
                if(a % 3 == 0) break;

                a = a + 1;
                if(a % 3 == 1) return;
                a = 1;
                return;
            while a < 10;

            int a;
            return;
        }
        """
        expect = "Unreachable Statement: VarDecl(a,IntType)"
        self.assertTrue(TestChecker.test(input,expect,463))

    #test 65
    def test_unreachable_statement_dowhile_1(self):
        input = """
        void main() {
            int a;
            a = getInt();
            do
                if (a > 10) return;
                else break;
                a = a + 1;
            while a <= 10;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,464))

    #test 66
    def test_unreachable_statement_dowhile_2(self):
        input = """
        void main() {
            int a;
            a = getInt();
            do
                if (a > 10) return;
                else break;
                a = a + 1;
            while a <= 10;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,465)) 

    #test 67
    def test_unreachable_statement_dowhile_3(self):
        input = """
        void main() {
            int a;
            a = getInt();
            do
                if (a > 10) {
                    if (a % 2 == 0) return;
                    else break;
                }
                a = 1;
                return;
                a = 2;
            while a <= 10;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,466))

    #test 68
    def test_unreachable_statement_dowhile_4(self):
        input = """
        void main() {
            int a;
            a = getInt();
            do
                if (a > 10) return;
                else break;
                a = a + 1;
            while a <= 10;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,467))

    #test 69
    def test_unreachable_statement_dowhile_5(self):
        input = """
        int main() {
            int a;
            a = getInt();
            for (a; a < 10; a = a + 1) {
                return 1;
            }
            a = 8;
            do
                a = a + 1;
                break;
            while a <= 10;
            a = 9;
            do
                a = a + 1;
                return 1;
            while a <= 10;
            a = 10;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,468)) 

	###------------------- 11. Index out of range ----------------------------------------------###

    #test 70
    def test_indexoutofrange_index_is_intlit(self):
        input = """
        int main() {
            int a[10],b;
            a[1] = 0;
            b = 8;
            a[b] = 10;
            a[b + 10] = 10;
            //error
            a[11] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(11))"
        self.assertTrue(TestChecker.test(input,expect,469))

    #test 71
    def test_indexoutofrange_index_is_intlit_neg(self):
        input = """
        int main() {
            int a[10],b;
            a[2] = 0;
            b = 8;
            a[-b] = 10;
            a[-b + 10] = 10;
            //error
            a[-1] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,470))

    #test 72
    def test_indexoutofrange_index_is_binop(self):
        input = """
        int main() {
            int a[10],b; b = 1;
            a[100 + b] = 100;
            //error
            a[12 + 13] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,IntLiteral(12),IntLiteral(13)))"
        self.assertTrue(TestChecker.test(input,expect,471))

    #test 73
    def test_indexoutofrange_index_is_const_expr_1(self):
        input = """
        int main() {
            int a[10],b; b = 1;
            a[100 * b - 12] = 100;
            //error
            a[1000 - 101 * 2] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(-,IntLiteral(1000),BinaryOp(*,IntLiteral(101),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,472))

    #test 74
    def test_indexoutofrange_index_is_const_expr_2(self):
        input = """
        int main() {
            int a[10],b; b = 1;
            a[100 % b] = 100;
            //error
            a[12 % 13] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(%,IntLiteral(12),IntLiteral(13)))"
        self.assertTrue(TestChecker.test(input,expect,473))

    #test 75
    def test_indexoutofrange_index_is_const_expr_3(self):
        input = """
        int main() {
            int a[10],b; b = 1;
            a[100 * b - 12] = 100;
            //error
            a[15 * (10 - (12 + 2))] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(*,IntLiteral(15),BinaryOp(-,IntLiteral(10),BinaryOp(+,IntLiteral(12),IntLiteral(2)))))"
        self.assertTrue(TestChecker.test(input,expect,474))

    #test 76
    def test_indexoutofrange_index_is_const_expr_4(self):
        input = """
        int main() {
            int a[10],b; b = 1;
            //a[100 % b] = 100;
            //error
            a[10 + 12 % 3 + 10 % 2] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(+,BinaryOp(+,IntLiteral(10),BinaryOp(%,IntLiteral(12),IntLiteral(3))),BinaryOp(%,IntLiteral(10),IntLiteral(2))))"
        self.assertTrue(TestChecker.test(input,expect,475))

    #test 77
    def test_indexoutofrange_index_arraycell_in_index(self):
        input = """
        int main() {
            int a[10];
            a[a[10] + 100] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,476))

    #test 78
    def test_indexoutofrange_index_binop_divide(self):
        input = """
        int main() {
            int a[10];
            a[19 / 2] = 10;
            a[21 / 2] = 10;
            return 1;
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),BinaryOp(/,IntLiteral(21),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,477))


	###------------------- 12. Uninitialized Variable ------------------------------------------###

    #test 79
    def test_uninitializedvariable_callexp(self):
        input = """
        int main() {
            int a,b,c;
            a = 1;
            b = a;
            b = b;
            putInt(a);
            putInt(b);
            //error
            putInt(c);
            return 1;
        }
        """
        expect = "Uninitialized Variable: c"
        self.assertTrue(TestChecker.test(input,expect,478))

    #test 80
    def test_uninitializedvariable_redecl_in_another_scope(self):
        input = """
        int main() {
            int a,b,c;
            a = 0; b = 1; c = 2;
            {
                int a;
                //error
                b = a;
            }
            return 1;
        }
        """
        expect = "Uninitialized Variable: a"
        self.assertTrue(TestChecker.test(input,expect,479))

    #test 81
    def test_uninitializedvariable_redecl_in_another_scope_2(self):
        input = """
        string a,b,c;
        int d;
        int main() {
            a = "hello";
            b = "hi";
            b = c;
            int a,b,c;
            a = 0; b = 1; c = d;
            {
                int a,e;
                {
                    string a;
                    a = "hello";
                    e = 10;
                }
                //error
                e = a * 2;
            }
            return 1;
        }
        """
        expect = "Uninitialized Variable: a"
        self.assertTrue(TestChecker.test(input,expect,480))

    #test 82
    def test_uninitializedvariable_inttype_self_assgin(self):
        input = """
        int a; string b; float c; boolean d;
        int main() {
            putIntLn(a); putBoolLn(d);
            putFloatLn(c); putStringLn(b);
            {
                int b,c,d;
                c = 10; d = 100;
                for (b = 1; b < 10; b = b + 1) {
                    int i;
                    i = 1;
                    c = c + i;
                    string a;
                }
                float l;
                l = 10;
                {
                    float k,l;
                    k = 10;
                    //error
                    k = l;
                }
            }
            return 1;
        }
        """
        expect = "Uninitialized Variable: l"
        self.assertTrue(TestChecker.test(input,expect,481))

    #test 83
    def test_uninitializedvariable_in_func_decl(self):
        input = """
        int vy1,vy2,vy3;
        int mety(int a, int b, int c) {
            int foo1,foo2,foo3,foo4;
            foo1 = a; foo2 = b; foo3 = c;
            foo1 = vy1; foo2 = vy2; foo3 = vy3;
            return foo4;
        }   
        int main() {
            vy1 = mety(2,3,4);
            return 1;
        }
        """
        expect = "Uninitialized Variable: foo4"
        self.assertTrue(TestChecker.test(input,expect,482))

    ###------------------- 13. Addition ------------------------------------------###
    
    #test 84
    def test_redeclared_builtin_function(self):
        input = """
        int mety(int a) {
            return a;
        }
        int putInt(int i) {
            return i;
        }
        void main() {
            return;
        }
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,483))

    #test 85
    def test_redeclared_builtin_function_1(self):
        input = """
        int mety(int a) {
            return a;
        }
        void putInt(int i) {
            return;
        }
        void main() {
            int a;
            a = mety(1); putInt(1);
            return;
        }
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,484))

    #test 86
    def test_redeclared_builtin_function_2(self):
        input = """
        string getFloat;
        void main() {
            return;
        }
        """
        expect = "Redeclared Variable: getFloat"
        self.assertTrue(TestChecker.test(input,expect,485))


    #test 87
    def test_typemismatchinexpr_inttype_floattype_scope(self):
        input = """
        void main() {
            int a;
            {
                string a;
                a = "hello";
                {
                    a = "hi";
                    boolean a;
                    a = true;
                }
                {
                    a = "That";
                    int a[2];
                    a[0] = 1;
                    {
                        a[1] = 3;
                        float a[2];
                        a[0] = 1;
                        a[1] = 2;
                    }
                    //error
                    a[0] = 1.1;
                }
            }
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input,expect,486))

    #test 88
    def test_typemismatchinexpr_callexpr_as_variable_2(self):
        input = """
        void main() {
            int a,b,c;
            a = putInt;
            b = 1;
            c = 1;
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(putInt))"
        self.assertTrue(TestChecker.test(input,expect,487))

    #test 89
    def test_typemismatchinexpr_return_scope(self):
        input = """
        string foo(string a, string b) {
            if (a == "hello") return "f_1";
            else return b;
        }

        void main() {
            string a,b;
            b = "hi";
            a = foo("hello",b);
            return;
        }
        int a,b,c;
        int foo2(int b, string c) {
            return c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),StringLiteral(hello))"
        self.assertTrue(TestChecker.test(input,expect,488))

    #test 90
    def test_indexOutOfRange_neg_index(self):
        input = """
        
        int main(){
            int a[100];
            a[-2] = 0;          
            return 1;
        }
        
        """
        expect = "Index Out Of Range: ArrayCell(Id(a),UnaryOp(-,IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,489))

    #test 91
    def test_typemismatchinstatement_For_IntType_as_Exp1_1(self):
        input = """

        int main() {
            int a,b,c;
            a = 1; b = 1; c = 1;
            for (1; true; 1) {
                break;
            } 
            for (a + 1; a > b; 1) {
                continue;
            }
            for (1; false; -1) {
                return 1;
            }
            for ("1";true;1) {

            }
        }
        """
        expect = "Type Mismatch In Statement: For(StringLiteral(1);BooleanLiteral(true);IntLiteral(1);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    #test 92
    def test_typemismatchinstatement_Dowhile_BoolType_as_Condition_1(self):
        input = """

        int main() {
            int a,b,c;
            boolean d;
            a = 1; b = 1; c = 1;
            do
                a = a + 1;
                a = a * 2;
                a = a / 2;
                if (a > 5 && a < 20) continue;
                else break;
            while(d = a < 10);
            do
                a = b;
                b = c;
                c = a + b;
                if (a > 5 && a < 20) return a;
                else return b;
            while(a - 10);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),Id(b)),BinaryOp(=,Id(b),Id(c)),BinaryOp(=,Id(c),BinaryOp(+,Id(a),Id(b))),If(BinaryOp(&&,BinaryOp(>,Id(a),IntLiteral(5)),BinaryOp(<,Id(a),IntLiteral(20))),Return(Id(a)),Return(Id(b)))],BinaryOp(-,Id(a),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,491))

    #test 93    
    def test_functionnotreturn_if_for(self):
        input = """
        //error
        int mety(int a) {
            int i;
            
            for (i = 0; i < a; i = i + 1) {
                i = i + a;
                return i;
            }
            if (a < 10) return a;
        }
        void main() {
            int a;
            a = mety();
            return;
        }
        """
        expect = "Function mety Not Return "
        self.assertTrue(TestChecker.test(input,expect,492))

    #test 94
    def test_unreachable_statement_main_for(self):
        input = """
        int main() {
            int a; a = 0;
            for (1;true;1) {
                return 1;
            }
            a = a + 1;
            for (2;false;2) {
                return 2;
            }
            a = a + 2;
            for (3;false;3) {
                break;
            }
            a = a + 3;
            for (4;false;4) {
                continue;
            }
            a = a + 4;
            for (4;false;4) {
                if (true) return 1;
                else return 2;
            }
            a = a + 5;
            for (5;false;5) {
                //error
                {
                    {return 1;}
                }
                a = 5;
            }
            return 1;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,493))

    #test 95
    def test_unreachable_statement_main_dowhile(self):
        input = """
        int main() {
            int a; a = 0;
            do
                if (true) continue;
                a = 1;
                if (true) return 1;
            while(true);
            a = a + 1;
            do
                if (true) continue;
                else break;
            while(true);
            a = a + 2;
            do
                if (true) break;
                else continue;
            while(true);
            a = a + 3;
            do
                if (true) return 1;
                else continue;
            while(true);
            a = a + 4;
            do
                if (true) continue;
                else return 1;
            while(true);
            a = a + 5;
            //error
            do
                if (true) return 2;
                else return 1;
            while(true);
            a = a + 6;

            return 1;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(6)))"
        self.assertTrue(TestChecker.test(input,expect,494))

    #test 96
    def test_unreachable_statement_main_dowhile_for(self):
        input = """
        int main() {
            int a; a = 0;
            do
                break;
            while(true);
            a = a + 1;
            do
                continue;
            while(true);
            a = a + 2;
            for (4;false;4) 
                if (true) continue; else break;
            a = a + 3;
            for (4;false;4) 
                if (true) break; else break;
            a = a + 4;
            for (4;false;4) 
                if (true) return 1; else break;
            a = a + 5;
            for (4;false;4) 
                if (true) return 1; else return 1;
            a = a + 6;
            if (true) return 1;
            else return 2;
            return 10;
        }
        """
        expect = "Unreachable Statement: Return(IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,495))

    #test 97
    def test_mismatchInStmt_return_differ_to_voidType(self):
        input = """        
        void main() {
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,496))

    #test 98
    def test_typemismatchinexpr_callexpr_as_variable_3(self):
        input = """        
        void main() {
            int a;
            a = 100 + (putInt % 2);
            return;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(putInt),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,497))

    #test 99
    def test_break_not_in_loop(self):
        input = """        
        void main() {
            int a; a = getInt();
            for (1;true;1) {
                if (a > 10) a = a * 2;

                {
                    if (a < 100) {
                        continue;
                    }
                }
            }

            {
                {   
                    if (a > 100) {
                        break;
                    }
                }
            }
            return;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,498))

    #test 100
    def test_continue_not_in_loop(self):
        input = """        
        void main() {
            int a; a = getInt();
            do {
                a = a + 1;
                {
                    a = a * 2;
                }
                if (a < 10) {
                    {
                        break;
                    }
                }
            }
            while(true);

            {
                {   
                    for (1;true;1) break;
                    
                    if (a > 100) {
                        continue;
                    }
                }
            }
            return;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,499))