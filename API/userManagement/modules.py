from datetime import datetime
import random
import string

def passwordPolicy(password:str):
    PASSWORD_LENGTH = 12

    if(PASSWORD_LENGTH > len(password)):
        return False
    return True

def namePolicy(username:str):
    NAME_MIN_LENGTH = 4
    
    if(NAME_MIN_LENGTH > len(username)):
        return False
    return True

def emailPolicy(email:str):
    return True

def dateTime_sqlFormat():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def generate_sessionKey():
    sessionKey_length = 32
    sessionKey = ""
    for i in range(sessionKey_length):
        if(random.getrandbits(1) == 0):
            sessionKey += random.choice(string.ascii_letters)
        else:
            sessionKey +=  random.choice(string.digits)
    return sessionKey

if __name__ == '__main__':
    print(dateTime_sqlFormat())