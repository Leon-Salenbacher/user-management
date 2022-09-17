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
        username = data["username"]
        email = data["email"]
        password = data["password"]
        profilePicture = data["profilePicture"]
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
        username = data["username"]
        oldPassword = data["oldPassword"]
        newPassword = data["newPassword"]
        sessionKey = data["sessionKey"]
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
        oldUsername = data["oldUsername"]
        newUsername = data["newUsername"]
        sessionKey = data["sessionKey"]
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
        username = data["username"]
        newEmail = data["newEmail"]
        password = data["password"]
        sessionKey = data["sessionKey"]
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
        username = data["username"]
        profilePicture = data["profilePicture"]
        sessionKey = data["sessionKey"]
    except:
        return{
            "status": 400
        }
    
    #funktion not implemented yet
    return{
        "status": 501
    }


if __name__ == '__main__':
    app.run(debug=True)