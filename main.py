from flask import Flask, request , redirect ,url_for
# from flask_sqlalchemy import SQLAlchemy


from databaseClasses import db , Users , UsersInfo
from usersInfo import users
from games import games

# firebase cred's
# import firebase_admin
# from firebase_admin import credentials , auth
from firebase_admin import auth

from tokenVerification import token_required 

import pymysql

app = Flask(__name__)
app.register_blueprint(users, url_prefix='/users/')
app.register_blueprint(games, url_prefix='/games/')


con = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='', 
                                            server='localhost', database='gamesterpro')

app.config["SQLALCHEMY_DATABASE_URI"] = con

db.init_app(app)



# cred = credentials.Certificate("admin-sdk.json")
# firebase_admin.initialize_app(cred)


    

@app.route("/", methods=["POST"])
def hello_world():
    data = request.get_json(force=True)
    print(data)
    # entry=Users(name="rifel man")
   

    # db.session.add(entry)
    # db.session.commit()
    return {'hello':"world"}



@app.route("/login",methods=["POST"])
@token_required
def login():

    data = request.get_json(force=True)

    print("\n \n",data,"\n \n")
    id_token = data['token']

    decoded_token = auth.verify_id_token(id_token)
    print(decoded_token)
    uid = decoded_token['uid']

    print(" \n \n \n \n ", decoded_token , "\n \n " , uid)


    
    # ================================================> User details < =================================================== 

    # uid = data['authDetails']['uid']
    if (Users.query.filter_by(fbUserId = uid).first()):
        #  redirect(url_for('users.re'))
        return "alreadyUser exisit"

    
    fullName = data['userFullName']
    if not fullName:
        fullName = data['authDetails']['displayName']

    
    authDeatail = data['authDetails']
    email = authDeatail['email']
    phoneNumber = authDeatail['phoneNumber']
    photoUrl = authDeatail['photoURL']
    
# =======================================>  creating gamer id Function  <===============================================

    def createGameId():
        result = db.engine.execute("select last_insert_id();")
        for i in result:
            # print(i[0])
            creatingGameId = 'Gamester' + str(275+i[0]+1)
            return creatingGameId


    # =======================================>  creating gamer id  <===============================================

    gameUserId = createGameId()
    print(gameUserId)
    refferCode = 'gamesterpro' + str(gameUserId[8:])
    print(refferCode)


    #==========================================>  User device id  <=============================================

    androidId = data['androidId']
    appsInstanceId= data['appsInstanceId']
    deviceName = data['deviceName']
    androidSystemVersion = data['androidSystemVersion']
    deviceId = data['deviceId']


    #===============================================>  Enteries <==================================================== 

    entryUsers= Users(fbUserId = uid , gameUserId = gameUserId , name = fullName, refferCode = refferCode , email = email,
                    phoneNumber = phoneNumber, photoUrl = photoUrl  )
   
    entryUsersInfo = UsersInfo(androidId = androidId, appsInstanceId =appsInstanceId , deviceName = deviceName ,
                        androidSystemVersion = androidSystemVersion , deviceId = deviceId , user = entryUsers  )

    db.session.add(entryUsers)
    db.session.add(entryUsersInfo)

    db.session.commit()
    print("\n both entry commit m dikt")    
    return "All Okay"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

