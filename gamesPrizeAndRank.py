
from databaseClasses import db

def bgmiGame(id):
    prizePool = db.engine.execute(f"select * from prize_pool_break_down where id = {id};")
    prize = []
    rank = []
    for i in prizePool:
                
                prize = list(i)
                del prize[0:2]

    for i,j in enumerate(prize):
                if j is not None:
                        rank.append(str(i+1))

                
    finalPize = []
    finalRank = []
    for i,j in enumerate(prize):
        if j is not None:           
            
                if i == 0:
                        # print("i is 0")                        
                        finalPize.append(prize[0])
                        finalRank.append(rank[0])
                        # print(finalPize,finalRank,"\n")
                       
                        continue
               
                elif j != prize[i-1]:
                        # print(f" j hai {j}, or i hai {i}yehi pe")
                        # print()
                                              
                        finalPize.append(prize[i])
                        finalRank.append(rank[i])
                        # print(finalPize,finalRank,"\n")


                elif j == prize[i-1]:
                        # print("j is equal")
                       

                        c = finalRank[-1]
                       
                        if '-' in c:
                                popper = finalRank.pop(-1)
                        
                                range = popper.replace(str(i),str(i+1))
                                
                                finalRank.append(range)
                                # print(finalPize,finalRank,"\n")
                                # print(finalRank)
                                # exit() 
                        else:
                                
                                popper = finalRank.pop(-1)
                                
                        
                                rankUpdate = popper + '-' + str(i+1)
                                finalRank.append(rankUpdate)
                                # print(finalPize,finalRank,"\n")


#     print(type(finalPize)) 
#     print(type(finalRank))
    return finalPize, finalRank      


# a = bgmiGame(2)
# p = a[0]
# r = a[1]

# print(p,r)


