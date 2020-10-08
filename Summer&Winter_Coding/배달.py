from collections import deque

def bfs(times, N, K):
    distance = [500001]*(N+1)
    
    queue = deque()
    queue.append(1)
    distance[1] = 0
    
    while queue:
        cur = queue.popleft()
        for i in range(1, N+1):
            if times[cur][i] != 0:
                if distance[i] > distance[cur] + times[cur][i]:
                    distance[i] = distance[cur]+times[cur][i]
                    queue.append(i)
                    
    return len([i for i in distance if i<=K])
    

def solution(N, road, K):

    times = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    for a in road:
        start, end, time = a
        if times[start][end]==0:
            times[start][end] = time
            times[end][start] = time
        else:
            if time < times[start][end]:
                times[start][end] = time
                times[end][start] = time
            
    answer = bfs(times, N, K)
        
    
    return answer
