def solution(n, times):
    answer = 0
    left = 0
    right = max(times)*n
    
    while left<=right:
        mid = (left+right)//2
        sum = 0
        for i in times:
            sum += mid//i
            if sum >= n:
                break
        if sum < n :
            left = mid+1
        else:
            answer=mid
            right = mid-1
        
            
    return answer
