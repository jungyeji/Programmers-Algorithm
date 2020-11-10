def move(fr, to, mid, n, answer):
    
    if n==1:
        answer.append([fr,to])
        return
    
    move(fr, mid, to, n-1, answer)
    # n-1개를 a에서 c를 거쳐 b로 이동
    answer.append([fr, to]) # n번째 원반 a에서 c로 이동
    move(mid, to, fr, n-1, answer)
    # n-1개를 b에서 a를 거쳐 c로 이동

def solution(n):
    answer = []
    move(1,3,2,n,answer)
    
    return answer
