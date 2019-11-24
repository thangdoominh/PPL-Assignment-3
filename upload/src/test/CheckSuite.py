import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
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
		self.assertTrue(TestChecker.test(input, expect, 419))
