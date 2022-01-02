import sys
import collections

N,P,Q=map(int,sys.stdin.readline().split())
nums=collections.defaultdict(int)
nums[0]=1

def dfs(n):
    if nums[n]!=0:
        return nums[n]
    nums[n]=dfs(n//P)+dfs(n//Q)

    return nums[n]

dfs(N)
print(nums[N])