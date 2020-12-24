def solution(s: str) -> bool:
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    return False