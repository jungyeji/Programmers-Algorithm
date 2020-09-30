def solution(n, results):
    answer = 0
    wins = {}
    loses = {}
    for i in range(n+1):
        wins[i]=set()
        loses[i]=set()
        
    for i in range(1,n+1):
        for result in results:
            winner, loser = result
            if winner == i:
                wins[i].add(loser)
            if loser == i:
                loses[i].add(winner)
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
    
    for i in range(1,n+1):
        if len(wins[i])+len(loses[i]) ==(n-1):
            answer+=1
    
    return answer
