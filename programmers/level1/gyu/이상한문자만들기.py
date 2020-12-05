def solution(s):
    answer = ""
    lst = s.split(' ')

    for string in lst:
        for i in range(len(string)):
            if i % 2 == 0:
                answer += string[i].upper()
            else:
                answer += string[i].lower()
        answer += ' '

    return answer[:-1]