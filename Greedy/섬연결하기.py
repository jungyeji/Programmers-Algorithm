def solution(n, costs):
    answer = 0
    connect = []
    
    costs.sort(key=lambda x:x[2])
    connect.append(costs[0][0])
    
    while len(connect) != n:
        for i in range(len(costs)):
            # 노드가 둘다 존재할 경우 다음 노드로 넘어가야함
            if (costs[i][0] in connect) and (costs[i][1] in connect):
                continue
            if (costs[i][0] in connect) or (costs[i][1] in connect):
                connect.append(costs[i][0])
                connect.append(costs[i][1])
                connect = list(set(connect))
                answer += costs[i][2]
                costs.pop(i)
                break
            
    return answer
