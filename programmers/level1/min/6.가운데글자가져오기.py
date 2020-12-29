# 짝수 홀수 판별
# 짝수면 2글자 아니면 1글자

import unittest


def solution(s: str) -> str:
    s_length = len(s)
    s_middle_index = s_length // 2

    if s_length & 1:
        return s[s_middle_index ]
    return s[s_middle_index - 1:s_middle_index + 1]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._odd_s = "abcde"
        self._even_s = "qwer"
        self._odd_result = "c"
        self._even_result = "we"

    def test_solution(self):
        result = solution(s=self._odd_s)
        self.assertEqual(self._odd_result, result)

        result = solution(s=self._even_s)
        self.assertEqual(self._even_result, result)


if __name__ == '__main__':
    unittest.main()