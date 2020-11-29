def solution(n: int):
    setting = {
        0: "박",
        1: "수"
    }
    answer = [setting.get(i % 2) for i in range(1, n + 1)]
    return "".join(answer)