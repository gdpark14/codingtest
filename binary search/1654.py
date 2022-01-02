import sys

num,final=map(int,sys.stdin.readline().split())
lan=[]
for i in range(num):
    temp=int(sys.stdin.readline())
    lan.append(temp)
lan=sorted(lan,key=lambda x:x)

ans=[]
def search(start,end):
    if start>end:
        return end

    mid=(start+end)//2
    count=0
    for i in range(len(lan)):
        count+=(lan[i]//mid)

    if final>count:
        return search(start,mid-1)
    elif final<=count:
        return search(mid+1,end)

print(search(1,lan[-1]))
