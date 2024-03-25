def solution(my_string):
    alpha=['a','e','i','o','u']
    answer = [x for x in my_string if x not in alpha]
    return ''.join(answer)