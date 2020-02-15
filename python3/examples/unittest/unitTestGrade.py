#!/bin/env python3

# Infomation on python native unittest module
# http://www.blog.pythonlibrary.org/2016/07/07/python-3-testing-an-intro-to-unittest/
# https://lukewickstead.wordpress.com/2015/06/12/unit-testing/
# Types of Python3 unit testing modules: doctest, unittest, nose2 and pytest

import unittest
import grade

class testGrade(unittest.TestCase):
    """
    testing the Grade is correct.
    """
    
    def test_grade_float_A(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(99.5)
        self.assertEqual(result, 'A')

    def test_grade_float_B(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(89.5)
        self.assertEqual(result, 'B')

        
    def test_grade_float_C(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(79.5)
        self.assertEqual(result, 'C')

        
    def test_grade_float_D(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(69.5)
        self.assertEqual(result, 'D')

    # wrong case
    """
    An example of an incorrect test case
    """
    def test_assertIsTypeInt(self):    
        #Test that the data is of type float or int
        result = grade.chkgrade('a')
        self.assertIs(type(self.result), str)

        
    def test_grade_float_F(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(59.5)
        self.assertEqual(result, 'F')

            
    def test_grade_int_A(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(99)
        self.assertEqual(result, 'A')

    def test_grade_int_B(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(89)
        self.assertEqual(result, 'B')

    def test_grade_int_C(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(79)
        self.assertEqual(result, 'C')

    def test_grade_int_D(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(69)
        self.assertEqual(result, 'D')

        
    def test_grade_int_F(self):
        """
        Test that the output of the grade is correct.
        """
        result = grade.chkgrade(59)
        self.assertEqual(result, 'F')

        
    def test_procnametype(self):
        """
        Test that the data is of type string
        """
        result = grade.procname("John Smith")
        self.assertIs(type(result), str)

        
    def test_procamounttype(self):
        """
        Test that the data is of type float or int
        """
        result = grade.procamount(120)
        self.assertIs(type(result), float)

    
if __name__ == "__main__":
    unittest.main()