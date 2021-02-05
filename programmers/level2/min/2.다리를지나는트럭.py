import unittest


def solution(bridge_length: int, weight: int, truck_weights: list) -> int:
    answer = 0

    bridge_in_truck = [0] * bridge_length

    while True:

        if not truck_weights:
            answer += len(bridge_in_truck)
            break

        answer += 1

        bridge_in_truck.pop(0)
        bridge_in_truck_weight = sum(bridge_in_truck)

        truck_weight = truck_weights[0]

        if bridge_in_truck_weight + truck_weight <= weight:
            bridge_in_truck.append(truck_weights.pop(0))

        else:
            bridge_in_truck.append(0)

    return answer

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._bridge_length = 2
        self._weight = 10
        self._truck_weights = [7, 4, 5, 6]
        self._result = 8

    def test_solution(self):
        result = solution(bridge_length=self._bridge_length,
                          weight=self._weight,
                          truck_weights=self._truck_weights)

        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()
