import math

def solution(w,h):
    
    gcd = math.gcd(w,h)
    
    # w*h - (gcd*(w//gcd + h//gcd - 1))
    answer = w*h - (w + h - gcd)
    return answer
