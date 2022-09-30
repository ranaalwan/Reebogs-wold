horizontal=True
while horizontal:
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
            turn_left()
          
        if is_facing_north():
            move()
        if object_here():
            take()
            
            if wall_in_front():
                turn_left()
                move()
            if wall_in_front() and object_here():
                done()
            if front_is_clear():
                turn_left()
                move()
            if object_here():
                done()
            if wall_in_front():
                object_here()
                take()
                move()
    elif wall_in_front():
        turn_left()
        turn_left()
        put()
        move()
        
            
            
        
    