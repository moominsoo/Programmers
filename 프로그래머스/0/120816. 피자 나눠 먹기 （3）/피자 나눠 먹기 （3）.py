def solution(slice, n):
    return (n//slice) + int(n%slice !=0) #맞으면 1, 틑리면 0반환
# return n//slice + (1 if n%slice else 0)
