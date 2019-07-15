print("====================================")
print("ROCK,PAPER,SCISSORS")
print("====================================")
print("New Account:")
print("-----------------------------------")
while True:
    username=input("Please enter new username:")
    password=input("Please enter new password:")
    correct=input("Please enter confirm password:")
    if password!=correct:
        print("your password don't match,please enter again")
        func()
    elif password==correct:
        print("Account Setup")
        text=open("account.txt","a")
        text.write("\n")
        text.write(username)
        text.write("\n")
        text.write(password)
        text.close()
        break
