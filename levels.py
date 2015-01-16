import database
def findlevel(data):
    level = 1
    score = int(data[2])
    level = level + (score/10)
    level = int(level)
    return level

def levelrun(level,array,currentscore):
    runs = (level*2)+1
    count = 0
    score = 0
    while count < runs:
        import random
        length = len(array)-1
        rand = random.randint(0, length)
        word = array[rand]
        print ("Word: ",word)
        answer = input("Spell: ")
        if answer == word:
            score = score + 1
            count = count + 1
            print ("Score: Correct, +1 ")
        else:
            score = score - 1
            print ("Score: Wrong, -2 ")
    score = score + int(currentscore[0])
    return score
    

