# 1. 왼손 오른손 키패트 맵핑
# 2. 중간 수인 경우 비교
#   - 왼손 ?
#   - 오른손 ?

keypad = {
        1: {
            "hand": "left",
            "location": (0, 0)
        },
        2: {
            "hand": None,
            "location": (0, 1)
        },
        3: {
            "hand": "right",
            "location": (0, 2)
        },
        4: {
            "hand": "left",
            "location": (1, 0)
        },
        5: {
            "hand": None,
            "location": (1, 1)
        },
        6: {
            "hand": "right",
            "location": (1, 2)
        },
        7: {
            "hand": "left",
            "location": (2, 0)
        },
        8: {
            "hand": None,
            "location": (2, 1)
        },
        9: {
            "hand": "right",
            "location": (2, 2)
        },
        "*": {
            "hand": None,
            "location": (3, 0)
        },
        0: {
            "hand": None,
            "location": (3, 1)
        },
        "#": {
            "hand": None,
            "location": (3, 2)
        }
    }


def solution(numbers: list, hand: str):
    answer = ""
    past_left = "*"
    past_right = "#"

    for number in numbers:
        if keypad[number]["hand"] == "left":
            answer += "L"
            past_left = number

        elif keypad[number]["hand"] == "right":
            answer += "R"
            past_right = number

        else:
            number_to_left_hand = get_distance_between_number(keypad[number]["location"], keypad[past_left]["location"])
            number_to_right_hand = get_distance_between_number(keypad[number]["location"], keypad[past_right]["location"])

            if number_to_left_hand < number_to_right_hand:
                answer += "L"
                past_left = number

            elif number_to_left_hand > number_to_right_hand:
                answer += "R"
                past_right = number

            else:
                if hand == "left":
                    answer += "L"
                    past_left = number

                else:
                    answer += "R"
                    past_right = number

    return answer


def get_distance_between_number(location1, location2):
    return abs(location2[0] - location1[0]) + abs(location2[1] - location1[1])


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")