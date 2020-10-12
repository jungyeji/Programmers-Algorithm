def solution(cookie):
    max_sum = 0
    
    for m in range(len(cookie)-1):
        l = m
        r = m+1
        l_sum = cookie[l]
        r_sum = cookie[r]
        
        while True:
            if l_sum==r_sum and max_sum < r_sum :
                max_sum=r_sum
            
            if l_sum <= r_sum and l > 0 :
                l -=1
                l_sum += cookie[l]
                
            elif l_sum >= r_sum and r < len(cookie)-1 :
                r +=1
                r_sum += cookie[r]
            else:
                break
    
    return max_sum
