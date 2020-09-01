def solution(record):
    answer = []
    users = {}
    logs = []
    for line in record:
        tmp = line.split()
        if tmp[0] == 'Enter':
            logs.append([tmp[1],"님이 들어왔습니다."])
            if tmp[1] in users:
                users[tmp[1]]=tmp[2]
            else:
                users[tmp[1]]=tmp[2]
                
        elif tmp[0] == 'Change':
            users[tmp[1]]=tmp[2]
        else:
            logs.append([tmp[1],"님이 나갔습니다."])
    
    for log in logs:
        answer.append(users[log[0]]+log[1])
    
    return answer
