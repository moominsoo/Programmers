def solution(box, n):
    roll= (box[0]//n) * (box[1]//n)
    answer = roll * (box[2]//n)
    return answer