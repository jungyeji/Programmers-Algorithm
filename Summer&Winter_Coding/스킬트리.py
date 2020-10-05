def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        string = ""
        for s in skill_tree:
            if s in skill:
                string += s
        
        flag = True
        for i in range(len(string)):
            if string[i] != skill[i]:
                flag = False
                break
        
        if flag == True:
            answer +=1
    
    return answer
