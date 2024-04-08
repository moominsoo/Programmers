def solution(num_list):
    matrix=1
    for i in num_list:
        matrix *= i
    if matrix > (sum(num_list))**2:
        return 0
    else:
        return 1