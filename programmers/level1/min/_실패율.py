# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#
# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
import unittest


def solution(N, stages):
    answer = {}

    for i in range(1, N + 1):
        stage_player = stages.count(i)
        success_player = sum([1 for j in stages if i <= j])
        fail_rate = stage_player / success_player if success_player else 0
        answer.update({
            i: {
                "stage": i,
                "fail_rate": fail_rate
            }
        })
    return sorted(answer, key=lambda x: answer[x]["fail_rate"], reverse=True)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._N = 5
        self._stages = [2, 1, 2, 6, 2, 4, 3, 3]
        self._result = [3, 4, 2, 1, 5]

    def test_solution(self):
        result = solution(N=self._N, stages=self._stages)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()
