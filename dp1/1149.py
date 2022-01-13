import sys
import collections

N=int(input())
RGB=[]
dp=[]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    if i==0:
        dp.append(temp[0])
        dp.append(temp[1])
        dp.append(temp[2])

    RGB.append(temp)
index=1

while index<N:
    dp_new=[]
    first_min=min(dp[1],dp[2])
    dp_new.append(first_min+RGB[index][0])

    second_min=min(dp[0],dp[2])
    dp_new.append(second_min+RGB[index][1])

    third_min=min(dp[0],dp[1])
    dp_new.append(third_min+RGB[index][2])

    dp=dp_new
    index+=1
print(min(dp))