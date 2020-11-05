def solution(n):
    stack = []
    q=n
    while(True):
        q,r = divmod(q,3)
        stack.append(r)
        if q==0:
            break
    
    stack = stack[::-1]
    
    answer = stack[0]
    
    for i in range(1, len(stack)):
        if stack[i]==0:
            pass
        else:
            answer+= stack[i]*(3**i)
    
    return answer
