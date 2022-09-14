from DB_modules import emailExisting, usernameExisting
from modules import emailPolicy, namePolicy, passwordPolicy
import DB_modules
from DBConnector import DBConnector

class UserManagement:
    def __init__(self):
        self.dbConnector = DBConnector("localhost", "root", "", "usermanagement")

    def createUser(self, username:str, email:str, password:str, profilePicture:str = "default"):
        #Test Policy
        username_pRes = namePolicy(username)
        password_pRes = passwordPolicy(password)
        email_pRes = emailPolicy(email)
        if(not username_pRes or  not password_pRes or not email_pRes): 
            return{
                "status": 400
            }

        #Test Availability
        username_aRes = usernameExisting(username)
        email_aRes = emailExisting(email)
        if(username_aRes['status'] != 200 or email_aRes['status'] != 200):
            return{
                "status": 500
            }
        elif(username_aRes['result'] or email_aRes['result']):
            return{
                "status": 400
            }

        #create User
        if(profilePicture == "default" or True):
            #INSERT INTO [tbl] ([column1]) VALUES (%s)
            sql = "INSERT INTO tblusers (username, email, password) " \
                + "VALUES (%s, %s, %s);"
            val = (username, email, password)
            res_db = self.dbConnector.manipulateData(sql, val)
            if(res_db['status'] != 200):
                return{
                    "status": 500
                }
            else:
                return{
                    "status": 201
                }    

    def changePassword(username:str, oldPassword:str, newPassword:str, sessionKey:str):
        return{
            "status": 200
        }

    def changeUsername(oldUsername:str, newUsername:str, sessionKey:str):
        return{
            "status": 200
        }

    def changeEmail(username:str, newEmail:str, password:str, sessionKey:str):
        return{
            "status": 200
        }


if __name__ == '__main__':
    um = UserManagement()
    res = um.createUser("Leonard1", "leonard1@gmail.com", "Leonard123451")