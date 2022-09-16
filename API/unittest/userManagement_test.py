import unittest
import os, sys 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from DB_modules import emailExisting, usernameExisting, rightSessionKey, rightPassword
from DBConnector import DBConnector 

#setUp Connection to DB
dbConnector = DBConnector("localhost", "root", "", "usermanagement")

#dev DB need to be running
class TestUsersManagement(unittest.TestCase):
    #setup Test Database
    @classmethod
    def setUp(self):
        

    #create User



if __name__ == '__main__':
    unittest.main()