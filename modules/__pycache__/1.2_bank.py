import bank

amount=int(input("enter amount:"))


print("belence before deposite:",bank.belence)


bank.deposite(amount)
print("belence after deposite:",bank.belence)



wihhdraw=int(input("enter withdraw amount:"))
print("belence befor the wihhdraw:",bank.belence)
bank.withdraw(amount)

print("belence after withdraw:",bank.belence)