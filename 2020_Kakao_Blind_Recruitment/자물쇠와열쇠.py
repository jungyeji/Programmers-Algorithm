def rotation(m,key):
    rotated_key = []
    for i in range(m):
        tmp = []
        for j in range(m):
            tmp.append(key[m-j-1][i])
        rotated_key.append(tmp)
    return rotated_key

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    key_90 = rotation(m,key)
    key_180 = rotation(m,key_90)
    key_270 = rotation(m,key_180)
    keys = [key, key_90, key_180, key_270]
    
    lock_count = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                lock_count+=1
    
    if lock_count == 0:
        return True
    
    expend_lock = [[2 for _ in range(2*m+n-2)] for _ in range(2*m+n-2)]
    for i in range(n):
        for j in range(n):
            expend_lock[m-1+i][m-1+j] = lock[i][j]
    # for i in range(m):
    #     lock[i] = [2]*(m-1)+lock[i]+[2]*(m-1)    
    # for _ in range(m-1):
    #     lock.insert(0, [2]*(n+2*m-2))
    #     lock.append([2]*(n+2*m-2))
    
    for start_x in range(n+m-1):
        for start_y in range(n+m-1):
            now_count = 0
            for i in range(start_x, start_x+m):
                for j in range(start_y, start_y+m):
                    if expend_lock[i][j]==0:
                        now_count +=1
            
            if now_count == lock_count:
                for now_key in keys:
                    new_count = now_count
                    out_flag = 0
                    for i in range(m):
                        for j in range(m):
                            if expend_lock[start_x+i][start_y+j] == 1 and now_key[i][j] == 1:
                                out_flag=1
                                break
                            elif expend_lock[start_x+i][start_y+j] == 0 and now_key[i][j] == 1:
                                new_count -=1
                        if out_flag == 1:
                            break
                    if new_count == 0:
                        answer=True
                        return answer
                    else:
                        continue     
            else:
                continue
    
    return answer
