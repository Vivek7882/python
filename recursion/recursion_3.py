# write a lambda function to calculate and return simple interest of given amount rate year 
# def getInterest(amount,rate,year):
#     interest = (amount * rate * year ) / 100
#     return interest

getinterest=lambda amount,rate,year:(amount*rate*year)/100

amount=float(input("enter amount:"))
rate=float(input("enter rate:"))
year=float(input("enter year:"))


print(getinterest(amount,rate,year))