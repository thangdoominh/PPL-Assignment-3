import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):

#-------------------------TEST REDECLAREd---------------------------
    def testRedeclared1(self):
        input = """
            int hi;
            int hi;
            void main() {}
        """
        expect = "Redeclared Variable: hi"
        self.assertTrue(TestChecker.test(input,expect,400))

    def testRedeclared2(self):
        input = """
            int a;
            void main() {}
            int a;
            void foo(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def testRedeclared3(self):
        input = """
            int foo;
            void main() {}
            int a;
            void foo(){}
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def testRedeclared4(self):
        input = """
            int a;
            void main(){}
            int foo(int b, float b){
                return 3;
        }
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,403))

    def testRedeclared5(self):
        input = """
            int a;
            void main(){}
            int foo(int b, float c){
                float b;
                {}
                return 3;
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def testRedeclared6(self):
        input = """
            int a;
            void main(){foo(a,a);}
            int foo(int b, float c){
                float var_check;
                {
                    b = 5;
                    int var_check;
                    var_check = 2;
                    putInt(a);
                }
                return 3;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def testRedeclared7(self):
        input = """
            void main(){
                func();
                func2();
            }
            void func(){
                int var_check;
            }
            void func2(){
                int var_check;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))

    def testRedeclared8(self):
        input = """
            int a;
            void main(){
                func(a);
                func2();
            }
            void func(int hello){
                int var;
                {
                    {
                        {
                            int hello;
                        }
                    }
                }
            }
            void func2(){
                int var;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,407))

    def testRedeclared9(self):
        input = """
            void check(){}
            void main(){
                check();
            }
            int check(){return3;}
        """
        expect = "Redeclared Function: check"
        self.assertTrue(TestChecker.test(input,expect,408))

    def testRedeclared10(self):
        input = """
            float main(){
                int a;
                foo3();
                return 1.5;
            }

            void func11(int a1, int a2){}
            int foo3(){
                func11(5,2);
                return 3;
            }
            float func11(){}

        """
        expect = "Redeclared Function: func11"
        self.assertTrue(TestChecker.test(input,expect,409))

    def testRedeclared11(self):
        input = """
            int var;
            int main(){
                foo(3);
                return 2;
            }
            void foo(float arg){
                //abcd
            }
            float var;

        """
        expect = "Redeclared Variable: var"
        self.assertTrue(TestChecker.test(input,expect,410))

    def testRedeclared12(self):
        input = """
            int check(boolean abc){
                if (abc) return 1;
                return 0;
            }
            void main(){
                check2();
            }
            int check;
            int check2(){
                string s;
                s = "hello";
                return check(true);
            }
        """
        expect = "Redeclared Variable: check"
        self.assertTrue(TestChecker.test(input,expect,411))

    def testRedeclared13(self):
        input = """
            int a;
            void main(){foo(a,a);}
            int foo(int b, float c){
                float var_check;
                int b;
                {
                    int b;
                    b = 5;
                    int var_check;
                    var_check = 2;
                }
                return 3;
            }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,412))


#-------------------------TEST UNDECLARE---------------------------
    def testUndeclared1(self):
        input = """
            int foo(int a){return 1;}
            void main(){
                foo(c);
            }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,413))

    def testUndeclared2(self):
        input = """
            void main(){}
            int goo(){
                boolean boo[5];
                booo[3] = 2;
            }

        """
        expect = "Undeclared Identifier: booo"
        self.assertTrue(TestChecker.test(input,expect,414))

    def testUndeclared3(self):
        input = """
            float main(){
                int a;
                foo3();
                return 1.5;
            }

            void func1(int a1, int a2){}
            int foo3(){
                a = 2*5+3;
                func11(5,2);
                return 3;
            }

        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def testUndeclared4(self):
        input = """
            int foo(int a){return 1;}
            void main(){
                foo(b(1));
            }
            """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input,expect,416))

    def testUndeclared5(self):
        input = """
            int var;
            int main(){
                foo(3);
                return 2;
            }
            void foo(float arg){
                putInt(var);
                //abcd
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,417))

    

    def testUndeclared6(self):
        input = """
            void foo(){
                foo();
            }

            void main(){
                int goo;
                foo();
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,418))

    def testUndeclared7(self):
        input = """
            void foo(){
                int foo;
                foo();
            }

            void main(){
                int foo1;
                foo();
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def testUndeclared8(self):
        input = """
            float main(){
                int a;
                foo3();
                return 1.5;
            }

            void func1(int a1, int a2){}
            int foo3(){
                func11(5,2);
                return 3;
            }

        """
        expect = "Undeclared Function: func11"
        self.assertTrue(TestChecker.test(input,expect,420))

    def testUndeclared9(self):
        input = """
            boolean ifCondition(){
                return True;
            }
            int a;
            void main(){
                if (ifCondition()){
                    if (false){}
                    else {a = 1;}
                } 
                else {
                    if (true){
                        if(ifCondition()){
                            if(check(3)) a = 1;
                        }
                        else a = 2;
                    }
                }
            }
            int check(int abc){
                if (abc) return 1;
                return 0;
            }
            
            """
        expect = "Undeclared Identifier: True"
        self.assertTrue(TestChecker.test(input,expect,421))

    def testUndeclared10(self):
        input = """
            int a;
            void main(){}
            int foo(int b, float c){
                {}
                b = 3*x;
                return 3;
            }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,422))

    def testUndeclared11(self):
        input = """
            float fus[55];
            float[] foo(float par[]){
                return par;
            }
            void main(){
                foo2(fus);
            }
        """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,423))


#-------------------------TEST TYPEMISMATCH IN STATEMENT---------------------------
    def testTypeMismatchStmt1(self):
        input = """
            int check(int abc){
                if (abc) return 1;
                return 0;
            }
            void main(){
                check2();
            }
            int check2(){
                string s;
                s = "hello";
                return check(3);
            }
        """
        expect = "Type Mismatch In Statement: If(Id(abc),Return(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def testTypeMismatchStmt2(self):
            input = """
                int a;
                void main(){
                    if (check(3)) a = 1;
                    else a = 0;
                }
                int check(int abc){
                    if (false) return 1;
                    return 0;
                }
            
            """
            expect = "Type Mismatch In Statement: If(CallExpr(Id(check),[IntLiteral(3)]),BinaryOp(=,Id(a),IntLiteral(1)),BinaryOp(=,Id(a),IntLiteral(0)))"
            self.assertTrue(TestChecker.test(input,expect,425))

    def testTypeMismatchStmt3(self):
            input = """
                void foo(){}

                void main(){
                    int foo;
                    foo();
                }

            """
            expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
            self.assertTrue(TestChecker.test(input,expect,426))

    def testTypeMismatchStmt4(self):
            input = """
                int a;
                void main(){
                    if (true){
                        if (true){
                            if(true){
                                if(true) a = 1;
                            }
                        }
                    } 
                    else {
                        if (true){
                            if(true){
                                if(check(3)) a = 1;
                            }
                        }
                    }
                }
                int check(int abc){
                    if (true) return 1;
                    return 0;
                }
            
            """
            expect = "Type Mismatch In Statement: If(CallExpr(Id(check),[IntLiteral(3)]),BinaryOp(=,Id(a),IntLiteral(1)))"
            self.assertTrue(TestChecker.test(input,expect,427))

    def testTypeMisMatchStmt5(self):
            input = """
                boolean ifCondition(){
                    return true;
                }
                int a;
                void main(){
                    if (ifCondition()){
                        if (false){}
                        else {a = 1;}
                    } 
                    else {
                        if (true){
                            if(ifCondition()){
                                if(check(3)) a = 1;
                            }
                            else a = 2;
                        }
                    }
                }
                int check(int abc){
                    if (abc) return 1;
                    return 0;
                }
            
            """
            expect = "Type Mismatch In Statement: If(CallExpr(Id(check),[IntLiteral(3)]),BinaryOp(=,Id(a),IntLiteral(1)))"
            self.assertTrue(TestChecker.test(input,expect,428))

    def testTypeMisMatchStmt6(self):
            input = """
                boolean condition(){
                    return true;
                }
                int a;
                void main(){
                    for (a;condition();3){
                        {
                            if (true){
                                if(condition()){
                                    if(false) a = 1;
                                }
                                else a = 2;
                            }
                        }
                    }
                }
                int check(int abc){
                    if (abc) return 1;
                    return 0;
                }
                
            """
            expect = "Type Mismatch In Statement: If(Id(abc),Return(IntLiteral(1)))"
            self.assertTrue(TestChecker.test(input,expect,429))

    def testTypeMisMatchStmt7(self):
        input = """
            int a,b[5],c;
            float _vi,_int[6];
            string s, str1[3], str2[5], str3[2];
            int main(){
                    for (1;condition();1)
                        s = "Fighting!";
                    main1();
                return 1;
            }
            void main1(){
                    for ("1";true;1)
                        s = "Fighting!";
                    main2();
            }
            int main2(){
                    for (1;false;1)
                        s = "Fighting!";
                    return 2;
            }
            boolean condition(){
                    return true;
                }
        """
        expect = "Type Mismatch In Statement: For(StringLiteral(1);BooleanLiteral(true);IntLiteral(1);BinaryOp(=,Id(s),StringLiteral(Fighting!)))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def testTypeMisMatchStmt8(self):
        input = """
            int var, var2[4];
            int main(){
                    for (1;condition();1){
                        foo();
                    } 
                return 1;
            }
            void goo(){
                    for (1;true;condition()){}
                    foo();
            }
            float _vi,_int[6];
            int foo(){
                    for (1;false;1){
                        s = "Fighting!";}
                goo();
                return 2;
            }
            boolean condition(){
                    return true;
                }
            string s, str1[3], str2[5], str3[2];
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(true);CallExpr(Id(condition),[]);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,431))

    def testTypeMisMatchStmt9(self):
        input = """
            int var, var2[4];
            int main(){
                    for (1;condition();1){
                        foo();
                        for (1;true;str3){
                            for (1;false;1){
                                s = "Fighting!";
                            }
                        }
                        foo();

                    } 
                return 1;
            }
            void foo(){}
            boolean condition(){
                    return true;
                }
            string s, str1[3], str2[5], str3[2];
        """
        expect = "Type Mismatch In Statement: For(IntLiteral(1);BooleanLiteral(true);Id(str3);Block([For(IntLiteral(1);BooleanLiteral(false);IntLiteral(1);Block([BinaryOp(=,Id(s),StringLiteral(Fighting!))]))]))"
        self.assertTrue(TestChecker.test(input,expect,432))

    def testTypeMisMatchStmt10(self):
        input = """
            void main(){
                for (1;true;1){{{{{}}}}}
		    }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,433))

    def testTypeMisMatchStmt11(self):
        input = """
            void main(){
                for (1;true;1){{{{{func();}}}}}
            }
            int[] func(){
                int a[5];
                return a;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def testTypeMismatchStmt12(self):
        input = """
            void foo(int foo){
                int goo;
                foo();
            }

            void main(){
                int foo1;
                foo();
            }

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def testTypeMisMatchStmt13(self):
        input = """
            int foo;
            void main(){
                foo();
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def testTypeMisMatchStmt14(self):
        input = """
            int foo(){
                    do 
                        a=30 ;
                        if(true) a= bb[1];
                        else b=aa[1]= 30;
                    while (a!=b) ;
                return 3;
            }
            void main(){
                foo();
            }
            int a, aa[5], b, bb[5];
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,437))

    def testTypeMisMatchStmt15(self):
        input = """
            void main(){
                foo();
            }
            int a, aa[5], b, bb[5];
            int foo(){
                    do 
                        a=30 ;
                        if(true) a= bb[1];
                        else b=aa[1]= 30;
                    while (1) ;
                return 3;
            }
        """
        expect = "Type Mismatch In Statement: Dowhile([BinaryOp(=,Id(a),IntLiteral(30)),If(BooleanLiteral(true),BinaryOp(=,Id(a),ArrayCell(Id(bb),IntLiteral(1))),BinaryOp(=,Id(b),BinaryOp(=,ArrayCell(Id(aa),IntLiteral(1)),IntLiteral(30))))],IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def testTypeMisMatchStmt16(self):
        input = """
            void main(){
                func();
            }
            int[] func(){
                int a[5];
                return a;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))

    def testTypeMisMatchStmt17(self):
        input = """
            int main(){
                func();
                func1(func(), 2);
                return 1;
            }
            int[] func(){
                int a[5];
                return a;
            }
            void func1(int param1[], int param2){}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))

    def testTypeMisMatchStmt18(self):
        input = """
            int a,b,c;
            float[] foo(){
                int a[5];
                return a;
            }
            int func1(float param1[], int param2){
                return a*2+3;
            }
            void main(){
                foo();
                func1(foo(), 2);
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def testTypeMisMatchStmt19(self):
        input = """
            int main(){
                func();
                func1(func(), 2);
                return 1;
            }
            int[] func(){
                int a[5];
                return a;
            }
            void func1(int param1[], int param2){
                coerCheck();
            }
            int aa;
            float coerCheck(){
                return aa;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,442))
    
    def testTypeMisMatchStmt20(self):
        input = """
            int arr[555];
            void foo(){
                return arr;
            }
            void main(){
                foo();
                return;
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(arr))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def testTypeMisMatchStmt21(self):
        input = """
            int[] func(){
                int a[5];
                return a;
            }
            void func1(int param1[], int param2){
                coerCheck();
            }
            int aa;
            float coerCheck(){
                return "abc";
            }
            int main(){
                func();
                func1(func(), 2);
                return 1;
            }
        """
        expect = "Type Mismatch In Statement: Return(StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def testTypeMisMatchStmt22(self):
        input = """
            void main(){
                return;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def testTypeMisMatchStmt23(self):
        input = """
            int foo(){
                return 3;
            }
            void main(){
                return 3;
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(3))"
        self.assertTrue(TestChecker.test(input,expect,446))

    def testTypeMismatchStmt24(self):
        input = """
            int check(boolean abc){
                if (abc) return 1;
                return 0;
            }
            void main(){
                return check2();
            }
            int check2(){
                string s;
                s = "check(3)/4+3;";
                return check(true);
            }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(check2),[]))"
        self.assertTrue(TestChecker.test(input,expect,447))


#-------------------------TEST TYPEMISMATCH IN EXPRESSION---------------------------
    def testTypeMisMatchex1(self):
        input = """
            int main(){
                int a[5];
                a[5] = 3;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))

    def testTypeMisMatchex2(self):
        input = """
            int main(){
                int a[5];
                a[5] = 3;
                a[2.5] = 3;
                return 1;
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(2.5))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def testTypeMisMatchex3(self):
        input = """
            int main(){
                {
                    int a[5];
                    a[5] = 3;
                    "abc"[5] = 3;
                    return 1;
                }
            }
        """
        expect = "Type Mismatch In Expression: ArrayCell(StringLiteral(abc),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def testTypeMisMatchex4(self):
        input = """
            int[] _main(boolean f, int _id[], int a[]){
                    int x;
                    foo(2)[3+x] = a[_id[2]] +3;
                    int _is;
                    _is = 3333 ;
                    boolean aa[3000];
                    return a;
                }
            void main(){_main(false, foo(3), foo(4));}
            int[] foo(int param){
                int par[5];
                return par;
            }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,451))

    def testTypeMisMatchex5(self):
        input = """
            int x[100];
            void main(){
                x = 2;
            }

        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),IntLiteral(2))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def testTypeMisMatchex6(self):
        input = """
            int main(){
                {
                    func()[a+3];
                    return 1;
                }
            }
            int a;
            int[] func(){
                int a[5];
                return a;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def testTypeMisMatchex7(self):
        input = """
            boolean b_a;
            boolean b_b;
            void main(){
                boolean a;
                a = b_a + b_b;
            }
            
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(b_a),Id(b_b))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def testTypeMisMatchex8(self):
        input = """
            int inta;
            int intb;
            void main(){
                int c;
                c = inta && intb; 
            }
            """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(inta),Id(intb))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def testTypeMisMatchex9(self):
        input = """
            float fa;
            float fb;
            void main(){
                boolean c;
                c = fa == fb;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(fa),Id(fb))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def testTypeMisMatchex10(self):
        input = """
            string str;
            void main(){
                string substr;
                substr = str;
                putString(str);
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,457))

    def testTypeMisMatchex11(self):
        input = """
            string str;
            void main(){
                string substr;
                substr = str + 1;
                putString(str);
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(str),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,458))

    def testTypeMisMatchex12(self):
        input = """
            void main(){
                float f1;
                float f2;
                int res;
                res = f1/f2;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(res),BinaryOp(/,Id(f1),Id(f2)))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def testTypeMisMatchex13(self):
        input = """
            void main(){
                float f1;
                int f2;
                int res;
                res = f1/f2;
            }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(res),BinaryOp(/,Id(f1),Id(f2)))"
        self.assertTrue(TestChecker.test(input,expect,460))

    def testTypeMisMatchex14(self):
        input = """
            void main(){
                foo(3);
            }
            float foo(int param){
                return param;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def testTypeMisMatchex15(self):
        input = """
            int fus[55];
            int[] foo(int param){
                int par[5];
                return par;
            }
            int[] _main(boolean f, int _id[], int a[]){
                    int x;
                    foo(2)[3+x] = a[_id[2]] +3;
                    int _is;
                    _is = 1234 ;
                    boolean aa[3000];
                    return a;
                }
            
            void main(){
                _main(true, foo(2), foo(2));
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,462))

    def testTypeMisMatchex16(self):
        input = """
            int fus[55];
            float[] foo(int par[]){
                return par;
            }
            void main(){
                foo(fus);
            }
        """
        expect = "Type Mismatch In Statement: Return(Id(par))"
        self.assertTrue(TestChecker.test(input,expect,463))

    def testTypeMisMatchex17(self):
        input = """
            int fus[55];
            float[] foo(float par[]){
                return par;
            }
            void main(){
                foo(fus,3);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(fus),IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def testTypeMisMatchex18(self):
        input = """
            int fus[55];
            float[] foo(float par[]){
                return par;
            }
            void main(){
                foo();
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,465))

    def testTypeMisMatchex19(self):
        input = """
            int fus[55];
            float[] foo(float par[]){
                return par;
            }
            void main(){
                foo(55);
            }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(55)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def testTypeMisMatchex20(self):
        input = """
        int main(){
            func();
            func1(func(), 2);
            return 1;
        }
        int[] func(){
            int a[5];
            return a;
        }
        void func1(int param1[], int param2){
            coerCheck();
        }
        int aa;
        float coerCheck(){
            func(2);
            return aa;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(func),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def testTypeMisMatchex21(self):
        input = """
        void main(){
                foo1(foo1(foo1(foo1(1))));
                _main(true, foo(aaa), foo(aaa));
            }
            int aaa[55];
            int[] foo(int par[]){
                return par;
            }
            int[] _main(boolean f, int _id[], int a[]){
                    int x;
                    foo(2)[3+x] = a[_id[2]] +3;
                    int _is;
                    _is = 9e7 ;
                    boolean aa[3000];
                    return a;
                }
            int foo1(int a){
                return 1;
            };
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def testTypeMisMatchex22(self):
            input = """
            int check(boolean abc){
                if (abc) return 1;
                return 0;
            }
            void main(){
                check2();
            }
            int check2(){
                string s;
                s = "check(3)/4+3;";
                return check(1);
            }
            """
            expect = "Type Mismatch In Expression: CallExpr(Id(check),[IntLiteral(1)])"
            self.assertTrue(TestChecker.test(input,expect,469))

    def testTypeMisMatchex23(self):
        input = """
        int a,b,c;
        float[] foo(){
            float a[5];
            return a;
        }
        int func1(float param1[], int param2){
            return a*2+3;
        }
         void main(){
            foo();
            func1(foo(), 2);
            boolean b;
            b = (1+2*3)==(b*8*3) || true && (func1(foo(),88) == 0);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(*,Id(b),IntLiteral(8))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def testTypeMisMatchex24(self):
        input = """
        int a,b,c;
        float[] foo(){
            float a[5];
            return a;
        }
        int func1(float param1[], int param2){
            return a*2+3;
        }
         void main(){
            foo();
            func1(foo(), 2);
            boolean b;
            b = (1+2*3)==(c*8*3) || true && (func1(foo(),88) == 0);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,471))

#-------------------------FUNCTION NOT RETURN---------------------------
    def testNotReturn1(self):
        input = """
            int a;
            int main(){
                for (a;true;3){
                    {
                        if (true){
                            return 0;
                        }
                        else{
                            return 1;
                        }
                    }
                }
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,472))

    def testNotReturn2(self):
        input = """
            int a;
            int main(){
                if (true){
                    return 0;
                }
                else{
                    return 1;
                }
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def testNotReturn3(self):
        input = """
            int a;
            int main(){
                if (true){
                    return 0;
                }
                else{
                }
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,474))

    def testNotReturn4(self):
        input = """
            int a;
            int main(){
                if (true){
                    {
                        {{{}}}
                    }
                }
                else{
                    return 1;
                }
            }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,475))

    def testNotReturn5(self):
        input = """
            int a;
            int main(){
                if (true){
                    {
                        {{{return a;}}}
                    }
                }
                else{
                    return 1;
                }
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,476))

    def testNotReturn6(self):
        input = """
            float foo(){

            }
            void main(){}
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input,expect,477))

#-------------------------TEST BREAK/CONTINUE NOT IN LOOP---------------------------
    def testBreakCont1(self):
        input = """
            float foo(){
                return 3.5;
            }
            void main(){
                break;
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,478))

    def testBreakCont2(self):
        input = """
            float foo(){
                return 3.5;
            }
            void main(){
                if (false){
                    foo();
                    int a;
                    a = 3;
                    break;
                }
                else{}
            }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,479))

    def testBreakCont3(self):
        input = """
            float foo(){
                return 3.5;
            }
            void main(){
                continue;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,480))

    def testBreakCont4(self):
        input = """
            float foo(){
                return 3.5;
            }
            void main(){
                if (false){
                    foo();
                }
                else{
                    foo();
                    int a;
                    a = 3;
                    continue;
                }
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def testBreakCont5(self):
        input = """
            int main(){
                int i;
                for (1; i <= 5; i+1){
                    if (i == 3) {break;}
                }
                return 2;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def testBreakCont6(self):
        input = """
            int main(){
                int i;
                for (1; i <= 5; i+1){
                    if (i == 3) {break;}
                    else {continue;}
                }
                continue;
                return 2;
            }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,483))

    def testBreakCont7(self):
        input = """
            int a,aa[5],b,bb[5];
            float foo(){
                do 
                        a=30 ;
                        if(true) a= bb[1];
                        else b=aa[1]= 30;
                        break;
                    while (a!=b) ;
                return 3;
            }
            void main(){
                foo();
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def testBreakCont8(self):
        input = """
            int a,aa[5],b,bb[5];
            float foo(){
                do 
                        a=30 ;
                        if(true) a= bb[1];
                        else b=aa[1]= 30;
                        continue;
                    while (a!=b) ;
                return 3;
            }
            void main(){
                foo();
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

#-------------------------TEST NO ENTRY POINT---------------------------
    def testNoEntryPoint1(self):
        input = """
            int[] _main(boolean f, int _id[], int a[]){
                    int x;
                    foo(2)[3+x] = a[_id[2]] +3;
                    int _is;
                    _is = 3333 ;
                    boolean aa[3000];
                    return a;
                }
            int[] foo(int par[]){
                return par;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,486))

    def testNoEntryPoint2(self):
        input = """
            void func(){
                int var_check;
            }
            void func2(){
                int var_check;
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,487))

    def testNoEntryPoint3(self):
        input = """
            int var;
            /*int main(){
                foo(3);
                return 2;
            }*/
            void foo(float arg){
                //abcd
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,488))

#-------------------------TEST UNREACHABLE FUNCTION---------------------------
    def testUnreachableFunc1(self):
        input = """
            int var;
            void foo(){}
            void main(){}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,489))

    def testUnreachableFunc2(self):
        input = """
            int foo(){
                    do 
                        a=30 ;
                        if(true) a= bb[1];
                        else b=aa[1]= 30;
                    while (a!=b) ;
                return 3;
            }
            void main(){
                //foo();
            }
            int a, aa[5], b, bb[5];
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,490))

    def testUnreachableFunction3(self):
        input = """
            int foo(){
                main();
                foo();
                return 1;
            }
            void main(){

            }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,491))

#-------------------------TEST NOT LEFT VALUE---------------------------
    def testNotLeftValue1(self):
        input = """
            void main(){
                3 = 2;
            }

        """
        expect = "Not Left Value: IntLiteral(3)"
        self.assertTrue(TestChecker.test(input,expect,492))

    def testNotLeftValue2(self):
        input = """
            int x;
            void main(){
                x + 1 = 2;
            }

        """
        expect = "Not Left Value: BinaryOp(+,Id(x),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def testNotLeftValue3(self):
        input = """
            void main(){
                "abc" = 2;
            }

        """
        expect = "Not Left Value: StringLiteral(abc)"
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def testNotLeftValue4(self):
        input = """
            boolean a;
            void main(){
                !a = 2;
            }

        """
        expect = "Not Left Value: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def testNotLeftValue5(self):
        input = """
            boolean foo(int param){return true;}
            int a_var,m,n,b[13],a[13];
            int main(){
                foo(a[3]) = 3;
                return 0;
            }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(3))])"
        self.assertTrue(TestChecker.test(input,expect,496))


#-------------------------TEST COMBINED AND ADVANCED--------------------------- 
    def testMix1(self):
        input = """
            void main(){
                foo1(foo1(foo1(foo1(1))));
                _main(true, foo(aaa), foo(aaa));
            }
            int aaa[55];
            int[] foo(int par[]){
                return par;
            }
            int[] _main(boolean f, int _id[], int a[]){
                    int x;
                    int addi[5];
                    foo(addi)[3+x] = a[_id[2]] +3;
                    int _is;
                    _is = 1234 ;
                    boolean aa[3000];
                    return a;
                }
            int foo1(int a){
                return 1;
            };
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,497))

    def testMix2(self):
        input = """
            int a;
            string s;
            void main(){
                if (true){
                    if (true){
                        for (a;true;1)
                            s = "Fighting!";
                        if(true){
                            if(true) a = 1;
                        }
                    }
                } 
                else {
                    if (funbool()){
                        if(true){
                            if(funbool()) a = 1;
                        }
                    }
                }
            }
            boolean funbool(){
                int True;
                return True;
            }
            
        """
        expect = "Type Mismatch In Statement: Return(Id(True))"
        self.assertTrue(TestChecker.test(input,expect,498))
        
    def testMix3(self):
        input = """
        boolean foo(int param){return true;}
        int a_var,m,n,b[13],a[13];
        int main(){
			if(foo(3)){
				if(a[m+n] == b[m+1] || 3 == a[a_var * 3]){
					a_var=4;
				}
			}
			else{
				if(a[m+n] == b[m+1] || 3 == a[a_var * 3]){
					a_var=4;
					}
				else{
					do{
						do{
							for(a[3];true;1){
								a[m+n];
							}
						}while(true);

					} while (false || 3 == a[a_var * 3] || a[m+n] == b[m+1]);
				}
			}
            return 0;
		}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))
