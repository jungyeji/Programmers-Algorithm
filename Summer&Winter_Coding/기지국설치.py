def solution(n, stations, w):
    answer = 0
    
    split_range = []
    
    start = 0
    for station in stations:
        end = station-w-1
        split_range.append(end-start)
        start = station+w
        if start > n:
            break
    if start < n:
        split_range.append(n-start)
    
    
    length = 2*w+1
    
    for split in split_range:
        if split%length ==0 :
            answer += split//length
        else:
            answer += (split//length)+1           
            
    return answer
