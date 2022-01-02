import sys

nums=int(sys.stdin.readline())

room=[]

for i in range(nums):
    temp=list(map(int,sys.stdin.readline().split()))
    room.append(temp)

room=sorted(room,key=lambda x : (x[0],x[1]))

occupy=room[0]
count=1
for i in range(1,len(room)):
    temp=room[i]
    if temp[0]>occupy[0] and temp[1]<occupy[1]:
        occupy=temp
    else:
        if temp[0]>=occupy[1]:
            occupy=temp
            count+=1

print(count)