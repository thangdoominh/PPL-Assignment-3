import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    #Redeclared Error
    def test_redeclared_global_variable(self):
        input = """
        int a; 
        int a; 
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_variable_function(self):
        input = """
        int main; 
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_local_variable(self):
        input = """
        int b; 
        void main(){
            int a;
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_redeclared_function(self):
        input = """
        int a(){
            return 1;
        }
        void a(){}
        void main(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_parameter(self):
        input = """
        void main(int c, int c){}"""
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_parameter_local_variable(self):
        input = """ 
        void main(int a){
            int a;
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_block_variable(self):
        input = """
        void main(){
            {
                int a;
                int a;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_block_block_variable(self):
        input = """ 
        void main(){
            int a;
            {
                int a;
                {
                    int b;
                    int b;
                }
            }
        }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_arraytype(self):
        input = """
        void main(){
            int a[5];
            int a[3];
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_variable_arraytype(self):
        input = """
        void main(){
            int a;
            int a[10];
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    #Undeclared Error
    def test_undeclared_global_variable(self):
        input = """
        int a;  
        void main(){
            b = 5;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_ifstmt_expr(self):
        input = """
        void main(){
            int b;
            if (a > 5) b = 5;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_undeclared_forstmt_expr(self):
        input = """
        void main(){
            int b;
            for (i; i < 10; i = i + 1){
                b = b + 1;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_dowhilestmt_expr(self):
        input = """
        void main(){
            int b;
            do a = 5; b = b + 1; while(b == 0);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_undeclared_returnstmt_expr(self):
        input = """
        void main(){
            return a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_undeclared_function_priority(self):
        input = """
        void main(){
            foo();
        }
        void fo(){
            f();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_undeclared_function_binaryop_expr(self):
        input = """
        void main(){
            int a;
            a = foo(3)[3];
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_undeclared_function_infunction(self):
        input = """
        int foo(int a){
            return 1;
        }
        void main(){
            int a;
            a = foo(fo(1));
        }
        """
        expect = "Undeclared Function: fo"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_undeclared_identifier_function_priority(self):
        input = """
        void main(){
            a = foo();
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_undeclared_function_identifier_priority(self):
        input = """
        void main(){
            foo() = a;
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_typemismatchstatement_ifstmt(self):
        input = """
        void main(){
            int a;
            if (a) a = 2;
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),BinaryOp(=,Id(a),IntLiteral(2)))"
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_Unreachable_Function_simple(self):
        """Simple program: int main() {} """
        input = """
        int foo(){
          return 1;
        }
        int main(){
          return 1;              
        }"""
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,421))
    def test_Unreachable_Function_complex_more(self):
        input = """
            void foo(int x){return;}
            int MyGirlFriend(){return 100;}
            void main(){
                int a;
                {
                    int a,x;
                    int b;
                    foo(a);
                    x = 2;
                }
            }
            """
        expect = "Unreachable Function: MyGirlFriend"
        self.assertTrue(TestChecker.test(input,expect,501))
    def test_Unreachable_Function_simple2(self):
        """Simple program: int main() {} """
        input = """
        int foo(int a){
          return 1;
        }
        void fragment(){
          foo(3);  
        }
        int main(){
          return 1;              
        }
        """
        expect = "Unreachable Function: fragment"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test_Unreachable_Function_more_simple(self):
        """Simple program: int main() {} """
        input = """
        int a,b,c,d[5];
        void foo(int x){}
        void fa(){}
        void main(){
            int a;
            {
                int a;
                int b;
                foo(a);
            }
        }
        """
        expect = "Unreachable Function: fa"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test_Unreachable_Function_int_complex(self):
        """Simple program: int main() {} """
        input = """
        int a,b,c,d[5];
        int[] foo(int x){
            int a[1];
            return a;
        }
        void main(){
            int x;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test_Unreachable_Function_more_simple_float(self):
        """Simple program: int main() {} """
        input = """
        void thang() {
            return;
        }
        int thang1(){
            thang1();
            return 1;
        }
        void main() {
            float ahihi;
            ahihi = thang2();
            thang();
        }
        float thang2() {
            return 0.1;
        }
        """
        expect = "Unreachable Function: thang1"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test_Redeclared_PutIntLn(self):
        """Simple program: int main() {} """
        input = """
        int i;
        void putIntLn(int a){}
        int f(){
            return 200;
        }
        int a,b,c,d[5];
        void main(){
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main=f=i=100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        
        """
        expect = "Redeclared Function: putIntLn"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test_TypeMismatchInExpression_more_complex(self):
        """Simple program: int main() {} """
        input = """
        void foo(float a[]){}
        void goo(float x[]){
            float y[10];
            int z[10];
            foo(x);
            foo(y);
            foo(z);
        }
        void main(){
        }
        
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(z)])"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test_Redeclared_Function_scope_more_complex(self):
        """Simple program: int main() {} """
        input = """
        void putInt(int x){}
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a+3;
            if (i>0){
                int d;
                d = i+3;
                putInt(d);
            }
            return i;
        }
        void main(){
            int a;
            float b[3];
            foo(a,b);
        }
        
        """
        expect = "Redeclared Function: putInt"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test_scope_undeclare_more_complex(self):
        """Simple program: int main() {} """
        input = """
        int a;
        void main(){
            c=3
            foo();
        }
        int b;
        void foo(){
            b=3;
        }
        
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test_Undeclared_Function_putIntLn(self):
        """Simple program: int main() {} """
        input = """
        int a;
        void main(){
            putint(a);
            foo();
        }
        int b;
        void foo(){
            b=3;
        }
        
        """
        expect = "Undeclared Function: putint"
        self.assertTrue(TestChecker.test(input,expect,430))
   
    def test_Redeclare_Function_NoDiff_Simple(self):
        """Simple program: int main() {} """
        input='''
        int foo(int a){}
        int foo(int a){}
        void main() 
        {
            int a;
            foo(a);
        }
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test_Redeclare_Function_ParamDiff_Simple(self):
        """Simple program: int main() {} """
        input='''
        void foo(int a){}
        void foo(){}
        void main() 
        {
            int a;
            foo(a);
        }
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test_Redeclare_Function_TypeRetDiff_Simple(self):
        """Simple program: int main() {} """
        input='''
        int[] foo(int a)
        {
            int a[1];
            return a;
        }
        float[] foo(float b)
        {
            float b[1];
            return b;
        }
        void main() 
        {
            int a;
            foo(a);
        }
        '''
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test_Redeclare_Variable_NoDiff_Simple(self):
        """Simple program: int main() {} """
        input='''
        void main() 
        {
            int a;
            int a;
        }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test_Redeclare_Variable_TypeDiff_Simple(self):
        """Simple program: int main() {} """
        input='''
        void main() 
        {
            int a;
            float a;
        }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test_Redeclare_Variable_Param_Simple(self):
        """Simple program: int main() {} """
        input='''
        void foo(int a){
            int a;
        }
        void main() 
        {
            int b;
            foo(b);
        }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test_Redeclare_Variable_ParamDiff_MoreSimple(self):
        """Simple program: int main() {} """
        input='''
        void foo(int a){
            float a;
        }
        void main() 
        {
            int b;
            foo(b);
        }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test_Redeclare_Variable_ParamDiff_MoreSimple(self):
        """Simple program: int main() {} """
        input='''
        void foo(int a){
            float a;
        }
        void main() 
        {
            int b;
            foo(b);
        }
        '''
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test_Redeclare_Variable_Block_Simple(self):
        """Simple program: int main() {} """
        input='''
        void main() 
        {
            int a;
            {
                int a;
                int b;
                int b;
            }
        }
        '''
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_Redeclare_Param_Simple(self):
        """Simple program: int main() {} """
        input='''
        void foo(int a, int c, int a){
        }
        void main() 
        {
            int a;
            int c;
            int b;
            foo(a,b,c);
        }
        '''
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_Type_MisMatch_Stmt_simple(self):
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

    def test_Type_MisMatch_Stmt_simple_1(self):
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
    
    def test_Type_MisMatch_Stmt_simple_2(self):
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

    def test_Type_MisMatch_Stmt_simple_3(self):
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

    def test_Type_MisMatch_Stmt_simple_4(self):
        input = """
            void main(){
                return;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_Type_MisMatch_Stmt_simple_5(self):
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

    def test_Type_MisMatch_Stmt_simple_6(self):
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


    def test_Type_Mismatch_in_expression_1(self):
        input = """
            int main(){
                int a[5];
                a[5] = 3;
                return 1;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_Type_Mismatch_in_expression_2(self):
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

    def test_Type_Mismatch_in_expression_3(self):
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
    def test_Type_Mismatch_in_expression_array_subcripting(self):
        "test_TypeMismatchInExpression_array_subcripting"
        input = """
        int main(){
            int a;
            float b;
            a = 1;
            b = 1.01;
            int a2[1];
            float b2[51];
            return 55.02;
        }"""
        expect = "Type Mismatch In Statement: Return(FloatLiteral(55.02))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_Type_Mismatch_in_expression_binary_more(self):
        "test_TypeMismatchInExpression_binary_more"
        input = """
        int main(){
            int a;
            a = 5;
            int b;
            b = 6;
            string c;
            c = "hello";
            a > b;
            c > a;
            return -1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>,Id(c),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_Type_Mismatch_in_expression_binary_modul(self):
        "test_TypeMismatchInExpression_binary_modul"
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            a >= b;
            a % c;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_Type_Mismatch_in_expression_binary_equal(self):
        "test_TypeMismatchInExpression_binary_equal"
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            boolean bool;
            bool = a == b;
            bool = a == c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_Type_Mismatch_in_expression_block(self):
        "test_typemismatch_block"
        input = """
        int main(){
            int d[5];
            d = 5;
        } """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(d),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_Type_Mismatch_in_expression_binary_less(self):
        "test_TypeMismatchInExpression_binary_less"
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "thang";
            boolean bool;
            bool = a <= b;
            bool = a <= c;
            bool = a >= s;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_Type_Mismatch_in_expression_binary_addOp(self):
        "test_TypeMismatchInExpression_binary_add_add"
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "ahihi";
            a = a + b + b +a +a+ b+a;
            a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(s))"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_Type_Mismatch_in_expression_binary_addOp_sub_mul_div(self):
        "test_TypeMismatchInExpression_binary_add_sub_mul_div"
        input = """
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "ahihi";
            c = a + b*a/c + b -c*c+a +a+ b+a;
            b = a + b*a/c + b -c*c+a +a+ b+a;
            //a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(-,BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(a)),Id(c))),Id(b)),BinaryOp(*,Id(c),Id(c))),Id(a)),Id(a)),Id(b)),Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,458))
    
    def test_Type_Mismatch_in_expression_binary_operator(self):
        "test_Type_Mismatch_in_expression_binary_operator"
        input = """
        float foo(int a, float b){
            return a + b;
        }
        void main(){
            int a;
            a = 5;
            int b;
            b = 6;
            float c;
            c = 1.e-9;
            string s;
            s = "ahihi";
            c = a + b*a/c + b -c*c+a +a+ b+a;
            c = a + b*a/c + b -c*c+a +a+ b+a - foo(a, c);
            c =  foo(b, c) % a;
            //a = a + b + s;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,CallExpr(Id(foo),[Id(b),Id(c)]),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_unreachable_function(self):
        "test_unreachable_function"
        input = """
        int a;
        void foo2(){}
        int main(){
            int a;
            foo();
            return 1;}
        int foo(){return a + 1;}"""
        expect = "Unreachable Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,460))
    def test_function_not_return_userdef_func_not_return(self):
        input = """
        int main() {
            func(1, 2, 3);
            return 0;
        }
        float func(float a, float b, float c) {
            float sum;
            sum = a + b + c;
            putFloatLn(sum);
        }
        """
        expect = "Function func Not Return "
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_function_not_return_in_one_branch(self):
        input = """
        int testIQ(int IQ) {
            if (IQ > 150) {
                putString("Woww");
                return IQ;
            }
            else
                putString("Meh");
        }
        void main() {
            testIQ(100);
            return;
        }"""
        expect = "Function testIQ Not Return "
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_function_not_return_return_in_nestedblock(self):
        input = """
        int main() {
            {
                {
                    {
                        return 0; 
                    }
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_function_not_return_return_in_dowhile(self):
        input = """
        int main() {
            int a;
            do {
                a = getInt();
            }
            putInt(a + 1);
            a = a * 2;
            putIntLn(a + 1);
            a = a * a;
            {
                putFloatLn(a + 7);
                {
                    return 0;
                }
            } while true;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_function_not_return_ifstmt_return_two_branch(self):
        input = """
        int main() {
            float a;
            a = getFloat();
            {
                if (a > 5) {
                    {
                        return 0;
                    }
                }
                else {
                    return 1;
                }
            }
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_function_not_return_return_in_for(self):
        input = """
        int main() {
            do {
                int i;
                for (i = 55; i <= 180; i = i + 5) {
                    putBoolLn(JLPT(i));
                    return 0;
                }
            } while true;
        }
        boolean JLPT(int point) {
            if (point >= 90) return true;
            else return false;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_function_not_return_void_func(self):
        input = """
        void foo() {goo();}
        int main() {
            goo();
            return 0;
        }
        void goo() {foo();}"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_function_not_return_void_func_with_return(self):
        input = """
        void notReturnStmt() {
            if (7.5 < 1e2) {
                putString("(y)");
            }
        }
        int main() {
            returnStmt();
            return 0;
        }
        void returnStmt() {
            notReturnStmt();
            return;
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_function_not_return_combine_return_func(self):
        input = """
        int f1() {
            if (true) return 9;
            else return 10; 
        }
        float f2() {
            if (true) return f1();
            return 200;
        }
        int main() {
            a[0] = a[1] = 5;
            int temp;
            temp = arr(a)[0];
            putString(g2());
            return 0;
        }
        int a[2];
        int[] arr(int a[]) {
            f2();
            return a;
        }
        boolean g1() {
            return 2 * 3 < 18 * 9;
        }
        string g2() {
            if (g1()) return "Yes";
            do return "No";
            while !g1();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_break_continue_not_in_loop_break_not_in_loop(self):
        input = """
        void main() {
            break;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_function_true_as_variable(self):
        input = """
        void foo() {
        }
        void main() {
            foo;
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_LHS_arraycell(self):
        input = """
        void main(int a[]) {
            a[1] = 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_No_LHS_arraycell(self):
        input = """
        void main(int a[]) {
            2 = a[1];
        }
        """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_LHS_arraycell_Simple_manyAssign(self):
        input = """
        void main(int a[]) {
            a[0] = a[1] = a[2] = 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_Type_Mismatch_In_Expression_Boolean(self):
        input = """
        void main(boolean a[]) {
            a[0] = a[1] || a[2] < a[3];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,ArrayCell(Id(a),IntLiteral(2)),ArrayCell(Id(a),IntLiteral(3)))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_Float_coerce_Int(self):
        input = """
        void main(float a[]) {
            a[0] = a[1] + 1 - a[2] / a[3] * 4 / 5;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_No_LHS_Simple_manyAssign(self):
        input = """
        void main(float a[]) {
            a[0] = a[1] = 5 = 2;
        }
        """
        expect = "Not Left Value: IntLiteral(5)"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_No_LHS_Complex_All_manyAssign(self):
        input = """
        void main(boolean a[]) {
            a[1] = true = a[2] = false;
        }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_Unreachable_Function_Global_Variable(self):
        input = """
        void fo(){
        }
        void main(){
            int a;
        }
        int b;
        void foo(){
            b = 2;
        }
        """
        expect = "Unreachable Function: fo"
        self.assertTrue(TestChecker.test(input,expect,479))

    #Noleftvalue
    def test_No_Left_Value_Int(self):
        input = """
        void main(){
            int a;
            2 = a;
        }
        """
        expect = "Not Left Value: IntLiteral(2)"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_No_Left_Value_Float(self):
        input = """
        void main(){
            float a[4];
            26.9 = a[2];
        }
        """
        expect = "Not Left Value: FloatLiteral(26.9)"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_No_Left_Value_String(self):
        input = """
        void main(){
            string a;
            "a" = a;
        }
        """
        expect = "Not Left Value: StringLiteral(a)"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_No_Left_Value_String(self):
        input = """
        void main(){
            boolean a[3];
            true = a[1];
        }
        """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_noleftvalue_random(self):
        input = """
        void main(int a[]){
            int b;
            28.8 = b;
        }
        """
        expect = "Not Left Value: FloatLiteral(28.8)"
        self.assertTrue(TestChecker.test(input,expect,484))

    #Random Error
    def test_random_dowhilestmt(self):
        input ="""void main(){
            int a;
            int b;
            a = 1;
            b = 0;
            do {a = a + 1.0; b = b - 1;
            } while a <= 10 && b > -10 ;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_random_forstmt(self):
        input = """int main(){
            int i, a[5];
            int i, j, a[5];
            for (i = 10; i > 0; --i) {
                for (j = 0; j < i; j = j + 1) 
                    a[i] = j; a[0] = 0;
            }
            return i;
        }"""
        expect = "Redeclared Variable: i"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_ifstmt_10(self):
        input = """int main(){
            string a;
            boolean b;
            if (a == "a") b = true;
            else {
                if (a == "b") b = false;
                else {a = "c";
                }
            }
            return 1;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),StringLiteral(a))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_random_breakstmt(self):
        input = """int main(){
            float i;
            i = 0.0;
            for (i;i < 10.0;i = i + 1.0) 
                if (i == 5) break;
            return 1;
        }"""
        expect = "Type Mismatch In Statement: For(Id(i);BinaryOp(<,Id(i),FloatLiteral(10.0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),FloatLiteral(1.0)));If(BinaryOp(==,Id(i),IntLiteral(5)),Break()))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_random_continuestmt(self):
        input = """int main(){
            boolean b;
            int i, j;
            j = 10;
            for (i = 0; i < 10; i = i + 1) {
                b = i > 5; 
                if (b == true) continue;
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_random_returnstmt(self):
        input = """int main(){
            float y, i;
            y = 0;
            for (i = 0; i < 10; i = i + 1) {
                y = y + 1;
                if (y > 3) {
                    y = 0;
                    break;
                } 
            }
            return y;
        }"""
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(y),BinaryOp(+,Id(y),IntLiteral(1))),If(BinaryOp(>,Id(y),IntLiteral(3)),Block([BinaryOp(=,Id(y),IntLiteral(0)),Break()]))]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_random_funccall(self):
        input = """int[] ntt(int n[], int t[]){
            return n[t]+t[n];
        }
        int main(){
            int n[4], t[4];
            if (ntt(n[3],t[0]) != 0) return ntt(n[3],t[3]);
            return n[1];
        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(n),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_random_expression(self):
        input = """int main(){
            boolean a,b,c;
            int d;
            a = b && c || d;
            return d;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,BinaryOp(&&,Id(b),Id(c)),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_random_recursion(self):
        input = """
        int foo(int a){
            return a + foo(--a);
        }
        int main(){
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_random_recursion_false(self):
        input = """int ntt(int n, int t){
            return n+t;
        }
        int main(){
            if (ntt(3,0) != 0) return ntt(3,3);
            return ntt(3);
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(ntt),[IntLiteral(3)])"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_random_return_false(self):
        input = """int main(int args){
            int x,y,z[3];
            for(i=5;i>0;--i) x=y;
            return args;
        }"""
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_random_ifstmt_false(self):
        input = """void main(){
            int a;
            if (a == 5) a = a + 1.0;
            else a = a + 0.2;
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,Id(a),FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_forstmt_ifstmt(self):
        input = """int main(){
            int i, j, a[5];
            for (i = 10; i > 0; --i) 
                for (j = 0; j < i; j = j + 1) 
                    a[i] = j; 
            a[0] = 0;
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_breakstmt_forstmt(self):
        input = """void main(){
            int i;
            i = 0;
            string s;
            s = "";
            for (i;i < 10;i = i + 1) 
                if (i == 5) break; 
                else s = s + "t";
        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(s),StringLiteral(t))"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_returnstmt_forstmt_ifstmt(self):
        input = """int main(){
            int y, i;
            y = 0;
            for (i = 0; i < 10; i = i + 1) {
                y = y + 1;
                if (y < 3) return y; 
            }
        }"""
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_return_in_block(self):
        input ="""
            int Mee(){
                int a;
                {
                    if(a==2) return 1;
                    return "ahihi";
                }
            }
            void main(){}
            """
        expect = "Type Mismatch In Statement: Return(StringLiteral(ahihi))"
        self.assertTrue(TestChecker.test(input,expect,500))