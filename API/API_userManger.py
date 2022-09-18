from flask import Flask, request 
from flask_cors import CORS, cross_origin

from userManagement.userManagemenet_main import UserManager
userManager = UserManager()

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
            "status": 400
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
            "status": 400
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
            "status": 400
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
            "status": 400
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
            "status": 400
        }
    
    #funktion not implemented yet
    return{
        "status": 501
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



if __name__ == '__main__':
    app.run(debug=True)