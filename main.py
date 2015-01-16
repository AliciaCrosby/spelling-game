import other
import levels
import database
database.createtable()
array = other.getvocab()
username = input("Please enter your username/a new username: ")
alls = database.selectall()
taken = False
for each in alls:
    if each[1]==username:
        taken = True
        print ("Username accepted - Logged in")
if taken == False:
    database.insertnew(username)
    print ("Username accepted - New login created in")
user = database.finduserdata(username)
currentlevel = levels.findlevel(user)
print ("Level: ", currentlevel)
currentscore = database.findscore(username)
score = levels.levelrun(currentlevel,array,currentscore)
database.updatescore(username,score)
print ("Score: ", score)


