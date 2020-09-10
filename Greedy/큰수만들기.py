def solution(number, k):
    numbers = []
    
    for i in range(len(number)):
        while len(numbers) > 0 and numbers[-1] < number[i] and k > 0:
            numbers.pop()
            k -= 1
        if k == 0:
            numbers += list(number[i:])
            break
        numbers.append(number[i])
        
    if k>0:
        numbers = numbers[:-k]
    
    answer = ''.join(numbers)
    return answer
