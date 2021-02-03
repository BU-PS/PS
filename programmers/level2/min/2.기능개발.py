from math import ceil


def solution(progresses: list, speeds: list):
    answer = list()
    remain_days = list()

    for p, s in zip(progresses, speeds):
        remain_days.append(ceil((100 - p) / s))

    while remain_days:
        cnt = 0
        check = False
        first = remain_days[0]

        for day in remain_days[:]:
            if first < day:
                check = True
                answer.append(cnt)
                break

            else:
                cnt += 1
                remain_days.pop(0)

        if check is False:
            answer.append(cnt)

    return answer




solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]	)
