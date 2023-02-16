#1.	Create a global dictionary variable called credentials that contains 3 key-value pairs. 
credentials = {
   "Mateo Davalos":["mateo287", "10000"],"James Smith":["james100", "10000"],"Bob Anderson":["bob111", "10000"]}

#2. Create two variables called username and choice
username = ""
choice = ""

#3.	Create a function called ValidateCredentials
def ValidateCredentials(username,userpassword):
    if username in credentials: 
        if userpassword in credentials.get(username):
            return True
    return False

#4.	Create a function called Login
def Login():
    while True: 
        username = input("Hello user, to begin type in your username. Type quit if you'd like the quit: ")
        if (username == 'quit'):
            print("Have a nice day! Hope to see you soon.")
            exit(0)
        userpassword=input("Please type in your password to finish the login process: ")
        print(ValidateCredentials(username,userpassword))
        if (ValidateCredentials(username,userpassword)):
            return username 
        else: 
            choice=input("Would you like to continue. Type yes or no: ")
            if (choice == 'yes'):
                print("Have a nice day! Hope to see you soon.")
                exit(0)
            return ""
Login()

#Create 3 function that allow the user to know there balance, deposit, and withdrawl money
def printbalance(username):
    balance = int(credentials.get(username)[1])
    print("This is your balance as of right now:",balance)
    Mainmenu(username)
def deposit(username):
    balance = int(credentials.get(username)[1])
    deposit = int(input("How much would you like to deposit today?: "))
    balance = balance + deposit
    credentials.get(username)[1] = balance
    print("This is your new balance:",balance)
    Mainmenu(username)
def withdrawl(username):
    balance = int(credentials.get(username)[1])
    withdrawl = int(input("How much would you like to withdrawl?: "))
    #If user entered a number to high then tell them
    if withdrawl > balance:
        return print("It seems like your withdrawl was too high. Please enter a different number: ")
        return withdrawl(username)
    credentials.get(username)[1] = balance - withdrawl
    print("Your balance is now:",credentials.get(username)[1])
    Mainmenu(username)

#Ask the user to type either 1-4 to pick their action
def Mainmenu(username):
    username = input("Please type in your username for verification: ")
    while True:
        choice=input("Type 1 to Withdrawl, 2 to PrintBalance, 3 Deposit , and 4 to Quit \n")
        if (choice == '1'):
            withdrawl(username)
            return "Withdrawl"
        elif (choice == '2'):
            printbalance(username)
            return "Print Balance"
        elif (choice == '3'):
            deposit(username)
            return "Deposit"
        elif (choice == '4'):
            print("Have a nice day. Hope to see you soon :)")
            exit(0)  
Mainmenu(username)