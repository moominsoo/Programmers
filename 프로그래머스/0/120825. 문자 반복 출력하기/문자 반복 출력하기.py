def solution(my_string, n):
    answer = [i*n for i in my_string]
    return ''.join(answer)

#return ''.join(i*n for i in my_string) 그냥 이렇게 해도됨
