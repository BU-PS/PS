import unittest


def solution(arr: list) -> list:
    value = None
    answer = list()

    for ar in arr:
        if value == ar:
            continue

        value = ar
        answer.append(ar)
    return answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._arr = [1, 1, 3, 3, 0, 1, 1]
        self._answer = [1, 3, 0, 1]

    def test_solution(self):
        answer = solution(arr=self._arr)
        self.assertEqual(self._answer, answer)


if __name__ == '__main__':
    unittest.main()