def solution(n):
    snail = [[0 for _ in range(n)] for _ in range(n)]
    
    num = 1
    x, y = -1,0
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            elif i%3==2:
                x-=1
                y-=1
            
            snail[x][y]=num
            num+=1
            
    answer = []
    for i in range(n):
        for j in range(n):
            if snail[i][j] !=0:
                answer.append(snail[i][j])
    return answer
