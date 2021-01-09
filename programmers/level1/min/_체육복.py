# reversed -> lost 확인하면서 체크
# 자신이 여별을 가져왔지만 그걸 잃어버린 경우도 체크

import unittest


def solution(n: int, lost: list, reserve: list) -> int:
    losts = list(set(lost) - set(reserve))
    reserves = list(set(reserve) - set(lost))

    answer = n - len(losts)
    for re in reserves:
        if re - 1 in losts:
            del losts[losts.index(re - 1)]
            answer += 1
        elif re in losts:
            del losts[losts.index(re)]
            answer += 1
        elif re + 1 in losts:
            del losts[losts.index(re + 1)]
            answer += 1
    return answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._n = 5
        self._lost = [1, 2, 4, 5]
        self._reserve = [2, 3, 4]
        self._result = 3

    def test_solution(self):
        result = solution(n=self._n, lost=self._lost, reserve=self._reserve)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()