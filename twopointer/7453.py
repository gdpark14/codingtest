import sys
import collections

n=int(input())
a_list=[]
b_list=[]
c_list=[]
d_list=[]
for _ in range(n):
    a,b,c,d=map(int,sys.stdin.readline().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)
    d_list.append(d)


def mixup(first,second):
    temp_list=[]
    for i in range(len(first)):
        for j in range(len(second)):
            temp_list.append(first[i]+second[j])
    return temp_list
a_b_list=mixup(a_list,b_list)
c_d_list=mixup(c_list,d_list)


total_list=mixup(a_b_list,c_d_list)
total_list.sort()

start=0
end=len(total_list)-1

while start+1<end:
    mid=(start+end)//2
    if total_list[mid]<0:
        start=mid
    elif total_list[mid]>=0:
        end=mid
count=0
while total_list[end]==0:
    end+=1
    count+=1
print(count)