import sys
import collections



L,T=map(int,sys.stdin.readline().split())
N=int(input())
ants=[]
for i in range(N):
    temp=sys.stdin.readline().split()
    temp[0]=int(temp[0])
    ants.append(temp)


for ant in ants:
    if ant[1]=="D":
        one_step=L-ant[0]
        if one_step>=T:
            ant[0]+=T
        else:
            way_to_go=T-one_step
            #가장 오른쪽
            if (way_to_go//L)%2==0:
                move=way_to_go%L
                ant[0]=L-move
            #가장 왼쪽
            else:
                move=way_to_go%L
                ant[0]=move
    else:
        one_step=ant[0]
        if one_step>=T:
            ant[0]-=T
        else:
            way_to_go=T-one_step
            if (way_to_go//L)%2==0:
                move=way_to_go%L
                ant[0]=move
            else:
                move=way_to_go%L
                ant[0]=L-move


ants.sort(key=lambda x:[x[0]])
ans=[]
for i in ants:
    ans.append(i[0])
print(*ans)