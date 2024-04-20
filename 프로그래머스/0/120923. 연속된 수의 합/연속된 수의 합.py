def solution(num, total):
    answer=[]
    a = total //num
    for i in range(a-(num-1)//2,a+(num+2)//2):
        answer.append(i)
    return answer