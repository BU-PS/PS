def solution(s: str) -> str:
    answer = ""

    split_strings = s.split(sep=" ")
    for strings in split_strings:
        for i in range(len(strings)):
            if i % 2 == 0:
                answer += strings[i].upper()
            else:
                answer += strings[i].lower()
        answer += " "
    return answer[:-1]
