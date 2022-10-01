from flask import Flask, request 
from flask_cors import CORS, cross_origin

from userManagement.userManagemenet_main import UserManager
from userManagement.DB_modules import usernameExisting, emailExisting 
userManager =  UserManager()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#createUser
@app.route("/userManager/createUser", methods = ['POST'])
@cross_origin()
def create_user_api():
    """
        required Data:
        {
            "username": [username],
            "email": [email],
            "password": [password],
            "profilePicture": [profilePicture]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        email = str(data["email"])
        password = str(data["password"])
        profilePicture = str(data["profilePicture"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }

    res = userManager.createUser(username, email, password, profilePicture)
    return res

#changePassword
@app.route("/userManager/change/password", methods = ['POST'])
@cross_origin()
def change_password_api():
    """
        required Data:
        {
            "username": [username],
            "oldPassword": [oldPassword],
            "newPassword": [newPassword],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        oldPassword = str(data["oldPassword"])
        newPassword = str(data["newPassword"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    res = userManager.changePassword(username, oldPassword, newPassword, sessionKey)
    return res

#changeUsername
@app.route("/userManager/change/username", methods = ['POST'])
@cross_origin()
def change_username_api():
    """
        required Data:
        {
            "oldUsername": [oldUsername],
            "newUsername": [newUsername],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        oldUsername = str(data["oldUsername"])
        newUsername = str(data["newUsername"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    res = userManager.changeUsername(oldUsername, newUsername, sessionKey)
    return res

#changeEmail
@app.route("/userManager/change/email", methods = ['POST'])
@cross_origin()
def change_email_api():
    """
        required Data:
        {
            "username": [username],
            "newEmail": [newEmail],
            "password": [password],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        newEmail = str(data["newEmail"])
        password = str(data["password"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    res = userManager.changeEmail(username, newEmail, password, sessionKey)
    return res

#changeProfilePicture
@app.route("/userManager/change/profilePicture", methods = ['POST'])
@cross_origin()
def change_profilePicture_api():
    """
        required Data:
        {
            "username": [username],
            "profilePicture": [profilePicture],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        profilePicture = str(data["profilePicture"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    #funktion not implemented yet
    return{
        "status": 501,
        "error_message": "funktion not implemented yet"
    }

#get UserData_byUsername
@app.route("/userManager/get/UserData_by_username/<username>", methods = ['GET'])
@cross_origin()
def get_userData_by_username(username):
    if(not isinstance(username, str)):
        return{
            "status": 400
        }
    res = userManager.getUserData_by_username(username)
    return res

#SignIn User
@app.route("/userManager/SignIn_User", methods = ['POST'])
@cross_origin()
def signIn_user_api():
    """
        required Data:
        {
            "username": [username],
            "password": [password]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        password = str(data["password"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    res = userManager.signIn_user(username, password)
    return res

#SignOut User 
@app.route("/userManager/SignOut_User", methods = ['POST'])
@cross_origin()
def signOut_user_api():
    """
        required Data:
        {
            "username": [username],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }

    res = userManager.signOut_user(username, sessionKey)
    return res


#Update Session
#Updating "lastUpdate" in tblsigninusers
@app.route("/userManager/updateSession", methods = ['POST'])
@cross_origin()
def update_sesion_api():
    """
        required Data:
        {
            "username": [username],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    
    res = userManager.update_sessionKey_lastUpdate(sessionKey, username)    
    return res
    
#get LogginState
@app.route("/userManager/get_LogginState", methods = ['POST'])
@cross_origin()
def get_LogginState_api():
    """
        required Data:
        {
            "username": [username],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    res = userManager.get_logginState(username, sessionKey)
    return res

#get new SessionKey
@app.route("/userManager/new_sessionKey", methods = ['POST'])
@cross_origin()
def new_sessionKey_api():
    """
        required Data:
        {
            "username": [username],
            "sessionKey": [sessionKey]
        }    
    """
    try:
        data = request.get_json()
        username = str(data["username"])
        sessionKey = str(data["sessionKey"])
    except:
        return{
            "status": 400,
            "error_message": "missing Data or wrong data format"
        }
    res = userManager.get_newSessionKey(username, sessionKey)
    return res

#get Username Existing
@app.route("/userManager/existing/username/<username>", methods = ['GET'])
@cross_origin()
def existing_username_api(username):
    res = usernameExisting(username)
    if(res['status'] == 500): return {"status": 500}
    else: return res

#get email Existing
@app.route("/userManager/existing/email/<email>", methods = ['GET'])
@cross_origin()
def existing_email_api(email):
    res = emailExisting(email)
    if(res['status'] == 500): return {"status": 500}
    else: return res


#Test Funktion
@app.route("/userManager/Test", methods = ['POST'])
@cross_origin()
def Test_api():
    return userManager.get_logginState("Rolf", "420857324")    


if __name__ == '__main__':
    app.run(debug=True, port="5000", host="127.0.0.1")