import sys
import collections

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
route=[-1]
dp=[1]
for i in range(1,num):
    temp=nums[:i]
    temp_max=0
    temp_index=-1

    for j in range(len(temp)):
        if temp[j]<nums[i]:
            if dp[j]>temp_max:
                temp_index=j
            temp_max=max(temp_max,dp[j])

    count=temp_max+1
    dp.append(count)
    route.append(temp_index)

print(max(dp))

num_index=dp.index(max(dp))

reverse_ans=[]
for i in range(max(dp)):
    ans_num=nums[num_index]
    reverse_ans.append(ans_num)
    num_index=route[num_index]

for i in range(len(reverse_ans)):
    print(reverse_ans[-(i+1)],end=' ')