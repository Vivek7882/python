#write a program to findout name of crickerter in string which has 20 player name using in operator.

insert=input("enter crickerter name :")

cricketers = ["Sachin Tendulkar", "Virat Kohli", "MS Dhoni", "Rohit Sharma", "Rahul Dravid", "Sourav Ganguly", "Kapil Dev", "Sunil Gavaskar", "Anil Kumble", "Jasprit Bumrah", "Hardik Pandya", "Yuvraj Singh", "Shikhar Dhawan", "Ravindra Jadeja", "KL Rahul", "Rishabh Pant", "Brett Lee", "Shane Warne", "AB de Villiers", "Chris Gayle"]

found= insert in cricketers

print(found)

foundnot=insert not in cricketers

print(foundnot)