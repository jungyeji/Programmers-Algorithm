def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    def dfs(index):
        visited[index] = 1
        for j in range(n):
            if j != index:
                if computers[index][j]==1 and visited[j]==0:
                    dfs(j)
        return
        
    
    for i in range(n):
        if visited[i] == 0 :
            answer +=1
            dfs(i)
    
    return answer
