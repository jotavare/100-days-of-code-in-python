# you are painting a wall
# the instructions on the paint can says that 1 can of paint can cover 5 square meters of wall
# given a random height and width of wall, calculate how many cans of paint you'll need to buy
# but because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans

# import math module
import math

# define function, calculate, round the number up with 'math.ceil'
def paint_calc(height, width, cover):
    total_can = math.ceil(height * width / cover)
    print(f"You'll need {total_can} cans of paint.")

# ask the user for input and define argument
print("How many cans of paint you'll need to buy.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

# call the function
paint_calc(height=test_h, width=test_w, cover=coverage)