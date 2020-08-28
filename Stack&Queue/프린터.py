from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque()
    
    for i in range(len(priorities)):
        dq.append((priorities[i], i))
        
    while len(dq) > 0:
        item = dq.popleft()
        
        if len(dq)>0 and item[0] < max(dq)[0]:
            dq.append(item)
        else:
            answer += 1
            
            if item[1] == location:
                return answer
     
    return answer
