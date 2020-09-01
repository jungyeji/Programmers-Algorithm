def balance(s):
    check=0
    for i in s:
        if i == '(':
            check +=1
        elif i == ')':
            check -=1
    if check==0:
        return True
    else:
        return False
        
def correct(s):
    stack = []
    stack.append(s[0])
    
    for i in range(1,len(s)):
        if len(stack)!=0 and s[i]==')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack)==0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    
    if len(p)==0 or correct(p):
        return p
    
    u,v='',''
    
    for i in range(2,len(p)+1,2):
        if balance(p[0:i]):
            u=p[0:i]
            v=p[i:len(p)]
            break
    
    if correct(u):
        answer += u + solution(v)
    else:
        answer += '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            if u[i]=='(':
                answer += ')'
            else:
                answer += '('
                
                
    return answer
