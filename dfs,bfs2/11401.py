import sys
import collections

n=int(input())
paper=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    paper.append(temp)

def check(check_paper):
    leng=len(check_paper)
    comp=check_paper[0][0]
    for i in range(leng):
        for j in range(leng):
            if check_paper[i][j]!=comp:
                return -2
    return comp

ans=collections.defaultdict(int)
ans[-1]=0
ans[0]=0
ans[1]=0

def divide(in_paper):
    if check(in_paper)!=-2:
        index=check(in_paper)
        ans[index]=ans[index]+1
        return
    term=len(in_paper)//3
    for i in range(3):
        for j in range(3):
            next=[]
            for k in range(term):
                temp=in_paper[i*term+k][j*term:j*term+term]
                next.append(temp)

            divide(next)

divide(paper)
print(ans[-1])
print(ans[0])
print(ans[1])