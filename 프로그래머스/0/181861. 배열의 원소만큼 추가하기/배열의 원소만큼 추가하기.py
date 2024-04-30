def solution(arr):
    result=[]
    for i in range(len(arr)):
        a = arr[i]
        add = [a]*a
        result += add
    return result