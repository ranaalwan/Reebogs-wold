def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
            move()
            if wall_on_right():
                turn_left()
    elif right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
    
    

        
            
        
        
   

            
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
