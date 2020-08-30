from itertools import permutations

def solution(numbers):
    answer = 0
    prime_numbers = [False, False] + [True]*10000000
    for i in range(len(prime_numbers)):
        if prime_numbers[i]:
            k = i*2
            while k<= 10000000:
                prime_numbers[k] = False
                k += i
    nums = []
    for i in range(1,len(numbers)+1):
        num_tmp = permutations(numbers, i)
        for num in num_tmp:
            nums.append(int("".join(num)))
    
    nums = list(set(nums))
    
    for n in nums:
        if prime_numbers[n]:
            answer += 1
            
    return answer
