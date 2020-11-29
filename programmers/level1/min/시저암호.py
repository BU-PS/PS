import string as strings


def solution(string, num):
    result = list()
    alphabet_sizes = 26
    lower_cases = {s: index for index, s in enumerate(list(strings.ascii_lowercase))}
    upper_cases = {s: index for index, s in enumerate(list(strings.ascii_uppercase))}

    for letter in string:
        change_letter = None
        change_index = None

        if letter.isspace():
            change_letter = letter
        elif letter.islower():
            change_index = (lower_cases.get(letter) + num) % alphabet_sizes
            change_letter = list(lower_cases.keys())[change_index]
        elif letter.isupper():
            change_index = (upper_cases.get(letter) + num) % alphabet_sizes
            change_letter = list(upper_cases.keys())[change_index]

        result.append(change_letter)
    return "".join(result)

solution("B", 2)
