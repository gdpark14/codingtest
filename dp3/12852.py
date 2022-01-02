import sys
import collections

num=int(sys.stdin.readline())

temp_dp=collections.defaultdict(int)
for i in range(1,num+1):
    temp_dp[i]=0
dp=temp_dp
route=[0]
for i in dp.keys():
    if i==1:
        continue
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i//2]+1,dp[i//3]+1,dp[i-1]+1)
        if dp[i//2]+1<min(dp[i//3]+1,dp[i-1]+1):
            route.append(i//2)
        elif dp[i//3]+1<dp[i-1]+1:
            route.append(i//3)
        else:
            route.append(i-1)
    elif i%3==0:
        dp[i]=min(dp[i//3]+1,dp[i-1]+1)
        if dp[i//3]+1<dp[i-1]+1:
            route.append(i//3)
        else:
            route.append(i-1)
    elif i%2==0:
        dp[i]=min(dp[i//2]+1,dp[i-1]+1)
        if dp[i//2]+1<dp[i-1]+1:
            route.append(i//2)
        else:
            route.append(i-1)
    else:
        dp[i]=dp[i-1]+1
        route.append(i-1)
print(dp[num])

temp=num
for i in range(dp[num]+1):
    print(temp, end=' ')
    temp=route[temp-1]

    