# 1. 문자열 내 마지막 뒷 부분 *변경
# 2. 리턴


def solution(phone_number: str) -> str:
    phone_number_len = len(phone_number)
    return "*" * (phone_number_len - 4) + phone_number[phone_number_len - 4:]
