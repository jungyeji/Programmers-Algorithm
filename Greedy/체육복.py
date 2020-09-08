def solution(n, lost, reserve):
    lost2 = list(set(lost)-set(reserve))
    reserve2 = list(set(reserve)-set(lost))
    
    for num in reserve2:
        if (num-1) in lost2:
            lost2.remove(num-1)
        elif (num+1) in lost2:
            lost2.remove(num+1)
    
    answer = n - len(lost2)
    return answer
