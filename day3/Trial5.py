print("welcome to Mabella pizza deliveries")
size = input("what type of pizza do you want? S, M, L : ")
add_pepperoni = input("Do you want pepperoni? Y/N : ")
extra_cheese = input("Do you want extra cheese? Y/N : ")
bill = 0

if size == "S":
    bill += 15
    print("small pizza is $15")
    if add_pepperoni == "Y":
        bill += 2
        print("pepperoni for small pizza is $2")
    else:
        print("your final bill is $15")

    if extra_cheese == "Y":
        bill += 1
        print("extra cheese is $1")
elif size == "M":
    bill += 20
    print("medium pizza is $20")
    if add_pepperoni == "Y":
        bill += 3
        print("pepperoni for medium pizza is $3")

    else:
        print("your final bill is $20")

    if extra_cheese == "Y":
        bill += 1
        print("extra cheese is $1")
else:
    bill += 25
    print("large pizza is $25")
    if add_pepperoni == "Y":
        bill += 3
        print("pepperoni for large pizza is $3")

    if extra_cheese == "Y":
        bill += 1
        print("extra cheese is $1")

print(f"total bill is ${bill}")
