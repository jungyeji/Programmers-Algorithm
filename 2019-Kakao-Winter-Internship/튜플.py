import collections

def solution(s):
    s = s[1:-1]    
    
    numbers = []
    temp = []    
    for elem in s:
        if elem == '{':
            continue
        elif elem == '}':
            numbers.append(''.join(temp).split(','))
            temp = []
        else:
            temp.append(elem)
    
    
    for i in range(len(numbers)):
        for number in numbers[i]:
            if number == '':
                numbers[i].remove(number)

    numbers = sorted(numbers, key=len)
    
    answer = []
    for number in numbers:
        answer += number
    
    return [int(x) for x in list(collections.Counter(answer).keys())]