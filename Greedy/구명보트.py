def solution(people, limit):
    answer = 0
    people.sort()
    
    i = 0
    j = n-1
    while i <= j:
        if i==j:
            answer +=1
            break
        if (people[i]+people[j])<=limit:
            answer +=1
            i+=1
            j-=1
        else:
            answer +=1
            j-=1
                
    return answer
