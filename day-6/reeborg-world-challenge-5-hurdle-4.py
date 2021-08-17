# define function turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define function loop
def wall():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif wall_in_front():
            turn_left()
        elif not right_is_clear():
            move()          
        elif front_is_clear() and right_is_clear():
            turn_right()
            
# print output
wall()