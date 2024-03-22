def solution(array):
    array.sort()
    return array[int(len(array)/2)]

#return sorted(array)[len(array) // 2] sorted 내장함수 사용
