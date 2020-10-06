def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = set()
    for dir in dirs:
        dx = x
        dy = y
        
        if dir == 'U':
            if y < 5:
                dy +=1
                route = (x,y,dx,dy)
                routeb = (dx,dy,x,y)
                if route not in visited:
                    visited.add(route)
                    visited.add(routeb)
                    answer +=1
                x = dx
                y = dy
            
        elif dir == 'L':
            if x > -5:
                dx -=1
                route = (x,y,dx,dy)
                routeb = (dx,dy,x,y)
                if route not in visited:
                    visited.add(route)
                    visited.add(routeb)
                    answer +=1
                x = dx
                y = dy  
                
        elif dir == 'R':
            if x < 5:
                dx +=1
                route = (x,y,dx,dy)
                routeb = (dx,dy,x,y)
                if route not in visited:
                    visited.add(route)
                    visited.add(routeb)
                    answer +=1
                x = dx
                y = dy  
                
            
        elif dir == 'D':
            if y >-5:
                dy -=1
                route = (x,y,dx,dy)
                routeb = (dx,dy,x,y)
                if route not in visited:
                    visited.add(route)
                    visited.add(routeb)
                    answer +=1
                x = dx
                y = dy
        
    return answer
