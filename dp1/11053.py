import sys
import collections

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
count=[]

# dp행렬
for i in range(len(nums)):
    count.append(1)

for i in range(1,len(nums)):
    # index 앞까지 행렬
    temp=nums.copy()
    temp=temp[0:i]
    
    max_cnt=0
    for j in range(0,len(temp)):
        # temp요소가 해당index보다 작다면
        if temp[j]<nums[i]:
            max_cnt=max(max_cnt,count[j])
    max_cnt+=1
    count[i]=max_cnt
print(max(count))