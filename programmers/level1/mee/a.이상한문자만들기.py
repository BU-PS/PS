def solution(s):
    answer=''
    s=s.split()

    for strings in s:
        for i in range(len(strings)):
            if i&1==0:
                answer+=strings[i].upper()
            else:
                answer+=strings[i].lower()
        answer+=' '

    return answer[:-1]