def solution(N, number):
    answer = -1
    s = [0, {N}]
    
    if number == N:
        return 1
    
    for i in range(2,9):
        case = {int(str(N)*i)}
        
        for j in range(1, i//2+1):
            for x in s[j]:
                for y in s[i-j]:
                    case.add(x+y)
                    case.add(x-y)
                    case.add(y-x)
                    case.add(x*y)
                    if x!=0:
                        case.add(y//x)
                    if y!=0:
                        case.add(x//y)
            
        if number in case:
            return i
        s.append(case)
        
    return answer
