from flask import Blueprint, render_template, abort ,request , url_for , redirect , jsonify
# from  databaseClasses import db , Users , UsersInfo
# from firebase_admin import credentials
# import firebase_admin
# from firebase_admin import auth

# from tokenVerification import token_required , initialize
from tokenVerification import token_required 


users = Blueprint('users', __name__ , url_prefix='/users/')



@users.route('/re')
@token_required
def re():
   

   
    return {"USer":"You are already registered"}


@users.route('/',methods=["POST","GET"])
@token_required
def isRegistered():

   
    return 0
    


@users.route('/newUsers')
def newUsers():
    data = request.get_json(force=True)
    print(data)
    return "All Okay"


