import os, sys
from userManagement.modules import dateTime_sqlFormat, compare_dateTime_isMoreCurrent, get_minData_sessionKey_lastUpdate, convert_stringToDatetime, generate_sessionKey, dateTime_sqlFormat
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


def proof_logginState_lastUpdate(username:str, sessionKey:str):
    #get DateTime lastUpdate from DB
    sql_getDatetime = "SELECT lastUpdate FROM tblsigninusers " \
        + "WHERE userID = (SELECT id FROM tblusers " \
        + "WHERE username ='" + username + "') AND " \
        + "sessionKey = '" + sessionKey +  "';"
    res_getDatetime = dbConnector.executeSQL(sql_getDatetime)
    if(res_getDatetime['status'] != 200):
        return{
            "status": 500,
            "error": res_getDatetime['error']
        }
    lastUpdate_dateTime = res_getDatetime["data"][0][0] 
    #get min DateTime accapted
    min_dateTime = get_minData_sessionKey_lastUpdate()

    #compare both Datetimes
    res_compare = compare_dateTime_isMoreCurrent(lastUpdate_dateTime, min_dateTime)
    if(not res_compare):
        return{
            "status": 403
        }
    else: 
        return{
            "status": 200
        }

def renew_sessionKey(username:str, sessionKey:str):
    #sql deleting current sessionKey
    sql_deleting_sessionKey = "DELETE FROM tblsigninusers " \
        + "WHERE userID = (SELECT id FROM tblusers " \
        + "WHERE username = '" + username + "') AND " \
        + "sessionKey = '" + sessionKey + "';"
    res_deleting_sessionKey = dbConnector.sql_manipulateData(sql_deleting_sessionKey)
    if(res_deleting_sessionKey['status'] != 200):
        
        return{
            "status": 500,
            "error": res_deleting_sessionKey['error']
        }

    #get required data 
    res_getUserID = getUserID(username)   
    if(res_getUserID['status'] != 200):
        return{
            "status": 500,
            "error": res_getUserID['error']
        }
    userID = res_getUserID['userID']
    newSessionKey = generate_sessionKey()
    cur_dateTime = dateTime_sqlFormat()

    #sql creating new sessionKey
    sql_creating_sessionKey = "INSERT INTO tblsigninusers (sessionKey, userID, created, lastUpdate) VALUES (%s, %s, %s, %s);"
    val_creating_sessionKey = (newSessionKey, userID, cur_dateTime, cur_dateTime)
    res_creating_sessionKey = dbConnector.manipulateData(sql_creating_sessionKey, val_creating_sessionKey)
    if(res_creating_sessionKey['status'] != 200):
        return{
            "status": 500,
            "error": res_creating_sessionKey['error'],
        }
    return{
        "status": 201,
        "newSessionKey": newSessionKey
    }

def getUserID(username:str):
    sql = "SELECT id FROM tblusers WHERE username = '" + username + "';"
    res = dbConnector.executeSQL(sql)
    if(res['status'] != 200):
        return{
            "status": 500,
            "error": res['error']
        }
    return{
        "userID": res['data'][0][0],
        "status": 200
    } 
    


if __name__ == '__main__':
    print(renew_sessionKey("Leon", "9480275908"))
