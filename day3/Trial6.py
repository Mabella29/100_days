# Love calculator
print("welcome to the love calculator")
name1 = input("What is your name? \n")
name2 = input("What is your crush's name? \n")

combined_name = name1 + name2
lower_case_name = combined_name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
#int_score = int(love_score)/ alt way

print(love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print("Your score is", love_score, " ,and you go together like coke and mentos.")

elif int(love_score) >= 40 and int(love_score) <= 50:
    print("Your score is", love_score, " ,you are alright together.")

else:
    print("Your score is", love_score)
