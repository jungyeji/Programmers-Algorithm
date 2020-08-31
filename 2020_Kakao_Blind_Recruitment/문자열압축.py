def solution(s):
    answer = len(s)
    n = len(s)
    for i in range(1, n//2+1):
        comp = s[0:i]
        result = ""
        count=1
        for j in range(i,n,i):
            if s[j:j+i] == comp:
                count+=1
            else:
                if count ==1:
                    result += comp
                    comp = s[j:j+i]
                else:
                    result += str(count)+comp
                    comp = s[j:j+i]
                    count=1
        
        if count==1:
            result += comp
        else:
            result += str(count)+comp
        
        if answer > len(result):
            answer = len(result)
        
        result = ""
        
    return answer
