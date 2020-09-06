def friends(m, n, board, delete):
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != ' ' and board[i][j]==board[i][j+1] and board[i][j:j+2] == board[i+1][j:j+2]:
                delete[i][j] = True
                delete[i][j+1] = True
                delete[i+1][j] = True
                delete[i+1][j+1] = True
            
    return delete

def delBlock(m, n, board, delete):
    count = 0
    for i in range(m):
        for j in range(n):
            if delete[i][j]==True:
                count+=1
                board[i] = board[i][:j]+' '+board[i][j+1:]
    
    rotated = []
    for i in range(n):
        tmp = ''
        for j in range(m):
            tmp += board[j][i]
        rotated.append(tmp)
        
    for i in range(n):
        for j in range(m):
            if rotated[i][j]==' ':
                rotated[i] = ' '+rotated[i][:j]+rotated[i][j+1:]
    
    rotated2 = []
    for i in range(m):
        tmp = ''
        for j in range(n):
            tmp += rotated[j][i]
        rotated2.append(tmp)
               
            
    return rotated2, count

def solution(m, n, board):
    answer = 0
    count = 1
    while count>0:
        delete_map = friends(m, n, board, [[False]*n for _ in range(m)])
        board, count = delBlock(m, n, board, delete_map)
        answer += count       
        
    return answer
