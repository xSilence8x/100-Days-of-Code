# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

by4 = year % 4 == 0
by100 = year % 100 == 0
by400 = year % 400 == 0

# what is divisible by 400 is also divisible by 100, so that's why need to
# type "not by100" to reverse boolean value

# for example:
# for year = 2000 -> if(True or not True) and True = True and True = True -> leap year
# for year = 2100 -> if (False or not True) and True = False and True = False -> not leap year

result = "Leap year." if (by400 or not by100) and by4 else "Not leap day."
print(result)
