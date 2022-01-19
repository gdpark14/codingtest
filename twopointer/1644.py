import sys
import collections

N=int(input())

prime_list=[]
def prime(prime_list,index):
    if index==1:
        return False
    else:
        a=[False,False]+[True]*(index-1)
        for i in range(2,N+1):
            if a[i]:
                prime_list.append(i)
                for j in range(2*i,N+1,i):
                    a[j]=False
        return True
count=0
if prime(prime_list,N):
    count=0
    end=0
    start=0
    temp=prime_list[start]+prime_list[end]
    for i in range(len(prime_list)):
        temp-=prime_list[start]
        start=i
        while temp<N and end<len(prime_list)-1:
            end+=1
            temp+=prime_list[end]
        if temp==N:
            count+=1
print(count)
