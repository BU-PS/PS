def solution(a:int, b:int) -> int:
    _ = [a, b]
    return sum([i for i in range(min(_), max(_))])