import sys
import collections

N=int(input())
nums=list(map(int,sys.stdin.readline().split()))
o_sum,o_minus,o_mul,o_div=map(int,sys.stdin.readline().split())
operator=[]
for i in range(o_sum):
    operator.append("+")
for i in range(o_minus):
    operator.append("-")
for i in range(o_mul):
    operator.append("*")
for i in range(o_div):
    operator.append("/")

operator_candidate=[]
def dfs(cur_list,candidate):
    if len(cur_list)==N-1:
        operator_candidate.append(cur_list)
        return
    check=[]
    for i in range(len(candidate)):
        next_cur_list=cur_list.copy()
        next_candidate=candidate.copy()

        temp=next_candidate.pop(i)
        if temp in check:
            continue
        check.append(temp)
        
        next_cur_list.append(temp)
        dfs(next_cur_list,next_candidate)
dfs([],operator)

global max_ans
global min_ans

max_ans=-1000000000
min_ans=1000000000
def calculate(nums,operator):
    global max_ans
    global min_ans
    temp=nums[0]
    for i in range(len(operator)):
        if operator[i]=="+":
            temp+=nums[i+1]
        if operator[i]=="-":
            temp-=nums[i+1]
        if operator[i]=="*":
            temp=temp*nums[i+1]
        if operator[i]=="/":
            if temp>0:
                temp=temp//nums[i+1]
            if temp<0:
                temp=-temp
                temp=temp//nums[i+1]
                temp=-temp
    max_ans=max(max_ans,temp)
    min_ans=min(min_ans,temp)

for i in operator_candidate:
    calculate(nums,i)
print(len(operator_candidate))
print(max_ans)
print(min_ans)