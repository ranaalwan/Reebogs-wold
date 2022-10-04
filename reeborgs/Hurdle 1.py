def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def pass_well():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if wall_in_front():
        pass_well()        
    elif not wall_in_front():
        move()
    

        
            
        
        
   

            
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
