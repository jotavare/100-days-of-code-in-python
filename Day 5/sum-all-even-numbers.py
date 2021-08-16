# calculate the sum of all the even numbers from 1 to 100 
# only 1 print statement in your console output
# just print the final total and not every step of the calculation

# gave a variable the value of 0
total = 0

# used the for and range() functions to calculate all the even numbers
for number in range(2, 101, 2):
    total += number

# printed the output
print(f"Total: {total}")