import sys
import collections

M,N,L=map(int,sys.stdin.readline().split())
shoot=sorted(list(map(int,sys.stdin.readline().split())))
animals=[]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    animals.append(temp)
animals=sorted(animals)

ans=0
for animal in animals:
    ##check nearest shoot
    start=0
    end=len(shoot)-1

    while start<=end:
        mid=(start+end)//2

        temp=abs(shoot[mid]-animal[0])+animal[1]
        if(temp<=L):
            ans+=1
            break
        else:
            if shoot[mid]<animal[0]:
                start=mid+1
            else:
                end=mid-1

print(ans)