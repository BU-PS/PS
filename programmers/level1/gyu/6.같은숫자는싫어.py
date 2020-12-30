# 코드 2 - stack 구조 풀이
def solution(arr):
    answer = []
    
    base = arr.pop()
    answer.append(base)
    
    while arr:
        data = arr.pop()

        if base != data:            # 연속적이지 않으면 데이터 추가
            answer.append(data)
        
        base = data                 
    
    answer.reverse()
    return answer


# 코드 3 - 가장 쉬운 코드??ㅋㅋ
def solution(arr):
    answer = []
    
    base = arr[0]
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if base != arr[i]:
            answer.append(arr[i])
            base = arr[i]
    
    return answer


# 코드 1 - 효율성 테스트 실패
'''
python의 list 자료구조는 stack 구조.
자료구조는 크게 선입선출의 queue와 선입후출의 stack으로 나눌 수 있습니다. 
list는 stack 구조이므로 list[0] 을 제거하면 100번의 연산 필요 O(N^2) <- pop 을 해서 시간복잡도 에러

append()가 더 빠른 이유(pop보다 빠른 이유)
pop 은 맨뒤에서 -> 맨 앞으로 이동하는 식인데, append는 마지막 인덱스에 추가하면됨. O(1)
'''
def solution(arr):
    answer = []
    
    base = arr.pop(0)
    answer.append(base)
    
    while arr:
        data = arr.pop(0)

        if base != data:            # 연속적이지 않으면 데이터 추가
            answer.append(data)
        
        base = data                 
    
    return answer