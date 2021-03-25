"""
풀이 2 - 😁 stack 풀이
"""
def solution(number, k):
    numbers = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
    # 문자열에도 모을 수 있지만 문자열은 immutable(값이 변하지 않는)특성을 가지기에 코드 효율은 리스트(mutable)다 더 좋다
    
    # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
    # k는 줄일 수 있는지를 판단?
    for i, num in enumerate(number):
        while len(numbers) and numbers[-1] < num and k > 0: # numbers에 데이터가 있고 마지막 원소가 num 보다 작고, 줄일 수 있다면 (k>0)
            numbers.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1
        if k == 0:  # 중간에 뺄 수 있는 만큼 뺐다면, 이후에 데이터 붙이기
            numbers += list(number[i:])
            break
        numbers.append(num)

    # 반복문이 끝났는데도 불구하고 k가 0 보다 크면 리스트의 범위가 넘어간 경우이기 때문에 그 만큼 빼줘야 함.
    numbers = numbers[:-k] if k > 0 else numbers    # 뺄 수 있는 만큼 빼지 못하면, 그 만큼 뒤에서 삭제
                                                    # 예를 들어 98765에서 k=2이면, 98765가 나오고 여기서 987이 정답
    
    answer = ''.join(numbers)
    return answer




""" 
풀이 1 - 😭 10 번만 시간 초과...ㅠㅠ
참고해보니 O(n) 으로 풀어야 한다고 한다.
https://scarletbreeze.github.io/articles/2019-07/pythonKit%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4(4)%ED%83%90%EC%9A%95%EB%B2%95%ED%81%B0%EC%88%98
"""
def solution(number, k):
    answer = ''
    base_size = len(number) # 주어진 숫자들의 범위
    size = len(number) - k  # 총 구해야 하는 자릿 수
    start = 0               # 두 번째 반복문에서 시작해야하는 자리 위치
    
    for i in range(size):   # 총 size 만큼 반복 4-2="2"
        _max = '0'          # 각 단 계에서 가능한 가장 큰 수 찾기
        for j in range(start, base_size-size+i+1):  # start 부터 가능한 범위 만큼
            if _max < number[j]:
                _max = number[j]
                start = j + 1
        answer += _max          # 가장 큰 수 찾고, 가장 큰 수를 정답에 붙임

    return answer