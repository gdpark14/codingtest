import sys
import collections

N=int(input())
arr=list(map(int,sys.stdin.readline().split()))

ans=2000000000
ans_pair=[0,0]
st=0
en=len(arr)-1

while st<en:
    if abs(arr[st]+arr[en])<=ans:
        ans=abs(arr[st]+arr[en])
        ans_pair=[arr[st],arr[en]]
        
    if arr[st]+arr[en]>0:
        en-=1
    elif arr[st]+arr[en]<0:
        st+=1
    else:
        break

print(ans_pair[0],ans_pair[1])