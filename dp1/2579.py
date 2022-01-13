import sys
import collections

num=int(input())
stairs=[]
for i in range(num):
    temp=int(input())
    stairs.append(temp)
dp=[]
dp.append([[stairs[0],0]])
if num==1:
    print(stairs[0])
else:

    dp.append([[stairs[0]+stairs[1],1],[stairs[1],0]])

    index=2
    while index<num:
        dp_index=[]
        ##before 2 step
        max_value=0
        for term in dp[index-2]:
            value=term[0]
            max_value=max(max_value,value)
        dp_index.append([max_value+stairs[index],0])

        ##before 1 step
        for term in dp[index-1]:
            if term[1]==0:
                dp_index.append([term[0]+stairs[index],1])
        dp.append(dp_index)
        index+=1

    candidate=dp[-1]
    candidate=sorted(candidate, key= lambda x: x[0])
    print(candidate[-1][0])