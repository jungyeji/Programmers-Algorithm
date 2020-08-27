def solution(operations):
    answer = []
    numbers = []
    for operation in operations:
        op = operation.split()
        if op[0] == "I":
            numbers.append(int(op[1]))
        elif op[0] == "D":
            if len(numbers)>0:
                if op[1] == "1":
                    numbers.remove(max(numbers))
                else:
                    numbers.remove(min(numbers))
    
    if len(numbers)==0:
        answer = [0,0]
    else:
        answer = [max(numbers),min(numbers)]
    
    return answer
