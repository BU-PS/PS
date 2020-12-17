def solution(phone_number):
    answer=''
    for i in str(phone_number):
        answer+=i
        num=answer[:-4]
        num=num.translate(str.maketrans('0123456789','**********'))
    return num+answer[-4:]