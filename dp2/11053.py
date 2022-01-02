import sys
import collections

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

dp=[]

for i in range(len(nums)):
    dp.append(1)

for i in range(1,len(nums)):
    temp=nums.copy()
    temp=temp[0:i]

    cnt=0
    for j in range(0,len(temp)):
        if nums[i]>temp[j]:
            cnt=max(cnt,dp[j])
    cnt+=1
    dp[i]=cnt
    
print(max(dp))