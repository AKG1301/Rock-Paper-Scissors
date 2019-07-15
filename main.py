import time
import random
loose=("the computer wins")
win=("you win")
lives=5
win=0
draw=0
passwordlist=[]
lose=0
computerlive=5
while True:
    print("====================================")
    print("to begin fill the below information:")
    print("====================================")
    username=input("Please enter your username:")
    password=input("Please enter your password:")
    searchfile=open("account.txt","r")
    for line in searchfile:
        passwordlist.append(line.strip())
        if username and password in passwordlist:
            print("Loading...")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("access granted")
            print("==============================================================================================================")
            time.sleep(1)
            print("    ____________                    _________       _________    __________             ")
            time.sleep(1)
            print("   /            \                  /         \     /         \  /             |     /")
            time.sleep(1)
            print("   |            |                 |          |    |          | |              |    /   ")                                                  
            time.sleep(1)
            print("   | ___________/__               |          |    |          | |              |   /      ")                                             
            time.sleep(1)
            print("  /                \              |          |    |          | |              |  /         ")                                                                                                                                     
            time.sleep(1)
            print(" /                 |              |__________/    |          | |              | /                                            ")          
            time.sleep(1)
            print("|__________________/              |        \      |          | |              |/\                                          ")           
            time.sleep(1)
            print("|                  \              |         \     |          | |              |  \                                       ")             
            time.sleep(1)
            print("|                  |              |          \    |          | |              |   \                                    ")                
            time.sleep(1)
            print("|__________________/              |           \   |          | |              |    \                                 ")   
            time.sleep(1)
            print("|                  \              |            \  \__________/  \__________   |     \                              ")
            time.sleep(1)
            print("|                  |                   ________    _________    ________    _________  __________             ")                                              
            time.sleep(1)
            print("|__________________/                  /        \  /         \  /        \  |          /          \          ")                  
            time.sleep(1)
            print("|                  \                  |        |  |         |  |        |  |          |          |        ")                     
            time.sleep(1)
            print("\                  |                  |        |  |         |  |        |  |          |          |      ")                                        
            time.sleep(1)
            print(" \_________________/                  |________/  |         |  |________/  |____      |__________/")    
            time.sleep(1)
            print("                                      |           |_________|  |           |          |        \  ")
            print("                                      |           |         |  |           |          |         \  ")
            print("                                      |           |         |  |           |          |          \ ")
            print("                                      |           |         |  |           |_________ |           \ ")
            print("                                                                                                        ")
            print("                _______    ________      ______     ______    ________   _________   ________   ")
            print("               /       \  /          |  /      \   /      \  /          /         \ /        \  ")
            print("               |          |          |  |          |         |          |         | |        |")
            print("               |          |          |  |          |         |          |         | |        |")
            print("               \_______   |          |  \______    \______   |          |         | |________/")
            print("                       \  |          |         \          \  |          |         | |      \  ")
            print("                       |  |          |         |          |  |          |         | |       \  ")
            print("                       |  |          |         |          |  |          |         | |        \ ")
            print("               \_______/   \_______  |  \______/   \______/  \________  \_________/ |         \       ")
            print("==============================================================================================================")
            print("lives rules:")
            print("you start with",lives,"lives")
            print("if you win you get 1 extra lives")
            print("if you loose you loose a live")
            print("if you draw you get 0 extra lives")
            print("-----------------------------------")
            print("MAKE SURE DON'T USE CAPITALS")
            print("-----------------------------------")
            print("to see a list of rules type:rules")
            print("-----------------------------------")
            print("At any point type 'exit' to leave the game")
            print("to see lives type:lives")
            print("to see looses type:loose")
            print("to see draw type:draw")
            print("-----------------------------------")
            print("the computer has lives as well")
            print("can you beat the computer?")
            print("\nGood Luck!")
            print("------------------------------------")
            q=input("press enter to continue:")
            print("\n\n\n\n")
            while True:
                rps=input("rock,paper,scissors?")
                computer=("paper","rock","scissors")
                computer=random.choice(computer)
                
                if(computer=="rock" and rps=="paper"):
                    print("the computer chooses:",computer)
                    print("you win")
                    win+=1
                    lives+=1
                    computerlive-=1
                elif(computer=="rock" and rps=="scissors"):
                    print("the computer chooses:",computer)
                    print("you loose!")
                    lose+=1
                    lives-=1
                    computerlive+=1
                elif(computer=="paper"and rps=="rock"):
                    print("the computer chooses:",computer)
                    print("you loose!")
                    lose+=1
                    lives-=1
                    computerlive+=1
                elif(computer=="paper" and rps=="scissors"):
                    print("the computer chooses:",computer)
                    print("you win")
                    win+=1
                    lives+=1
                    computerlive-=1
                elif computer=="scissors" and rps=="rock":
                    print("the computer chooses:",computer)
                    print("you win")
                    win+=1
                    lives+=1
                    computerlive-=1
                elif computer=="scissors"and rps=="paper":
                    print("the computer chooses:",computer)
                    print("you loose!")
                    lose+=1
                    lives-=1
                    computerlive+=1
                elif computer==rps:
                    print("the computer chooses:",computer)
                    print("you draw")
                    draw+=1


                elif rps=="exit":
                    exit()
                elif rps=="rules":
                    print("*********************************")
                    print("RULES")
                    print("*********************************")
                    print("rock looses against paper")
                    print("rock beats scissors")
                    print("paper beats rock")
                    print("scissors looses against rock")
                    print("paper looses against scissors")
                    print("scissors beats paper")
                    print("*********************************")
                elif rps=="lives":
                    print("lives:",lives)
                elif rps=="drew":
                    print("draw:",draw)
                elif lives==0:
                    print("thanks for playing:")
                    print("you run out of lives")
                    print("you got",win,"correcct")
                    print("you lose",loose,"times")
                    print("you drew",draw,"times")
                    stop=input("press enter to exit:")
                    exit()
                elif computerlive==0:
                    print("thanks for playing")
                    print("you won")
                    print("you got",win,"correcct")
                    print("you lose",loose,"times")
                    print("you drew",draw,"times")
                    stop=input("press enter to exit:")
                    exit()
                elif rps=="draw":
                    print("draw:",draw)
                elif rps=="loose":
                    print("loose:",lose)
        else:
            print("your username and password is incorrect")
            time.sleep(1)
            exit()
           

