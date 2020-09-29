from collections import deque

def solution(n, edge):
    answer = 0
    adjlist = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    for e in edge:
        adjlist[e[0]].append(e[1])
        adjlist[e[1]].append(e[0])
        
    queue = deque([1])    
    visit = 1
    
    while queue:
        length = len(queue)
        for i in range(length):
            v = queue.popleft()
        
            if visited[v] == 0:
                visited[v] = visit
                for a in adjlist[v]:
                    queue.append(a)
        visit+=1
    
    max_visit = max(visited)
    
    for i in range(2,n+1):
        if visited[i] == max_visit:
            answer +=1

    
    return answer
