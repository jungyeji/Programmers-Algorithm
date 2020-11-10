def solution(n, money):
    memo = [[0 for _ in range(n+1)] for _ in range(len(money))]
    # memo[y][x] = memo[0]~memo[y]까지의 동전으로 x원 만드는 방법의 개수
    
    memo[0][0] = 1
    #동전의 최소값으로 만들 수 있는 값들
    for i in range(money[0], n+1, money[0]):
        memo[0][i] = 1
    
    for y in range(1, len(money)):
        for x in range(n+1):
            if x>=money[y]: #금액이 money[y]보다 클 때
                memo[y][x] = (memo[y-1][x]+memo[y][x-money[y]])%1000000007
            else:
                memo[y][x] = memo[y-1][x]
    
    return memo[-1][-1]

#n=5
#money=[1,2,5]

# [1,2]로 4원을 만드는 방법 = (1원만 사용 + 2원 사용에 (4-2)를 1원으로 만드는 방법)
#memo[2][4] = memo[1][4] + memo[2][4-2]
#memo[2][2] = memo[1][2] + memo[2][2-2]
