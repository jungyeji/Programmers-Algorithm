def solution(n):
    
    first = 1
    second = 1
    
    for i in range(n):
        first, second = second, first+second
    
    return first %1234567
