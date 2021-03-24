def solution(numbers):
    num=[str(i) for i in numbers]
    num.sort(key=lambda x:(x*4)[:4])

# 전체가 0일 경우도 고려하기
    if len(num)==num.count("0"):
        return "0"
    return "".join(num)