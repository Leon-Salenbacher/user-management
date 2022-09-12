from DBConnector import DBConnector
dbConnector = DBConnector("localhost", "root", "", "usermanagement")



def usernameExisting(username:int):
    return{
        "status": 200,
        "result": True
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