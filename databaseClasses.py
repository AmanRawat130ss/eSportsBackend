from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from  datetime import datetime , date , time ,timedelta

app2 = Flask(__name__)
con = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='', server='localhost', database='gamesterpro')
app2.config["SQLALCHEMY_DATABASE_URI"] = con
db = SQLAlchemy(app2)

# db = SQLAlchemy()
data = [["BGMI","Erangle", "Classic","Solo"],["BGMI","Erangle", "Classic","Duo"],["BGMI","Erangle", "Classic","Squad"],
["BGMI","Miramar", "Classic","Solo"],["BGMI","Miramar", "Classic","Duo"],["BGMI","Miramar", "Classic","Squad"],
["BGMI","Sanok", "Classic","Solo"],["BGMI","Sanok", "Classic","Duo"],["BGMI","Sanok", "Classic","Squad"],
["BGMI","Karakin", "Classic","Solo"],["BGMI","Karakin", "Classic","Duo"],["BGMI","Karakin", "Classic","Squad"],
["BGMI","Vikendi", "Classic","Solo"],["BGMI","Vikendi", "Classic","Duo"],["BGMI","Vikendi", "Classic","Squad"],
["BGMI","Random", "Quick Match","Solo"],["BGMI","Random", "Quick Match","Duo"],["BGMI","Random", "Quick Match","Squad"],
["BGMI","Random", "Death Match","Squad"]
]
rules = [ "Minimum level 25 required", "BRDM not allowed","Teaming up with other players, is now allowed.","Using any kind of Hacking, Glitches or Bugs can lead as a result of permanent or temporary BANNED in GamesterPro platform"]

gd = [
#     ["Kill Based","TPP",date(2021,11,17), time(9) , 95 , 28, 25, 
# 7,1200,40 ,30,"thisIsCoupnFirst","MatchKiId1","idle","Bhuka Battel","this is note",rules,
# "Gamester Pro",1,{'id':None,'password':None},1,{'Green':70},{"facebbok":"facebook.com",
# "youtube":"Youtube.com"} ],
["Kill Based","TPP",date(2021,11,17), time(9) , 95 , 28, 25, 
7,1200,40,"thisIsCoupnSecond","MatchKiId1","idle","Bhuka Battel","this is note 1",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':40,'Blue':60},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Survival Based","TPP",date(2021,11,17), time(9,30) , 60 , 15, 30, 
0,1535,30,"thisIsCoupnSecond","MatchKiId2","idle","Luka Chupi Battel","this is note 2",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':40,'Blue':60},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Kill Based","TPP",date(2021,11,17), time(10) , 49 , 20, 30, 
22,1226,30,"thisIsCoupnThird","MatchKiId3","idle","Livik master battel","this is note 3",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':70,'Blue':30},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Kill Based","TPP",date(2021,11,17), time(11) , 50 , 6, 30, 
25,1230,30,"thisIsCoupnFourth","MatchKiId4","idle","Do Or Die","this is note 4",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':00,'Blue':100},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Kill Based","TPP",date(2021,11,17), time(12) , 95 , 28, 25,
 15,1200,30,"thisIsCoupnFifth","MatchKiId5","idle","Bhuka Battel","this is note 5",rules,
 "Gamester Pro",1,{'id':None,'password':None},1,{'Green':50,'Blue':50},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Kill Based","TPP",date(2021,11,17), time(12,30) , 95 , 70,
 40, 25,1500,30,"thisIsCoupnSixth","MatchKiId5","Live","Chotu Battel","this is note 6",rules,
 "Gamester Pro",1,{'id':None,'password':None},1,{'Green':70,'Blue':30},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Survival Battel","TPP",date(2021,11,7), time(13,30) , 95 ,
 40, 25, 0,2000,30,"thisIsCoupnSeventh","MatchKiId5","idle","Lamba battel","this is note 7",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':10,'Blue':0},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}],

["Kill Based","TPP",date(2021,11,17), time(15) , 95 , 28, 25
,15,1300,30,"thisIsCoupnEighth","MatchKiId5","idle","Bhuka Battel","this is note 8",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':70,'Blue':30},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}]
]
# 

class Users(db.Model):
    
    id = db.Column(db.Integer(),  primary_key=True, autoincrement=True)
    fbUserId = db.Column(db.String(1000),   nullable=False , unique = True)
    gameUserId = db.Column(db.String(1000),   nullable=False)
    name =  db.Column(db.String(25),  nullable=False)
    refferCode = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(500),  nullable=True)
    phoneNumber = db.Column(db.Integer(),  nullable=True)
    photoUrl = db.Column(db.String(1000),   nullable=True)
    isBanned = db.Column(db.Boolean(), nullable = False, default = False)
    isAdmin =db.Column(db.Boolean, default=False)

    userInfo = db.relationship('UsersInfo', backref = 'user')  #backReffrence key towards UserInfo
    matchCreated = db.relationship('MatchDetails' , backref = 'creator')
    
    """userinfo is a fake column , used as users.userIfo to get all the device information from a user while a usersinfo uses usersinfo.user to get particular user for that information, it usses object for quering db  """ 

class UsersInfo(db.Model):
    
    id = db.Column(db.Integer(),  primary_key = True, autoincrement=True )
    androidId = db.Column(db.String(1000), nullable=False)
    appsInstanceId = db.Column(db.String(1000), nullable=False)
    deviceName = db.Column(db.String(1000), nullable=False)
    androidSystemVersion = db.Column(db.String(1000), nullable=False)
    deviceId = db.Column(db.String(1000), nullable=False)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id')) #foreing key towards users.id

class Games(db.Model):

    id = db.Column(db.Integer(),  primary_key = True ,autoincrement=True) # 1 2 3 
    gameName = db.Column(db.String(1000), nullable=False) # BGMI LUDO Fire Firee
    map = db.Column(db.String(1000), nullable=True) # erangle
    matchMode = db.Column(db.String(1000), nullable=False) # Classic , quick, tdm
    playersMode = db.Column(db.String(1000), nullable=False) # solo duo squad

    gameDetails = db.relationship('MatchDetails', backref = 'game')
    
    
def gameIdGenerator(gName,map,mMode,pMode):
    game = Games.query.filter_by(gameName = gName,map = map,matchMode = mMode, playersMode = pMode).first()
    return game.id


class MatchDetails(db.Model):

    id = db.Column(db.Integer(),  primary_key = True , autoincrement=True)
    matchType = db.Column(db.String(1000), nullable=True)
    perspectiveMode = db.Column(db.String(1000))
    gameDate = db.Column(db.Date, nullable=True)
    gameTime = db.Column(db.Time, nullable=True)
    maxPlayers = db.Column(db.Integer(), nullable=False)
    playersJoined = db.Column(db.Integer(), nullable=False )
    entryFee = db.Column(db.Integer(), nullable=True )
    
    
    prizePerKill = db.Column(db.Integer(), nullable=True)
    prizePool = db.Column(db.Integer(), nullable=True)
    
    useableBlueMoney = db.Column(db.Integer(), nullable = True)
    matchCoupon  = db.Column(db.String(1000), nullable = True)
    matchId  = db.Column(db.String(1000), nullable = False)
    matchStatus  = db.Column(db.String(1000), nullable = False)
 
    title = db.Column(db.String(1000), nullable = True)
    note = db.Column(db.String(1000), nullable = True)
    rules = db.Column(db.JSON(), nullable = True)
    createdBy = db.Column(db.String(1000), nullable = True)
    
    shareMatchButtonVisible = db.Column(db.Boolean, default=True)
    roomDetails = db.Column(db.JSON(), nullable = True)
    isMatchVerified = db.Column(db.Boolean, default=True)
    prizePoolMoney = db.Column(db.JSON(), nullable = True)
    matchLinks = db.Column(db.JSON(), nullable = True)

    gameId = db.Column(db.Integer(), db.ForeignKey('games.id')) # Foreign Key 
    #changebele to creator id
    creatorDetails = db.Column(db.Integer(), db.ForeignKey('users.id') , nullable = True) # Foreign Key

    prizePoolBreakDown = db.relationship('PrizePoolBreakDown', backref = 'match') # back reffrence 

class PrizePoolBreakDown(db.Model):
    
    
    id = db.Column(db.Integer(),  primary_key = True, autoincrement=True)
    MatchDetailId = db.Column(db.Integer(), db.ForeignKey('match_details.id')) # Foreign key
    rank1 = db.Column(db.Integer(), nullable = True)
    rank2 = db.Column(db.Integer(), nullable = True)
    rank3 = db.Column(db.Integer(), nullable = True)
    rank4 = db.Column(db.Integer(), nullable = True)
    rank5 = db.Column(db.Integer(), nullable = True)
    rank6 = db.Column(db.Integer(), nullable = True)
    rank7 = db.Column(db.Integer(), nullable = True)
    rank8 = db.Column(db.Integer(), nullable = True)
    rank9 = db.Column(db.Integer(), nullable = True)
    rank10 = db.Column(db.Integer(), nullable = True)
    rank11 = db.Column(db.Integer(), nullable = True)
    rank12 = db.Column(db.Integer(), nullable = True)
    rank13 = db.Column(db.Integer(), nullable = True)
    rank14 = db.Column(db.Integer(), nullable = True)
    rank15 = db.Column(db.Integer(), nullable = True)
    rank16 = db.Column(db.Integer(), nullable = True)
    rank17 = db.Column(db.Integer(), nullable = True)
    rank18 = db.Column(db.Integer(), nullable = True)
    rank19 = db.Column(db.Integer(), nullable = True)
    rank20 = db.Column(db.Integer(), nullable = True)
    rank21 = db.Column(db.Integer(), nullable = True)
    rank22 = db.Column(db.Integer(), nullable = True)
    rank23 = db.Column(db.Integer(), nullable = True)
    rank24 = db.Column(db.Integer(), nullable = True)
    rank25 = db.Column(db.Integer(), nullable = True)
    rank26 = db.Column(db.Integer(), nullable = True)
    rank27 = db.Column(db.Integer(), nullable = True)
    rank28 = db.Column(db.Integer(), nullable = True)
    rank29 = db.Column(db.Integer(), nullable = True)
    rank30 = db.Column(db.Integer(), nullable = True)
    rank31 = db.Column(db.Integer(), nullable = True)
    rank32 = db.Column(db.Integer(), nullable = True)
    rank33 = db.Column(db.Integer(), nullable = True)
    rank34 = db.Column(db.Integer(), nullable = True)
    rank35 = db.Column(db.Integer(), nullable = True)
    rank36 = db.Column(db.Integer(), nullable = True)
    rank37 = db.Column(db.Integer(), nullable = True)
    rank38 = db.Column(db.Integer(), nullable = True)
    rank39 = db.Column(db.Integer(), nullable = True)
    rank40 = db.Column(db.Integer(), nullable = True)
    rank41 = db.Column(db.Integer(), nullable = True)
    rank42 = db.Column(db.Integer(), nullable = True)
    rank43 = db.Column(db.Integer(), nullable = True)
    rank44 = db.Column(db.Integer(), nullable = True)
    rank45 = db.Column(db.Integer(), nullable = True)
    rank46 = db.Column(db.Integer(), nullable = True)
    rank47 = db.Column(db.Integer(), nullable = True)
    rank48 = db.Column(db.Integer(), nullable = True)
    rank49 = db.Column(db.Integer(), nullable = True)
    rank50 = db.Column(db.Integer(), nullable = True)
    rank51 = db.Column(db.Integer(), nullable = True)
    rank52 = db.Column(db.Integer(), nullable = True)
    rank53 = db.Column(db.Integer(), nullable = True)
    rank54 = db.Column(db.Integer(), nullable = True)
    rank55 = db.Column(db.Integer(), nullable = True)
    rank56 = db.Column(db.Integer(), nullable = True)
    rank57 = db.Column(db.Integer(), nullable = True)
    rank58 = db.Column(db.Integer(), nullable = True)
    rank59 = db.Column(db.Integer(), nullable = True)
    rank60 = db.Column(db.Integer(), nullable = True)
    rank61 = db.Column(db.Integer(), nullable = True)
    rank62 = db.Column(db.Integer(), nullable = True)
    rank63 = db.Column(db.Integer(), nullable = True)
    rank64 = db.Column(db.Integer(), nullable = True)
    rank65 = db.Column(db.Integer(), nullable = True)
    rank66 = db.Column(db.Integer(), nullable = True)
    rank67 = db.Column(db.Integer(), nullable = True)
    rank68 = db.Column(db.Integer(), nullable = True)
    rank69 = db.Column(db.Integer(), nullable = True)
    rank70 = db.Column(db.Integer(), nullable = True)
    rank71 = db.Column(db.Integer(), nullable = True)
    rank72 = db.Column(db.Integer(), nullable = True)
    rank73 = db.Column(db.Integer(), nullable = True)
    rank74 = db.Column(db.Integer(), nullable = True)
    rank75 = db.Column(db.Integer(), nullable = True)
    rank76 = db.Column(db.Integer(), nullable = True)
    rank77 = db.Column(db.Integer(), nullable = True)
    rank78 = db.Column(db.Integer(), nullable = True)
    rank79 = db.Column(db.Integer(), nullable = True)
    rank80 = db.Column(db.Integer(), nullable = True)
    rank81 = db.Column(db.Integer(), nullable = True)
    rank82 = db.Column(db.Integer(), nullable = True)
    rank83 = db.Column(db.Integer(), nullable = True)
    rank84 = db.Column(db.Integer(), nullable = True)
    rank85 = db.Column(db.Integer(), nullable = True)
    rank86 = db.Column(db.Integer(), nullable = True)
    rank87 = db.Column(db.Integer(), nullable = True)
    rank88 = db.Column(db.Integer(), nullable = True)
    rank89 = db.Column(db.Integer(), nullable = True)
    rank90 = db.Column(db.Integer(), nullable = True)
    rank91 = db.Column(db.Integer(), nullable = True)
    rank92 = db.Column(db.Integer(), nullable = True)
    rank93 = db.Column(db.Integer(), nullable = True)
    rank94 = db.Column(db.Integer(), nullable = True)
    rank95 = db.Column(db.Integer(), nullable = True)
    rank96 = db.Column(db.Integer(), nullable = True)
    rank97 = db.Column(db.Integer(), nullable = True)
    rank98 = db.Column(db.Integer(), nullable = True)
    rank99 = db.Column(db.Integer(), nullable = True)
    rank100 = db.Column(db.Integer(), nullable = True)

    
    