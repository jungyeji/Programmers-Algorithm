import math

def solution(n, k):
    answer = []
    
    nums = [x for x in range(1,n+1)]
    
    while(n!=0):
        tmp = math.factorial(n-1)
        
        answer.append(nums.pop((k-1)//tmp))
        n-=1
        k = k%tmp
    
    return answer
