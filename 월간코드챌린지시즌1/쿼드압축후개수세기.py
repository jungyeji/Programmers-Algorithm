def solution(arr):

    def func(r, c, s):
        result = [0,0]

        if s==1:
            if arr[r][c]==1:
                return [0,1]
            else:
                return [1,0]
            
        left_top = func(r, c, s//2)
        right_top = func(r, c+s//2, s//2)
        left_bottom = func(r+s//2, c, s//2)
        right_bottom = func(r+s//2, c+s//2, s//2)
        
        if left_top == right_top == left_bottom == right_bottom == [0,1]:
            return [0,1]
        elif left_top == right_top == left_bottom == right_bottom == [1,0]:
            return [1,0]
        else:
            result[0] = left_top[0]+right_top[0]+left_bottom[0]+right_bottom[0]
            result[1] = left_top[1]+right_top[1]+left_bottom[1]+right_bottom[1]
            return result
    
    answer = func(0, 0, len(arr))
    
    return answer
