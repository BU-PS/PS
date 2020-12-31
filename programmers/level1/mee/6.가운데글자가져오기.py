def solution(s):
    s=list(s)

    if len(s)&1:
        return s[len(s)//2]
    return s[len(s)//2-1]+s[len(s)//2]