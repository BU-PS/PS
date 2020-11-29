def solution(a: list, b: list) -> int:
    result = list()

    for num_a, num_b in zip(a, b):
        number = num_a * num_b
        result.append(number)
    return sum(result)


def other_solution(a: list, b: list) -> int:
    return sum([num_a * num_b for num_a, num_b in zip(a, b)])

