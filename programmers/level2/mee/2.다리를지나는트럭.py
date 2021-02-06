# 다리길이와 건너는시간은 같음.
def solution(bridge_length, weight, truck_weights):
    answer = 0
    br_tr=[0 for i in range(bridge_length)]
    while br_tr:
        answer+=1 
        br_tr.pop(0) 
        if truck_weights:
            if sum(br_tr)+truck_weights[0] <= weight:
                br_tr.append(truck_weights.pop(0)) 
            else: 
                br_tr.append(0)  
    return answer