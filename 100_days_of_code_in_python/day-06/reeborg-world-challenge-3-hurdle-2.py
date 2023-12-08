# define function turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define function loop
def loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# created a while loop and stoped at the flag
number_of_hurdles = 6
while number_of_hurdles > 0:
    while at_goal() == True:
        done()
    loop()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    
# other way of doing it
# while not at_goal():
#     jump()