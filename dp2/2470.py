import sys
import collections

num=int(sys.stdin.readline())
solution=list(map(int,sys.stdin.readline().split()))
solution=sorted(solution)

start=0
end=len(solution)-1

ans=solution[start]+solution[end]
ans_start=start
ans_end=end

while start<end:
    temp=solution[start]+solution[end]
    if abs(temp)<abs(ans):
        ans=temp
        ans_start=start
        ans_end=end
        if temp==0:
            break
    if temp<0:
        start+=1
    elif temp>0:
        end-=1
print(solution[ans_start],solution[ans_end])

