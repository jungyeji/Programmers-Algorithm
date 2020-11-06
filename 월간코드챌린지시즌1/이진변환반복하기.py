def change(n):
    string = ''
    q=int(n)
    while True:
        q,r = divmod(q,2)
        string+=str(r)
        if q==0:
            break    
    
    return string[::-1]

def solution(s):
    count1 = 0
    count2 = 0
    while True:
        count2 += s.count('0')
        s = s.replace('0','')
        s = change(len(s))
        count1 += 1
        if s=='1':
            break
    
    answer = [count1, count2]
    return answer
