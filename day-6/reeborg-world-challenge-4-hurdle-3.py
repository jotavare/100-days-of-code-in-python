# define function turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define function loop
def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
     
# create a loop that can detect walls in random places and the goal
while not at_goal():
    if wall_in_front():
        wall()
    else:
        move()
