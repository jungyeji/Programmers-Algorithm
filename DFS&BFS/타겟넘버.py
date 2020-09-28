answer = 0

def dfs(numbers, target, index, sum):
    global answer
    
    if index >= len(numbers):
        if sum == target:
            answer +=1
        return
    
    dfs(numbers, target, index+1, sum+numbers[index])
    dfs(numbers, target, index+1, sum-numbers[index])
    


def solution(numbers, target):
    global answer
    
    dfs(numbers, target, 0,0)
    
    return answer
