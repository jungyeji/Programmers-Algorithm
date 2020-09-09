def solution(name):
    answer = 0
    name = list(name)
    start = ['A']*len(name)
    
    index = 0
    while True:
        right = 1
        left = 1
        if name[index] != 'A':
            if ord(name[index])-ord('A')>13:
                answer += 26-(ord(name[index])-ord('A'))
            else:
                answer += ord(name[index])-ord('A')
            name[index] = 'A'
        
        if name == start:
            break
        else:
            for i in range(1, len(name)):
                if name[index+i] =='A':
                    right +=1
                else:
                    break
                if name[index-i] == 'A':
                    left +=1
                else:
                    break
            
            if right>left:
                answer +=left
                index -= left
            else:
                answer += right
                index += right
    
    return answer
