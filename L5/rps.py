# Paper, Rock, Scissor

def getResult(me, you):

    actions=["rock", "paper","scissor"]
    if me in actions and you in actions:
        if me =='rock' and you=="paper":
            print("You win.") 

        if me =='rock' and you=="scissor":
            print("I win.") 

        if me =='paper' and you=="rock":
            print("I win.") 

        if me =='paper' and you=="scissor":
            print("You win.") 

        if me =='scissor' and you=="paper":
            print("I win.") 

        if me =='scissor' and you=="rock":
            print("You win.") 
    else:
        print("Wrong selection.") 

me = input('Ben: ') 
you = input('Sen: ') 


getResult(me, you)







