import random, time


def deductFromBalance(balance):
    return balance - 1


def addToBalance(balance):
    return balance + 36


def checkBet(theBet):
    winningNumber = random.randint(1, 36)
    print("---------------------------------------")
    print("The winning number is:", winningNumber)
    if winningNumber == theBet:
        return True
    else:
        return False

balance = 0
print("Welcome to Erkos Casino! Good Luck!")

name = input("Enter your name: ")
balance = int(input("Enter the amount of credits you wish to deposit: "))
print("Hi,", name, "your deposit was successful! Your new balance is", balance)

while True:
    # playOrNot = int(input("Press 1 to keep playing. Press 2 to exit the game: "))
    # if playOrNot == 2:
    #     print("Exiting program..")
    #     exit()
    if balance < 1:
        balance = int(input("Please, deposit credits to continue!: "))
    else:
        betNumber = int(input("Please, enter a number from 1 to 36: "))
        print("No more bets! The ball is spinning...")
        time.sleep(3)
        if checkBet(betNumber):
            print("Congatz you have won!")
            balance = addToBalance(balance)
            print("Your new balance is", balance) 
        else:
            print("Sorry, you lost. Try again!")
            balance = deductFromBalance(balance)
            print("Your new balance is", balance)
