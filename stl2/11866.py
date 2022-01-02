import sys

num,dist=map(int,sys.stdin.readline().split())

temp=[]
ans=[]
for i in range(num):
    temp.append(i+1)

index=0
while len(ans)!=num:
    index=(index+dist-1)%len(temp)
    add=temp[index]

    ans.append(add)
    temp.remove(add)


print("<",end='')
for i in range(len(ans)-1):
    print(ans[i],end=", ")
print(ans[-1],end='')
print(">")

