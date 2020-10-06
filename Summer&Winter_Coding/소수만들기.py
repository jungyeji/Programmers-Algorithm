from itertools import combinations
import math

def Prime(num):
    if num<2:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    
    return True

def solution(nums):
    answer = 0
    
    for item in list(combinations(nums, 3)):
        if Prime(sum(item)):
            answer +=1
        else:
            continue

    
    
    return answer
