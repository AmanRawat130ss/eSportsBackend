from flask import request, jsonify

from functools import wraps

from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth



cred = credentials.Certificate("admin-sdk.json")
initialize = firebase_admin.initialize_app(cred)



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("chlaa yew")
        token = None
        # jwt is passed in the request header
        try:
            data = request.get_json(force=True)
        except:
            return jsonify({
                'message' : 'Data Error !!'
            }), 401 
        # print("\n \n",data,"\n \n")

        if 'token' in data:
        # try:
            if data['token']:
             id_token = data['token']

        # except:
        else:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            decoded_token = auth.verify_id_token(id_token)
         # print(decoded_token)
            uid = decoded_token['uid']
    
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(*args, **kwargs)
  
    return decorated