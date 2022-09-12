from cmath import exp
from random import expovariate
import unittest
import os, sys
from unittest import expectedFailure, result
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import DB_modules
#dev DB need to be running!

class TestDBModules(unittest.TestCase):

    #usernameExisting badcase01
    def test_usernameExisting_badcase01(self):
        result = DB_modules.usernameExisting("Peter")

        expected_result = {
            "status": 200,
            "result": False
        }
        self.assertEqual(result, expected_result)

    #usernameExisting goodcase01
    def test_usernameExisting_goodcase01(self):
        result = DB_modules.usernameExisting("Leon")

        expected_result = {
            "status": 200,
            "result": True
        }
        self.assertEqual(result, expected_result)

    #emailExisting badcase01
    def test_emailExisting_badcase01(self):
        result = DB_modules.emailExisting("peter@gmail.com")

        expected_result = {
            "status": 200,
            "result": False
        }
        self.assertEqual(result, expected_result)
        
    #emailExisting goodcase01
    def test_emailExisting_goodcase01(self):
        result = DB_modules.emailExisting("leon@salenbacher.com")

        expected_result = {
            "status": 200,
            "result": True
        }
        self.assertEqual(result, expected_result)

    #rightPassword badcase01
    def test_rightPassword_badcase01(self):
        result = DB_modules.rightPassword("Leon", "LeonP")

        expected_result = {
            "status": 200,
            "result": False
        }
        self.assertEqual(result, expected_result)

    #rightPassword goodcase01
    def test_rightPassword_goodcase01(self):
        result = DB_modules.rightPassword("Leon", "LeonPW")

        expected_result = {
            "status": 200,
            "result": True
        }
        self.assertEqual(result, expected_result)

    """ 
    SessionKey need to be created
    #rightSessionKey badcase01
    def test_rightSessionKey_badcase01(self):
        result = DB_modules.rightSessionKey("")

        expected_result = False
        self.assertEqual(result, expected_result)

    #rightSessionKey goodcase01
    def test_rightSessionKey_goodcase01(self):
        result = DB_modules.rightSessionKey("")

        expected_result = {
            "status": 200,
            "result": True
        }
        self.assertEqual(result, expected_result) 
    """

if __name__ == '__main__':
    unittest.main()