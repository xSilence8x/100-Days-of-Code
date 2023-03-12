# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

score_true = 0
score_love = 0

# calculate how many times are letters in word true/love in both the names
for letter in "true":
    score_true += name1.count(letter)
    score_true += name2.count(letter)

for letter in "love":
    score_love += name1.count(letter)
    score_love += name2.count(letter)

score = int(str(score_true) + str(score_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

