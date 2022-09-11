def passwordPolicy(password):
    PASSWORD_LENGTH = 12

    if(PASSWORD_LENGTH > len(password)):
        return False
    return True

def namePolicy(username):
    NAME_MIN_LENGTH = 4
    
    if(NAME_MIN_LENGTH > len(username)):
        return False
    return True

def proofEmailAvailability(email):
    return True