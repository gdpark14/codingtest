import sys
import collections

n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
acc_sum=collections.defaultdict(int)
acc_sum[0]=0
acc_sum[1]=nums[0]
for i in range(2,len(nums)+1):
    acc_sum[i]=acc_sum[i-1]+nums[i-1]


for p in range(m):
    i,j=map(int,sys.stdin.readline().split())
    print(acc_sum[j]-acc_sum[i-1])

    