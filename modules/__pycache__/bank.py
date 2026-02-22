belence=1000

def deposite (amount):
    global belence
    if amount<0:
        print("amount can't less than 0")
    else:
        belence=belence+amount

def withdraw(amount):
    global belence
    if amount<0:
        print("amount can't less tahn 0")
    else:
        belence=belence-amount
        