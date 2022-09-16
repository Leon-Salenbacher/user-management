from DB_modules import emailExisting, usernameExisting, rightSessionKey, rightPassword
from modules import emailPolicy, namePolicy, passwordPolicy
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
            sql = "INSERT INTO tblusers (username, email, password, profilePicture) " \
                + "VALUES (%s, %s, %s, %s);"
            val = (username, email, password, 'default')
            res_db = self.dbConnector.manipulateData(sql, val)
            if(res_db['status'] == 200):
                return{
                    "status": 201
                }
            return{
                "status": 500
            }  

    def changePassword(self, username:str, oldPassword:str, newPassword:str, sessionKey:str):
        #Test Policy
        newPassword_pRes = passwordPolicy(newPassword)
        if(not newPassword_pRes):
            return{
                "status": 400
            }
        
        #Test right SessionKey/oldPassword
        sessionKey_rRes = rightSessionKey(sessionKey, username)
        oldPassword_rRes = rightPassword(username, oldPassword)
        if(sessionKey_rRes['status'] != 200 or oldPassword_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not sessionKey_rRes['result'] or not oldPassword_rRes['result']):
            return{
                "status": 400
            }

        #create User
        sql = "UPDATE tblusers " \
                + "SET password = '" + newPassword + "' " \
                + "WHERE id = (SELECT id FROM tblusers " \
                + "WHERE username='" + username + "'); "
        res_db = self.dbConnector.executeSQL(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201
            }        
        return{
            "status": 201
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
    userManager = UserManagement()

    print("create User: ")
    #create User Leonard1
    res_createUser = userManager.createUser(
        "Leonard1", 
        "leonard1@gmail.com", 
        "Leonard123451"
    )
    print(res_createUser)
    print("\n")

    print("changePassword: ")
    #change Password for Rolf (id=2)
    res_changePassword = userManager.changePassword(
        "Rolf", 
        "RolfPW", 
        "Rolf_new_Password", 
        "420857324"
    )
    print(res_changePassword)
    print("\n")