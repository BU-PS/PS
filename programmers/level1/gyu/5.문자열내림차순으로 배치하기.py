def solution(s):
    array = list(s)
    array.sort(reverse=True)            # 아스키코드로 따졌을때 A=65, a=97 즉 소문자가 더큼., 그래서 reverse 함.
    return "".join(array)