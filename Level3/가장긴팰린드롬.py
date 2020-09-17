def isPalindrome(s, start, end):
    diff = int((end - start + 1) / 2 - 1)
    
    for i in range(diff + 1):
        c1 = s[start + i]
        c2 = s[end - i];
        
        if c1 != c2:
            return False

    return True


def solution(s):
    
    for answer in range(len(s),0,-1):
        start = 0
        end = 0 + answer - 1
        
        while end < len(s):
            if isPalindrome(s, start, end):
                return answer;
            start += 1
            end += 1
    
    return 1
