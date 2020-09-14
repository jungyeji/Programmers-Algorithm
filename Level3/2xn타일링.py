def solution(n):
    
    #피보나치
    first = 1
    second = 1
    for i in range(n):
        tmp = second
        second = first+second
        first = tmp
    return first%1000000007
