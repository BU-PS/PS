def solution(s):
    if s.count("P")+s.count("p") == s.count("Y")+s.count("y"):
        return True
    else:
        return False
