# split 이후 index 값을 찾자


import unittest


def solution(array: list, commands: list) -> list:
    answer = list()

    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._array = [1, 5, 2, 6, 3, 7, 4]
        self._commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
        self._result = [5, 6, 3]

    def test_solution(self):
        result = solution(array=self._array, commands=self._commands)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()