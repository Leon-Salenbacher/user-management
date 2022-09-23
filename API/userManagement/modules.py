from datetime import datetime, timedelta
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

def get_minData_sessionKey_lastUpdate():
    #return min accapeted DateTime for sessionKey lastUpdate
    min_datetim = datetime.now() - timedelta(hours=24, minutes=0)
    return min_datetim

def generate_sessionKey():
    sessionKey_length = 32
    sessionKey = ""
    for i in range(sessionKey_length):
        if(random.getrandbits(1) == 0):
            sessionKey += random.choice(string.ascii_letters)
        else:
            sessionKey +=  random.choice(string.digits)
    return sessionKey

def convert_stringToDatetime(dateTime_str:str):
    return datetime.strptime(dateTime_str, "%Y-%m-%d %H:%M:%S")

def compare_dateTime_isMoreCurrent(d_moreCurrent:datetime, d_older:datetime):
    if(d_moreCurrent > d_older):
        return True
    else:
        return False

if __name__ == '__main__':
    res = convert_stringToDatetime("2022-09-16 22:06:02")
    print(res)
    print(type(res))

