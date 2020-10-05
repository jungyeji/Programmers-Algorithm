def solution(n, words):
    said = []
    turn = 1
    start_letter = words[0][0]
    for i in range(len(words)):
        word = words[i]
        if start_letter != word[0]:
            break
        start_letter = word[-1]
        if word in said:
            break
        if i == len(words)-1:
            return [0,0]
        
        if (i+1)%n ==0:
            turn +=1
        
        said.append(word)
        
    answer = [(i%n)+1, turn]
        
    return answer
