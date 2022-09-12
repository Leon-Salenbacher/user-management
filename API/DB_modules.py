import re
from tracemalloc import reset_peak
from unittest import result
from DBConnector import DBConnector
dbConnector = DBConnector("localhost", "root", "", "usermanagement")



def usernameExisting(username:int):
    sql = "SELECT * FROM tblusers WHERE username = '" + username + "';"
    res = dbConnector.is_Existing(sql)

    if(res['status'] == 200):
        if(res['status']): 
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
    return{
        "status": 200,
        "result": True
    }

def rightPassword(username:str, password:str):
    return{
        "status": 200,
        "result": True
    }

def rightSessionKey(sessionKey:int, username:str):
    return{
        "status": 200,
        "result": True
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
    
    #print("\nchecking rightSessionKey")
    #res_sessionKey1 = rightSessionKey("9832479832")
    #res_sessionKey2 = rightSessionKey("9832479832")
    #print("Expecting: True, Result: " + str(res_sessionKey1['result]))
    #print("Expecting: False, Result: " + str(res_sessionKey2['result]))