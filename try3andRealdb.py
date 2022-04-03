
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import backref
from  datetime import datetime , date , time ,timedelta

app2 = Flask(__name__)

con = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='higamesterpro', password='amanrawat', server='higamesterpro.mysql.pythonanywhere-services.com', database='higamesterpro$gamesterpro')



app2.config["SQLALCHEMY_DATABASE_URI"] = con
app2.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app2.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False