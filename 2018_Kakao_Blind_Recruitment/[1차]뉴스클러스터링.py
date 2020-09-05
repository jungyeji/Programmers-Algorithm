import re
from collections import Counter

def solution(str1, str2):
    
    str1, str2 = str1.lower(), str2.lower()
    if str1 == str2:
        return 65536
         
    regex = re.compile('[a-z][a-z]')
    
    set1 = []
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if regex.search(tmp):
            set1.append(tmp)
    set2 = []
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if regex.search(tmp):
            set2.append(tmp)
    if len(set1)==0 and len(set2)==0:
        return 65536
    
    count1, count2 = Counter(set1), Counter(set2)
    
    intersection = count1 & count2 
    intersection = sum(list(intersection.values()))
    
    union = count1 | count2
    union = sum(list(union.values()))
    
    return int(intersection/union*65536)
    
