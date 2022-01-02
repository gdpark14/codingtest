import sys
import collections

N=int(input())
K=int(input())

start=1
end=K

def check(temp,comp):
    if temp<comp:
        return False
    else:
        return True

while start+1<end:
    mid=(start+end)//2

    temp_start=0
    temp_mid=0
    temp_end=0
    for i in range(1,N+1):
        index_start=min(start//i,N)
        temp_start+=index_start

        index_mid=min(mid//i,N)
        temp_mid+=index_mid

        index_end=min(end//i,N)
        temp_end+=index_end
    
    if check(temp_start,K)==check(temp_mid,K):
        start=mid
    elif check(temp_end,K)==check(temp_mid,K):
        end=mid

print(end)
