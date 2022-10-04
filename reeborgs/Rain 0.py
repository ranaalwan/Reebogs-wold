def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
move()
turn_right()
move()

    
def check_window():
    
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
            move()
    if at_goal():
        done()
        
    
def close_window():
    turn_right()
    build_wall()
    turn_left()

move()
turn_left()
while not at_goal():
    check_window()
    close_window()
    
    
    
    

        
            
        
        
   

            
        
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
