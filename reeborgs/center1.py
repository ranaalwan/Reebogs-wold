while True:
    if front_is_clear():
        move()
    if object_here():
        turn_left()
        turn_left()
        take()
        move()
        put()
        move()
        if object_here():
            object_here()
            turn_left()
            turn_left()
            take()
            move()
            done()
        if wall_in_front():
            
            turn_left()
            turn_left()
            move()
        elif wall_in_front():
            
            object_here()
            take()
            move()
    elif wall_in_front():
        
        
        turn_left()
        turn_left()
        put()
        move()
        
            
            
        
    