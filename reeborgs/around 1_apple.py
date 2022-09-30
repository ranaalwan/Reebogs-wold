move()
while not at_goal():
    if not front_is_clear():
        turn_left()
    if object_here():
        take()
    move()    


