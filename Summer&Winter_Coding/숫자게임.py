def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    for a in A:
        for b in B:
            if a < b:
                answer +=1
                B.remove(b)
                break
    
    return answer
