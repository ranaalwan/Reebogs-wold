def placement():
    put()
    
placement()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def finish():
    object_here()
    done()
    
    
while True:
    if wall_in_front():
        turn_left()
        move()
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()    
    if object_here():
        done()
    
        
    
        
        
    