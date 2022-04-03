from flask import Blueprint, render_template, abort ,request , url_for , redirect , jsonify
from  databaseClasses import db , MatchDetails ,Users ,PrizePoolBreakDown
from gamesPrizeAndRank import bgmiGame
# import json


import datetime
from datetime import datetime as dt , date , timedelta
 

# from functools import wraps

# from tokenVerification import token_required , initialize
from tokenVerification import token_required




games = Blueprint('games', __name__ , url_prefix='/games/')


@games.route('/matches',methods=["POST","GET"])
@token_required
def matches():
    data = request.get_json(force=True)
    # print(data,"\n \n")
    todayDate = date.today()
    timeNow = dt.now().time()
    uid = data['authDetails']['uid']
    # print(uid)

    matchDetails = MatchDetails.query.all()
    
    lis = []
    
    for i in matchDetails :
        prizePoolBreakD = i.prizePoolBreakDown
        prizePoolBreakDownId = prizePoolBreakD[0].id
        fromFunctionPrizeAndRank =  bgmiGame(prizePoolBreakDownId)
        prize =  fromFunctionPrizeAndRank[0]
        rank = fromFunctionPrizeAndRank[1]
        matchCreator  = i.creator.fbUserId

        if uid == matchCreator:
            userIsMatchCreator = True
        else : 
            userIsMatchCreator = False

        # getDetails = Users.query.filter_by(fbUserId = matchCreator).first()
        # adminOrnot = getDetails.isAdmin
        
        # if adminOrnot is 0:
        #     pass
        # else : 
        #     isMatchVerified = True

        if i.createdBy == "GamesterPro":
            isMatchVerified = True

        # matchStartTiming = i.gameTime.strftime("%X")
        matchStartTiming = str(datetime.datetime(i.gameDate.year,i.gameDate.month,i.gameDate.day,i.gameTime.hour,i.gameTime.minute).timestamp()* 1000)
        # print(com)    
        registrationClosingTimeMinus = datetime.datetime(i.gameDate.year,i.gameDate.month,i.gameDate.day,i.gameTime.hour,i.gameTime.minute) - timedelta( minutes=10, hours=0)
        print(registrationClosingTimeMinus)
        # registrationClosingTime = registrationClosingTimeMinus.time().strftime("%X")
        registrationClosingTime = str(registrationClosingTimeMinus.timestamp()* 1000)

        print(matchStartTiming , registrationClosingTime)

        # h = datetime.datetime(2021, 5, 6, hour=15, minute=50, second=44, microsecond=100)
        # print(h)

        pis = { "roomDetails":i.roomDetails,"Match Details":{"Game Id":"BGMI","Map":i.game.map,"Match Mode":i.game.matchMode ,"Match Type":i.matchType, "Perspective Mode":i.perspectiveMode,"Max Players":i.maxPlayers, "Players Joined":i.playersJoined,"Prize Per Kill":i.prizePerKill, "Useable Blue Money":i.useableBlueMoney},
                "title":i.title, "note":"This is note", "Money":{"Entry Fees":i.entryFee,
            "Prize Pool":{"Prize":prize,'Rank':rank}},"Prize Pool Breakdown":[],
            "Time":{"Match will start at":matchStartTiming, "Room joining will start at":registrationClosingTime},"Match Id":i.matchId, "isUserEnrolled":True,
              "matchCreatorsId":matchCreator,"created by": i.createdBy,"userIsMatchCreator":userIsMatchCreator,"shareMatchButtonVisible":True,"rules":i.rules, 
               "isMatchVerified":isMatchVerified,
              "matchStatus":i.matchStatus,"matchLinks":i.matchLinks,
         
       }

        lis.append(pis)
    
    # lisst = json.dumps(lis)
    # print(lisst)
   
    return jsonify(lis)
    # return "ok"

