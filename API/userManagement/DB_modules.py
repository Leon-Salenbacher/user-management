import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from userManagement.DBConnector import DBConnector
dbConnector = DBConnector("localhost", "root", "", "usermanagement")

def usernameExisting(username:str):
    sql = "SELECT * FROM tblusers WHERE username = '" + username + "';"
    res = dbConnector.is_Existing(sql)

    if(res['status'] == 200):
        if(res['result'] == True): 
            return{
                "status": 200,
                "result": True
            }
        else:
            return{
                "status": 200,
                "result": False
            }
    else:
        return{
            "status": 500,
            "error": res['error']
        }

def emailExisting(email:str):
    sql = "SELECT * FROM tblusers WHERE email= '" + email + "';"
    res = dbConnector.is_Existing(sql)

    if(res['status'] == 200):
        if(res['result'] == True):
            return{
                "status": 200,
                "result": True
            }
        else: 
            return{
                "status": 200,
                "result": False
            }
    else:
        return{
            "status": 500,
            "error": res['error']
        }

def rightPassword(username:str, password:str):
    sql = "SELECT * FROM tblusers WHERE username = '" + username + "' AND password = '" + password + "';"
    res = dbConnector.is_Existing(sql)

    if(res['status'] == 200):
        if(res['result'] == True):
            return{
                "status": 200,
                "result": True
            }
        else: 
            return{
                "status": 200,
                "result": False
            }
    else:
        return{
            "status": 500,
            "error": res['error']
        }

def rightSessionKey(sessionKey:str, username:str):
    sql = "SELECT * FROM tblsigninusers WHERE sessionKey = '" + sessionKey + "' " \
        + "AND userID = (SELECT id FROM tblusers WHERE username = '" + username + "');"

    res = dbConnector.is_Existing(sql)
    if(res['status'] == 200):
        if(res['result'] == True):
            return{
                "status": 200,
                "result": True
            }
        else: 
            return{
                "status": 200,
                "result": False
            }
    else:
        return{
            "status": 500,
            "error": res['error']
        }

if __name__ == '__main__':
    print("checking usernameExisting: ")
    res_name1 = usernameExisting("Leon")
    res_name2 = usernameExisting("Peter")
    print("Expecting: True, Result: " + str(res_name1['result']))
    print("Expecting: False, Result: " + str(res_name2['result']))

    print("\nchecking emailExisting: ")
    res_email1 = emailExisting("leon@salenbacher.com")
    res_email2 = emailExisting("peter@gmail.com")
    print("Expecting: True, Result: " + str(res_email1['result']))
    print("Expecting: False, Result: " + str(res_email1['result']))

    print("\nchecking rightPassword: ")
    res_password1 = rightPassword("Leon", "LeonPW")
    res_password2 = rightPassword("Leon", "LeonP2")
    print("Expecting: True, Result: " + str(res_password1['result']))
    print("Expecting: False, Result: " + str(res_password2['result']))
    
    print("\nchecking rightSessionKey")
    res_sessionKey1 = rightSessionKey("839247090242", "Leon")
    res_sessionKey2 = rightSessionKey("9832479832", "Leon")
    print("Expecting: True, Result: " + str(res_sessionKey1['result']))
    print("Expecting: False, Result: " + str(res_sessionKey2['result']))