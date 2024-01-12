'''
To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.
'''


print("The Love Calculator is calculating your score.....")
name1 = input() # What is your name?
name2 = input() # What is their name?



combined_name = (name1 + name2)
lower_name = combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f"Your score is {love_score}.")