def solution(sticker):
    answer = 0
    
    if len(sticker)==1:
        return sticker[0]
    
    memo1 = [0]*len(sticker)
    memo1[0] = sticker[0]
    memo1[1] = sticker[0]
    for i in range(2,len(sticker)-1):
        memo1[i] = max(memo1[i-1], memo1[i-2]+sticker[i])
    
    memo2 = [0]*len(sticker)
    memo2[0] = 0
    memo2[1] = sticker[1]
    for i in range(2,len(sticker)):
        memo2[i] = max(memo2[i-1], memo2[i-2]+sticker[i])
        
    answer = max(max(memo1), max(memo2))
    return answer
