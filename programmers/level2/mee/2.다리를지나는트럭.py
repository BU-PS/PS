# 다리길이와 건너는시간은 같음.
# 다리의 현재 상태를 표현해야함.
# 트럭이 지나고있는동안 다리위에 무게의 합이 weight보다 작다면 다음 트럭을 넣어주고 아니라면 0을 넣어주기.
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