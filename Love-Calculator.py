# Love Calculator
print("Let's see how much is your score!")

name1 = input("Your Name: ")
name2 = input("Name of the person you want to match: ")
combined_name = name1 + name2

lower_case_name = combined_name.lower()

# Counting the letters for "TRUE"
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e1 = lower_case_name.count("e")
true = t + r + u + e1

# Counting the letters for "LOVE"
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e2 = lower_case_name.count("e")
love = l + o + v + e2

# Merging the scores of "TRUE" and "LOVE" as a string
love_score = int(str(true) + str(love))
print(f"Your Love Score is {love_score}!")

# Conditional checks based on the concatenated love score
if love_score > 90:
    print("You guys are ready to get married <3")
elif 90 >= love_score >= 75:
    print("You are a good match!")
elif 75 > love_score > 50:
    print("You still need to try harder!")
else:
    print("Sorry, you are not a match.")
