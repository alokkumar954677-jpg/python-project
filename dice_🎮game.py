import random
import pyttsx3
engine =pyttsx3.init()
engine.setProperty('rate', 100) 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
player_name=input("enter player name==")
computer_win =0
you_win=0
match_draw=0
invaled=0
for i in range(5):
    print(f"Round {i+1}")
    computer= random.choice([1,2,3,4,5,6])
    you= int(input("enter🙎 your dice number(1 to 6)="))
    if(you<1 or you>6):
        print("you🙎 are invalid dice number=",you)
        invaled +=1
        continue
    # else:
    #     print()
    print("💻computer dice number=",computer)
    print("your 🙎dice number =",you)
    if(computer==you):
        match_draw +=1
        print(" match is draw 🫱🏻‍🫲🏼")
    elif(computer>you):
        computer_win +=1
        print("💻computer is winner🏆")
    else:
        you_win +=1
        print("you are winner 🏆")
    print ("\n=====final==========score========")
print("computer_winner\t\t",computer_win)
print("you are winner\t\t",you_win)
print("draw\t\t\t",match_draw)
print("ivaled dice number\t",invaled)
engine.stop()
if(computer_win>you_win):
        engine.say(" Congratulations computer are genius ")
elif(you_win>computer_win):
        engine.say(f" Congratulations {player_name} are genius ")
else:
        engine.say(f"{player_name}match is draw ")
engine.runAndWait()

        