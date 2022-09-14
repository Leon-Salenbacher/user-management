import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import modules

class TestModules(unittest.TestCase):
    #passwordPolicy badcase01 
    #password to little character
    def test_passwordPolicy_badcase01(self):
        result = modules.passwordPolicy("Leon")

        expected_result = False
        self.assertEqual(result, expected_result)

    #passwordPolicy goodcase01
    def test_passwordPolicy_goodcase01(self):
        result = modules.passwordPolicy("Leon12345678")

        expected_result = True
        self.assertEqual(result, expected_result)

    #namePolicy badcase01
    #name to little character
    def test_namePolicy_badcase01(self):
        result = modules.namePolicy("Le")

        expected_result = False
        self.assertEqual(result, expected_result)

    #namePolicy goodcase01
    def test_namePolicy_goodcase01(self):
        result = modules.namePolicy("Leon")
        
        expected_result = True
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()