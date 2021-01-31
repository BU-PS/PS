def solution(bridge_length: int, weight: int, truck_weights: list):
    time = 0
    bridge_weights = [0 for i in range(bridge_length)]

    while truck_weights:
        bridge_weights.pop(0)

        if sum(bridge_weights) + truck_weights[0] <= weight:
            bridge_weights.append(truck_weights.pop(0))
        else:
            bridge_weights.append(0)
        time += 1

    loading = len(bridge_weights)

    return time + loading
