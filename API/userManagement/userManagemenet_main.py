from datetime import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from userManagement.DB_modules import emailExisting, usernameExisting, rightSessionKey, rightPassword
from userManagement.modules import emailPolicy, namePolicy, passwordPolicy, dateTime_sqlFormat, generate_sessionKey
from userManagement.DBConnector import DBConnector

class UserManager:
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
        #we always take default picture for now
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

        #change Password on DB
        sql = "UPDATE tblusers " \
                + "SET password = '" + newPassword + "' " \
                + "WHERE id = (SELECT id FROM tblusers " \
                + "WHERE username='" + username + "'); "
        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201
            }        
        return{
            "status": 500
        }

    def changeUsername(self, oldUsername:str, newUsername:str, sessionKey:str):
        #Test Policy
        newUsername_pRes = namePolicy(newUsername)
        if(not newUsername_pRes):
            return{
                "status": 400
            }

        #Test right SessionKey/oldUsername/newUsername
        sessionKey_rRes = rightSessionKey(sessionKey, oldUsername)
        oldUsername_rRes = usernameExisting(oldUsername)
        newUsername_rRes = usernameExisting(newUsername)
        if(sessionKey_rRes['status'] != 200 or oldUsername_rRes['status'] != 200 or newUsername_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not sessionKey_rRes['result'] or not oldUsername_rRes['result'] or newUsername_rRes['result']):
            return{
                "status": 400
            }

        #change Username on DB
        sql = "UPDATE tblusers " \
                + "SET username = '" + newUsername + "' " \
                + "WHERE id = (SELECT id FROM tblusers " \
                + "WHERE username='" + oldUsername + "'); "
        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201
            }
        return{
            "status": 500
        }

    def changeEmail(self, username:str, newEmail:str, password:str, sessionKey:str):
        #Test Policy
        newEmail_pRes = emailPolicy(newEmail)
        if(not newEmail_pRes):
            return{
                "status": 400
            }
        
        #Test right SessionKey/username/password/newEmail
        sessionKey_rRes = rightSessionKey(sessionKey, username)
        newEmail_rRes = emailExisting(newEmail)
        password_rRes = rightPassword(username, password)
        username_rRes = usernameExisting(username)
        if(username_rRes['status'] != 200 or
            sessionKey_rRes['status'] != 200 or 
            password_rRes['status'] != 200 or 
            newEmail_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not sessionKey_rRes['result'] or
            newEmail_rRes['result'] or
            not password_rRes['result'] or
            not username_rRes['result'] 
            ):
            return{
                "status": 400
            }

        #change Email on DB
        sql = "UPDATE tblusers " \
                + "SET email = '" + newEmail + "' " \
                + "WHERE id = (SELECT id FROM tblusers " \
                + "WHERE username='" + username + "'); "
        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201
            }
        return{
            "status": 500
        }

    def getUserData_by_username(self, username:str):
        #Test name existing
        username_rRes = usernameExisting(username)
        if(username_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not username_rRes['result']):
            return{
                "status": 400
            }
        
        #get Data
        sql = "SELECT username, email, profilePicture " \
            + "FROM tblusers WHERE username = '" + username + "';"
        res_db = self.dbConnector.executeSQL(sql)
        if(res_db['status'] == 200):
            return{
                "status": 200,
                "data": {
                    "username": res_db["data"][0][0], 
                    "email": res_db["data"][0][1],
                    "profilePicture": res_db["data"][0][2]
                }
            }
        return{
            "status": 500
        }


    def signIn_user(self, username:str, password:str):
        #test right username/password
        username_rRes = usernameExisting(username)
        password_rRes = rightPassword(username, password)
        
        if(username_rRes['status'] != 200 or password_rRes['status'] != 200):
            return{
                "here": 1,
                "status": 500
            }
        elif(not username_rRes['result'] or not password_rRes['result']):
            return{
                "status": 403
            } 
        
        #get DateTime
        dateTime = dateTime_sqlFormat()

        #create SessionKey
        sessionKey = generate_sessionKey()

        #save sessionKey in DB
        sql = "INSERT INTO tblsigninusers (sessionKey, userID, created, lastUpdate) " \
            +   "VALUES ('" + sessionKey + "', (SELECT id FROM tblusers WHERE username = '" + username + "'), '" + dateTime + "', '" + dateTime + "');"
        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201,
                "sessionKey": sessionKey
            }
        return{
            "status": 500,
            "error": res_db
        }


if __name__ == '__main__':
    userManager = UserManager()

    print("create User: ")
    #create User Leonard1
    res_createUser = userManager.createUser(
        "Leonard1", 
        "leonard1@gmail.com", 
        "Leonard123451"
    )
    print(res_createUser)
    print("\n")

    print("change Password: ")
    #change Password for Rolf (id=2)
    #Password changed to Rolf_new_Password
    res_changePassword = userManager.changePassword(
        "Rolf", 
        "RolfPW", 
        "Rolf_new_Password", 
        "420857324"
    )
    print(res_changePassword)
    print("\n")

    print("change Username: ")
    #change Username for Max (id=3)
    #username changed to = Marc
    res_changeUsername = userManager.changeUsername(
        "Max",
        "Marc",
        "824579802"
    )
    print(res_changeUsername)
    print("\n")

    print("change Email: ")
    #change Email for Leon (id=1)
    #email changed to leon@salenbacher.com
    res_changeEmail = userManager.changeEmail(
        "Leon",
        "leon@salenbacher.com",
        "LeonPW",
        "9480275908"
    )
    print(res_changeEmail)
    print("\n")

    print("SignIn User: ")
    #SignIn user Leon (id=1)
    res_signInUser = userManager.signIn_user("Leon", "LeonPW")
    print(res_signInUser)
    print("\n")