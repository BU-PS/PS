def solution(w,h):
    answer=1
    for i in range(1,min(w,h)):
        if w%i==0 and h%i==0:
            gcd=i
    return w*h-(w+h-gcd)