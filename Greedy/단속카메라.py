def solution(routes):
    
    routes.sort()
    camera = routes[0][1]
    answer = 1
    for route in routes:
        
        if camera > route[1]:
            camera = route[1]
            
        if camera < route[0]:
            answer +=1
            camera = route[1]
    
    return answer
