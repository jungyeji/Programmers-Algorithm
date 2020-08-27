def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        tmp = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i] !=0:
            days.append(tmp+1)
        else:
            days.append(tmp)
    print(days)    
    
    for i in range(len(days)):
        if i==0:
            max = days[i]
            answer.append(1)
            continue
        if days[i]<=max:
            answer[-1] += 1
        else:
            max = days[i]
            answer.append(1)
    
    return answer
