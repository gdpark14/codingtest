import sys
import collections

comp={}
ans=collections.defaultdict(int)

black=[]
sero,garo,black_num=map(int,sys.stdin.readline().split())

for i in range(black_num):
    black.append(list(map(int,sys.stdin.readline().split())))

# 센터 중심 확인
def check(center:list):
    global comp

    if str(center) in comp:
        return
    else:
        temp=[[center[0]-1,center[1]-1],[center[0],center[1]-1],[center[0]+1,center[1]-1],[center[0]-1,center[1]],[center[0],center[1]],[center[0]+1,center[1]],[center[0]-1,center[1]+1],[center[0],center[1]+1],[center[0]+1,center[1]+1]]
        count=0
        for j in range(len(temp)):
            if temp[j] in black:
                count+=1
        ans[count]+=1
        comp[str(center)]=1

for k in black:
    for a in range(-1,2):
        for b in range(-1,2):
            if (k[0]+a)>1 and (k[0]+a)<sero and (k[1]+b)>1 and (k[1]+b)<garo:
                check([k[0]+a,k[1]+b])

minus_temp=sum(ans.values())
ans_zero=(garo-2)*(sero-2)-minus_temp
print(ans_zero)
for i in range(1,10):
    if i in ans:
        print(ans[i])
    else:
        print(0)