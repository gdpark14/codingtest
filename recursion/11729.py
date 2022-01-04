import sys

num=int(sys.stdin.readline())
global count
count=0
ans=[]
def move(from_,to,num):
    if num==0:
        return
    else:
        global count
        count+=1
    stopby=6-(from_+to)
    move(from_,stopby,num-1)
    ans.append([from_,to])
    move(stopby,to,num-1)

move(1,3,num)
print(count)
for i in ans:
    print(*i)