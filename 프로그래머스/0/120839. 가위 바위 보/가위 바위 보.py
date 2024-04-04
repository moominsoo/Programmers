def solution(rsp):
    win={"0":"5","2":"0","5":"2"}
    solution=[]
    for i in rsp:
        solution.append(win[i])
        
    return ''.join(solution)