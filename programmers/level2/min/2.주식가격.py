def solution(prices):
    answer = list()

    for idx, p in enumerate(prices, start=1):
        check = 0
        for _idx, _p in enumerate(prices[idx:], start=idx+1):
            if p > _p:
                check += 1
                answer.append(_idx - idx)
                break
        if check == 0:
            answer.append(len(prices[idx:]))
    return answer