import sys
import collections

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

dp=[]
for i in range(num):
    dp.append(1)
if nums:
    dp[0]=nums[0]
for i in range(1,num):
    dp[i]=max(0,dp[i-1])+nums[i]

print(max(dp))
