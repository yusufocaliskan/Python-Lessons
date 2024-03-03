
import random
# Paper=0, Rock=1, Scissor=2
# (paper-rock) % 3 =1
# (rock-paper) % 3 =2

actions=["rock", "paper","scissor"]

def getRandomChoice():
    return random.randint(0,2)

def makeDecision():
    return actions[getRandomChoice()]

def game():

    while True:
        me = input('Mine : ') 

        if me in actions:
            you = makeDecision()  
            result = getResult(me, you)
            print(result)

        else:
            return "Wrong selection."



def getResult(me, you):

    if me == you:
        return "Draw, try again. 🚀"

    beats ={
        'rock':"scissor",
        'paper': "rock",
        'scissor': "paper"
    }

    if beats[me] == you:
        return f"{me} win" 
    else:
        return f"{you} win" 





game()



