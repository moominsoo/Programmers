def solution(nums):
    answer=0
    num=int(len(nums)/2)
    setnum=list(set(nums))
    hash={}
    for i in setnum:
        hash[i]='a'
        num-=1
        if num==0:
            answer= list(hash.values()).count('a')
            break
    answer=list(hash.values()).count('a')
    return answer

#nums=[3,1,2,3]
#num=len(nums)//2
#hash={}
#for i in nums:
#    hash[i]=1
#setnum=list(set(nums)) #중복제거된 list
#for i in range(num):
#    setnum[i]='a'
#print(setnum.count('a'))