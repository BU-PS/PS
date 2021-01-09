# 입력받은 수 중복 제거
# sort -> 처음부터 더하고
# 다 더한값 다시 한번 중복제거 하면 ?
# 끝?


import unittest


def solution(numbers: list) -> list:
    answer = []
    for index, number in enumerate(numbers):
        for idx, num in enumerate(numbers):
            if index == idx:
                continue
            answer.append(number + num)
    return sorted(list(set(answer)))


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._numbers = [2, 1, 3, 4, 1]
        self._result = [2,3,4,5,6,7]

    def test_solution(self):
        result = solution(numbers=self._numbers)
        self.assertEqual(self._result, result)


