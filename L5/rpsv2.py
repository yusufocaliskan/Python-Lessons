
import random
# Paper=10, Rock=20, Scissor=30
# (paper-rock) % 3 =1
# (rock-paper) % 3 =2

actions=["rock", "paper","scissor"]

def getRandomChoice():
    return random.randint(0,2)

def makeDecision():
    return actions[getRandomChoice()]

def getResult(me, you):

    if me == you:
        return "Draw"

    outcomes ={
        ('rock', "paper"):'You win.',
        ('rock', "scissor"):'I win.',
        ('paper', "rock"):'I win.',
        ('paper', "scissor"):'You win.',
        ('scissor', "paper"):'I win.',
        ('scissor', "rock"):'You win.',
    } 

    if me in actions and you in actions:
        return outcomes.get((me, you)) + f"\nMe: {me}, You : {you}"
    else:
        return "Wrong selection."

me = input('Ben: ') 
you = makeDecision()  

result = getResult(me, you)
print(result)







