# data = [["BGMI","Erangle", "Classic","Solo"], ["lassan","piyaj"],["temter","asddsf"]]
from  datetime import *
# for i in data:
#     print(i[0])

# for i in data: ,["BGMI","Mira", "Classic","Solo"]
#     print(i, "\n")
    
#     print(i[2])
    # entry = Games(gameName = i[0],map =i[1],matchMode =i[2] , playersMode = i[3])
# ...     db.session.add(entry)
# ...     db.session.commit()


from databaseClasses import *
import datetime



rules = "Minimum level 25 required,BRDM not allowed,Teaming up with other players, is now allowed.Using any kind of Hacking, Glitches or Bugs can lead as a result of permanent or temporary BANNED in GamesterPro platform"

gName,map,mMode,pMode = "BGMI","Erangle","Classic","Solo" 
gid = gameIdGenerator(gName,map,mMode,pMode)

["Survival Based","TPP",date(2021,11,17), time(9,30) , 60 , 15, 30, 
0,1535,30,"thisIsCoupnSecond","MatchKiId2","idle","Luka Chupi Battel","this is note 2",rules,
"Gamester Pro",1,{'id':None,'password':None},1,{'Green':40,'Blue':60},{"facebbok":"facebook.com",
"youtube":"Youtube.com"}]





game = MatchDetails(matchType=i[0], perspectiveMode =i[1] ,gameDate =i[2] ,gameTime =i[3] ,maxPlayers =i[4] ,playersJoined= i[5],entryFee=i[6] ,prizePerKill= i[7] , prizePool= i[8], useableBlueMoney=i[9] ,matchCoupon = i[10],matchId = i[11],matchStatus =i[12] , title =i[13] ,note = i[14] , rules=i[15] ,createdBy =i[16] , shareMatchButtonVisible = i[17],roomDetails=i[18] , isMatchVerified = i[19], prizePoolMoney =i[20] ,matchLinks=i[21] , gameId = gid,creatorDetails =1)



game = MatchDetails(matchType=i[0] , perspectiveMode =i[1] ,gameDate =i[2] ,gameTime =i[3] ,maxPlayers =i[4] ,playersJoined= i[5],entryFee=i[6] ,prizePerKill= i[7] , prizePool= i[8], useableBlueMoney=i[9] ,matchCoupon = i[10],matchId = i[11],matchStatus =i[12] , title =i[13] ,note = i[14] , rules=i[15] ,createdBy =i[16] , shareMatchButtonVisible = i[17], isMatchVerified = True , gameId = gid,prizePoolBreakDown =i[18])


rules = [ "Minimum level 25 required", "BRDM not allowed","Teaming up with other players, is now allowed.","Using any kind of Hacking, Glitches or Bugs can lead as a result of permanent or temporary BANNED in GamesterPro platform"]
