'''
https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
custom compare sort return value 에 관한 내용
< 0 (음수) 왼쪽 항목이 오른쪽 항목 보다 먼저 정렬되어야하는 경우 음수 값을 반환합니다.
> 0 (양수) 왼쪽 항목이 오른쪽 항목 뒤에 정렬되어야하는 경우 양수 값을 반환합니다.
0   (동일) 왼쪽 및 오른쪽 항목의 무게가 같고 우선 순위없이 "동일하게"주문되어야하는 경우 반환

정리하면
return 값이 음수이면 순서 유지
return 값이 양수이면 순서 변경
reutrn 값이 0 이면 우선순위 X
'''

from functools import cmp_to_key

def cmp_sort(num1, num2):
    num1_2 = num1 + num2
    num2_1 = num2 + num1
    return (int(num1_2) > int(num2_1)) - (int(num1_2) < int(num2_1)) # num1_2이 크다면 1,  num2_1이 크면 -1, 같으면 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(cmp_sort), reverse=True)
    numbers = "".join(numbers)
    
    if numbers[0] == "0": 
        return "0"
    
    return numbers