def solution(dartResult):
    answer = 0
    score = [0,0,0]
    bonus = {'S':1,'D':2,'T':3}
    index = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i+1].isdigit():
                score[index]+= int(dartResult[i])*10
            else:
                score[index]+= int(dartResult[i])
                
        elif dartResult[i] in bonus.keys():
            score[index]**=bonus[dartResult[i]]
            index+=1
        elif dartResult[i] == '*':
            score[index-1] *=2
            if (index-2)>=0:
                score[index-2] *=2
        elif dartResult[i] == '#':
            score[index-1] *= -1
    
    answer = sum(score)
    
    return answer
