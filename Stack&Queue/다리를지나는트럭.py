def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = truck_weights[::-1]
    n = len(truck_weights)
    passing = []
    passing_time = []
    passed = []
    cur_weight = 0
    while len(passed) < n :
        for i in range(len(passing_time)):
            passing_time[i] += 1
            
        if len(passing_time)>0 and passing_time[0] == bridge_length:
            cur_weight -= passing[0]
            passed.append(passing[0])
            passing.pop(0)
            passing_time.pop(0)
            
        if len(truck_weights) >0 :
            if truck_weights[-1]+cur_weight <= weight:
                truck = truck_weights[-1]
                cur_weight += truck
                passing.append(truck)
                passing_time.append(0)
                truck_weights.pop()
            else : 
                pass
            answer += 1
            
    return answer+bridge_length
