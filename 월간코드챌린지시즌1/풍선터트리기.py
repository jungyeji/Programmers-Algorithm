from collections import Counter

def solution(a):

    answer = len(a)

    if len(a) <= 2:
        answer = len(a)
    else:
        left_min = a[0]
        right_min = a[-1]

        d = {}

        for i in range(1, len(a)-1):
            # left
            left_idx = i
            left_min = min(left_min, a[left_idx-1])
            if left_min < a[left_idx]:
                d[a[left_idx]] = d.get(a[left_idx], 0) + 1

            # right
            right_idx = i * -1 - 1
            right_min = min(right_min, a[right_idx+1])
            if right_min < a[right_idx]:
                d[a[right_idx]] = d.get(a[right_idx], 0) + 1
        
        answer = answer - Counter(d.values())[2]
    
    return answer
