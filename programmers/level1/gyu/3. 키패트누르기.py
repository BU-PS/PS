# number = (x, y), current(x, y)
def distance(number, current):
    return abs(number[0] - current[0]) + abs(number[1] - current[1])    

def solution(numbers, hand):
    answer = ''
    keyboard = {
        "1": (1, 1), "2":(1, 2), "3":(1, 3),
        "4": (2, 1), "5":(2, 2), "6":(2, 3),
        "7": (3, 1), "8":(3, 2), "9":(3, 3),
        "*": (4, 1), "0":(4, 2), "#":(4, 3)
    }   
    current_left = "*"
    current_right = "#"
    
    for number in numbers:
        number = str(number)
        if number in ["1", "4", "7"]:
            answer += "L"
            current_left = number
        elif number in ["3", "6", "9"]:
            answer += "R"
            current_right = number
        else:   # 중간 위치에 있는 경우
            left = distance(keyboard[number], keyboard[current_left])       # 중간 위치와 left 거리 계산
            right = distance(keyboard[number],keyboard[current_right])      # 중간 위치와 right 거리 계산
            if left < right:            # 거리가 right가 더 크면
                answer += "L"           # left 로 누름
                current_left = number
            elif left > right:          # 거리가 left 가 더 크면
                answer += "R"           # right 로 누름
                current_right= number
            else:                       # 같은 경우
                if hand == "left":      # hand(손잡이) 위치로 결정
                    answer += "L"
                    current_left = number
                else:
                    answer += "R"
                    current_right= number
    return answer