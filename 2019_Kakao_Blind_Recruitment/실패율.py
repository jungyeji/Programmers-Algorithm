def solution(N, stages):
    answer = []
    now = [0]*(N+2)
    reach = [0]*(N+2)
    
    for stage in stages:
        now[stage] +=1
    
    for i in range(1, len(reach)):
        for n in range(i,len(now)):
            reach[i] += now[n]
            
    fail_rate = [0]*N
    
    for i in range(N):
        if reach[i+1]==0:
            fail_rate[i]=[i+1,0]
        else:
            if now[i+1]==0:
                fail_rate[i]=[i+1,0]
            else:
                fail_rate[i] = [i+1, now[i+1]/reach[i+1]]
    
    fail_rate.sort(key=lambda x:x[1], reverse=True)
    
    for fail in fail_rate:
        answer.append(fail[0])
    
    return answer
