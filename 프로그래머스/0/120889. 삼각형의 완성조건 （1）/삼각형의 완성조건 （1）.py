def solution(sides):
    sides.sort()
    if sides[-1] < (sides[-2]+sides[-3]):
        return 1
    else: 
        return 2