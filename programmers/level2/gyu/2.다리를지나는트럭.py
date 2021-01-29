def _sum(arr):
    arr = [ data[1] for data in arr]
    return sum(arr)

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = [[0, weight] for weight in truck_weights ]
    on_bridge = []
    
    # 종료 조건       
    while truck_weights or on_bridge:
        time += 1
        
        if on_bridge and on_bridge[0][0] >= bridge_length:
            on_bridge.pop(0)
                    
        # 다리를 건널 수 있으면         
        # truck_weights 
        if truck_weights and _sum(on_bridge) + truck_weights[0][1] <= weight:
            truck = truck_weights.pop(0)
            on_bridge.append(truck)
        
        # 지나가는 과정
        if on_bridge:
            for truck in on_bridge:
                truck[0] += 1
    
    return time

