amount=int(input("enter amount:"))

c500=amount//500
amount=amount%500

c200=amount//200
amount=amount%200

c100=amount//100
amount=amount%100

c50=amount//50
amount=amount%50

c20=amount//20
amount=amount%20

c10=amount//10
amount=amount%10

c5=amount//5
amount=amount%5

c2=amount//2
amount=amount%2


ans=f"""

    500*1={c500}
    200*1={c200}
    100*1={c100}
    50*1={c50}
    20*1={c20}
    10*1={c10}
    5*1={c5}
    2*1={c2}
    1*1={amount}

 """
print(ans)


