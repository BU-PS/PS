def solution(w,h):
    import math
    gcd = math.gcd(w, h)
    
    return w * h - ((w // gcd) + (h // gcd) - 1) * gcd