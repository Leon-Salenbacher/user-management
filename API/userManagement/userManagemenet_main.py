from datetime import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from userManagement.DB_modules import emailExisting, usernameExisting, rightSessionKey, rightPassword, proof_logginState_lastUpdate, renew_sessionKey
from userManagement.modules import emailPolicy, namePolicy, passwordPolicy, dateTime_sqlFormat, generate_sessionKey
from userManagement.DBConnector import DBConnector

class UserManager:
    def __init__(self):
        self.dbConnector = DBConnector("localhost", "root", "", "usermanagement")

    def get_logginState(self, username:str, sessionKey:str):
        #test right username/sessionKey
        username_rRes = usernameExisting(username)
        sessionKey_rRes = rightSessionKey(sessionKey, username)
        if(username_rRes['status'] != 200 or sessionKey_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not username_rRes['result'] or not sessionKey_rRes['result']):
            return{
                "status": 403,
                "error_message": "Username or SessionKey doesn't exist"
            } 

        #proof logginState
        res_logginState = proof_logginState_lastUpdate(username, sessionKey)
        if(res_logginState['status'] == 500):
            return {
                "status": 500
            }
        else:
            return res_logginState

    def createUser(self, username:str, email:str, password:str, profilePicture:str = "default"):
        #Test Policy
        username_pRes = namePolicy(username)
        password_pRes = passwordPolicy(password)
        email_pRes = emailPolicy(email)
        if(not username_pRes or  not password_pRes or not email_pRes): 
            return{
                "status": 400,
                "error_message": "Data doesn't fit policy"
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
                "status": 400,
                "error_message": "username or email already used"
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
                "status": 400,
                "error_message": "New password doesn't fit policy."
            }
        
        #Test LogginState
        logginState_res = self.get_logginState(username, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res

        #Test right oldPassword
        oldPassword_rRes = rightPassword(username, oldPassword)
        if(oldPassword_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(not oldPassword_rRes['result']):
            return{
                "status": 400,
                "error_message": "Old password isn't right"
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

    def passwordForgot(username:str, email:str):
        #changes password for 10 min and sends temp password per email
        return{
            "status": "404"
        }

    def changeUsername(self, oldUsername:str, newUsername:str, sessionKey:str):
        #Test Policy
        newUsername_pRes = namePolicy(newUsername)
        if(not newUsername_pRes):
            return{
                "status": 400,
                "error_message": "Username doesn't fit policy"
            }

        #Test LogginState
        logginState_res = self.get_logginState(oldUsername, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res

        #Test if newUsername already existing
        newUsername_rRes = usernameExisting(newUsername)
        if(newUsername_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(newUsername_rRes['result']):
            return{
                "status": 400,
                "error_message": "Username already existing"
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
                "status": 400,
                "error_message": "new Email doesn't fit policy"
            }
        
        #Test LogginState
        logginState_res = self.get_logginState(username, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res


        #Test right password and if newEmail already exists
        newEmail_rRes = emailExisting(newEmail)
        password_rRes = rightPassword(username, password)
        if(password_rRes['status'] != 200 or newEmail_rRes['status'] != 200):
            return{
                "status": 500
            }
        elif(newEmail_rRes['result'] or not password_rRes['result']):
            return{
                "status": 400,
                "error_message": "new Email already existing or wrong Password"
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
                "status": 400,
                "error_message": "Username not Existing"
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
                "status": 500
            }
        elif(not username_rRes['result'] or not password_rRes['result']):
            return{
                "status": 403,
                "error_message": "Wrong Password or Username"
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
            "status": 500
        }


    def signOut_user(self, username:str, sessionKey:str):
        #Test LogginState
        logginState_res = self.get_logginState(username, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res

        #delete sign in user in DB
        sql = "DELETE FROM tblsigninusers WHERE userID = (SELECT id FROM tblusers WHERE username = '" + username + "') AND sessionKey = '" + sessionKey + "';"
        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201,
            }
        return{
            "status": 500,
            "error": res_db
        }

    def update_sessionKey_lastUpdate(self, sessionKey:str, username:str):
        #Test LogginState
        logginState_res = self.get_logginState(username, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res

        #updateing datetime "lastUpdate" in db tblsigninusers
        time = dateTime_sqlFormat()
        sql = "UPDATE tblsigninusers SET lastUpdate = '" + time + "' " \
            + "WHERE sessionKey = '" + sessionKey + "' AND " \
            + "userID = (SELECT id FROM tblusers WHERE username = '" + username + "');"

        res_db = self.dbConnector.sql_manipulateData(sql)
        if(res_db['status'] == 200):
            return{
                "status": 201,
            }
        return{
            "status": 500
        }

    def get_newSessionKey(self, username:str, sessionKey:str):
        #Test LogginState
        logginState_res = self.get_logginState(username, sessionKey)
        if(logginState_res['status'] != 200):
            return logginState_res

        #renew SessionKey
        res = renew_sessionKey(username, sessionKey)
        if(res['status'] == 201):
            return res
        return{
            "status": 500
        }