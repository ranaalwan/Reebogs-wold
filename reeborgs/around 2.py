#from library import turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def go_and_check_wall():
    if(right_is_clear()):
        turn_right()       
    if(wall_in_front()):
        turn_left()
    move()
    if(not object_here()):
        go_and_check_wall()
put()
go_and_check_wall()


