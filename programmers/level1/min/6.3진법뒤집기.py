# 3진법을 어떻게 만들까
# 만든 후 뒤집기
# 다시 10진법으로 변경


import unittest


def solution(n: int) -> int:
    result = 0
    quotient = n
    answers = []

    while quotient >= 3:
        answers.append(quotient % 3)
        quotient = quotient // 3

    answers.append(quotient)
    answer = "".join(map(str, answers))

    for i, a in enumerate(answer[::-1]):
        result += int(a) * (3 ** i)
    return result


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._n = 45
        self._result = 7

    def test_solution(self):
        result = solution(n=self._n)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()