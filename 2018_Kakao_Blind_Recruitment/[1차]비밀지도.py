def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = str(bin(arr1[i]|arr2[i]))[2:]
        answer.append(("0" *(n - len(tmp)) + tmp).replace("1", "#").replace("0", " "))
    
    return answer
