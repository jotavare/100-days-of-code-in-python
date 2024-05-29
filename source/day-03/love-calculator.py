# write a program that tests the compatibility between two people
# ask the user for 2 names
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# transform both names into lower case and combine
name1_lower = name1.lower()
name2_lower = name2.lower()
combined_name = name1_lower + name2_lower

# count how many letters, sum them and then combine 
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

true = t + r + u + e
love = l + o + v + e
total = int(str(true) + str(love))

# use if and elif to write a quote based on the total
if (total < 10) or (total > 90):
  print(f"Your score is {total}, you go together like coke and mentos.")
elif (total >= 40) and (total <=50):
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")