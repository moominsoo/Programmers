def solution(my_string, n):
    answer = [i*n for i in my_string]
    return ''.join(answer)