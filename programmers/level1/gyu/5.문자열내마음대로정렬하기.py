def solution(strings, n):
    strings.sort()                      # 우선 차례대로 만든 다음에
    strings.sort(key=lambda x:x[n])     # 원하는 특정 기준으로 정렬
    return strings