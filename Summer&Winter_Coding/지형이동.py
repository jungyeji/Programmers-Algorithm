from collections import deque, defaultdict

def bfs(land, height, check, i, j, group, n):
    q = deque()
    q.append((i,j))
    check[i][j] = group
    
    direction = [(0,-1),(0,1),(1,0),(-1,0)]
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = dx+x, dy+y
            if nx<0 or ny<0 or nx>=n or ny>=n or check[nx][ny]!=0:
                continue
            if abs(land[nx][ny]-land[x][y]) <= height:
                q.append((nx,ny))
                check[nx][ny] = group


def find_ladders(check, land, n):
    direction = [(0,-1),(0,1),(1,0),(-1,0)]
    ladders = defaultdict(lambda:10000)
    
    for i in range(n):
        for j in range(n):
            cur = check[i][j]
            for dx,dy in direction:
                nx, ny = i+dx, j+dy
                if nx<0 or ny<0 or nx>=n or ny>=n or check[nx][ny]==cur:
                    continue
                
                dist = abs(land[nx][ny]-land[i][j])
                ladders[(cur, check[nx][ny])] = min(dist, ladders[(cur, check[nx][ny])])
                
    return ladders

def find_root(x,roots):
    if x==roots[x]:
        return x
    else:
        r = find_root(roots[x], roots)
        roots[x] = r
        return r
    
def union_find(x,y,roots):
    x_root = find_root(roots[x], roots)
    y_root = find_root(roots[y], roots)
    roots[y_root] = x_root
    

def kruskal(ladders, group):
    sum = 0
    roots = {_:_ for _ in range(1,group)}
    for (x,y), value in ladders:
        #그룹의 roots가 다를 경우 병합
        if find_root(x,roots) != find_root(y,roots):
            union_find(x,y,roots)
            sum +=value
        if len(roots.items()) == 1:
             return sum
    return sum
            

def solution(land, height):
    answer = 0
    n = len(land)
    check = [[0 for _ in range(n)] for _ in range(n)]
    
    #bfs로 그룹 생성
    group = 1
    for i in range(n):
        for j in range(n):
            if check[i][j]==0:
                bfs(land, height, check, i,j, group, n)
                group+=1
    
    # 그룹 간 높이 차 계산
    ladders = find_ladders(check, land, n)
    ladders = sorted(ladders.items(), key=lambda x:x[1])
    
    #mst
    answer = kruskal(ladders, group)
    
    return answer
