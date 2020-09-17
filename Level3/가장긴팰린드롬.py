def solution(s):
    
    for leng in range(len(s),0,-1):
        start =0
        while start+leng <= len(s):
            end = start+leng
            check=True
            for i in range(leng//2):
                if s[start+i] != s[end-i-1]:
                    check=False
                    break
            
            if check:
                return leng
            
            start+=1
            
    
    return 1
