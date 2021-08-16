# the same code from "Hurdle 4" can be use in this one "Maze"
# theres one case where the robot will do a infinite loop - try again at day 15
# define function turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# define function loop
def wall():
    while front_is_clear():
        move()
    turn_left()
    
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
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
