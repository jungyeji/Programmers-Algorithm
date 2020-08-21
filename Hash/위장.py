from collections import Counter

def solution(clothes):
    lists = []
    
    for value in dict(clothes).values():
        lists.append(value)
        
    count = {}
    for i in lists:
        try: count[i]+=1
        except: count[i]=1
    
    answer = 1
    
    for value in count.values():
        answer = answer*(value+1)
        
    return answer-1
