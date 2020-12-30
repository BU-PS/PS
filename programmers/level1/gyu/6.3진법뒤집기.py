def convert_base10(str_number):
    value = 0
    
    # 각 자릿수에 맞게 10진법으로 변환
    for i in range(len(str_number)):
        value += int(str_number[i]) * (3 ** i)
    return value

def convert_base3(n):
    converted_value = ''
    
    # 3진법 수행
    while n:
        converted_value += str(n%3)
        n //= 3
    return converted_value


def solution(n):
    converted_data = convert_base3(n)
    reversed_data = converted_data[::-1]
    return convert_base10(reversed_data)

