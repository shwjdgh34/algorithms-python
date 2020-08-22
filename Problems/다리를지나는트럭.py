from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    timer = 0
    bridge_sum = 0

    current_truck = trucks.popleft()
    trucks.append(0)
    bridge_sum -= bridge.popleft()
    bridge.append(current_truck)
    bridge_sum += current_truck
    timer += 1

    while bridge_sum:
        bridge_sum -= bridge.popleft()
        current_truck = trucks[0]

        if weight >= bridge_sum + current_truck:
            trucks.popleft()
            trucks.append(0)
            bridge.append(current_truck)
            bridge_sum += current_truck
        else:
            bridge.append(0)
        timer += 1
    return timer


print(solution(2, 10, [7, 4, 5, 6]))
