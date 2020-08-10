def solution(board, moves):
    answer=0
    b_stacks = [[0 for i in range(len(board))] for j in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            b_stacks[j][i] = board[i][j]

    for i in range(len(b_stacks)):
        b_stacks[i].reverse()
        b_stacks[i] = list(filter(lambda x:x!=0, b_stacks[i]))

    basket = []
    for move in moves:
        if len(b_stacks[move-1]) != 0:
            pick = b_stacks[move-1].pop()
            if len(basket) == 0:
                basket.append(pick)
            else:
                if basket[-1] == pick:
                    basket.pop()
                    answer +=2
                else:
                    basket.append(pick)
                
    return answer