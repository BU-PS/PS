# 2차원 배열 생성
# 데이터 넣기 (여기가 중요한듯, 예를들면 True, False 와 연산도 쉽게)
# 둘다 False = False 나머지는 True
# False 공백 아닌건 #


# 생각바뀜
# 2진수에서 논리연산자 사용해서 만들면 개꿀
# n이 필요없는거같은데

import unittest


def solution(n, arr1, arr2):
    result = [bin(ar1 | ar2) for ar1, ar2 in zip(arr1, arr2)]
    answer = [r.replace("0b", "").zfill(n) for r in result]
    final = [i.replace("1","#").replace("0", " ") for i in answer]
    return final


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._n = 5
        self._arr1 = [9, 20, 28, 18, 11]
        self._arr2 = [30, 1, 21, 17, 28]
        self._result = ["#####", "# # #", "### #", "#  ##", "#####"]

    def test_solution(self):
        result = solution(n=self._n, arr1=self._arr1, arr2=self._arr2)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()

