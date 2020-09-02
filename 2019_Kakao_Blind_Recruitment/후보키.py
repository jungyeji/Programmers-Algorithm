from itertools import combinations

def solution(relation): 
    row = len(relation)
    col = len(relation[0])
    col_list = range(col)
    #조합
    combination_keys = []
    for i in range(1, col+1):
        tmp = combinations(col_list, i)
        combination_keys.extend(tmp) 
    
    #유일성
    uniqueness = []
    for comb in combination_keys:
        tuples = set()
        for r in range(row):
            tmp = ''
            for key in comb:
                tmp += relation[r][key]
            tuples.add(tmp)
        if len(tuples) == row:
            uniqueness.append(comb)
        
    #최소성
    answer = set(uniqueness)
    for i in range(len(uniqueness)):
        for j in range(i+1,len(uniqueness)):
            a = set(uniqueness[i])
            b = set(uniqueness[j])
            if a == a.intersection(b) :
                answer.discard(uniqueness[j])

    return len(answer)
