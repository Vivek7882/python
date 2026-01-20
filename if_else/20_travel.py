#write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 

train_cost=int(input("enter 1th class train price:"))

distanc=float(input("enter distanc:"))
petrol_price=float(input("enter petrol price:"))
fuel_efficency=float(input("enter fuel efficency:"))

fuel_need=distanc/fuel_efficency
car_cost=fuel_efficency*petrol_price


if train_cost<car_cost:
    print("train is cheaper")
else:
    print("car is cheaper")
    