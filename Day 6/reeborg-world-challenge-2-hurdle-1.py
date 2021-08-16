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

# call loop function 6 times
for step in range(6):
    loop()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
