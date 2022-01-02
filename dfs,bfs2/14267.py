import sys
import collections

sys.setrecursionlimit(99999)

n,m=map(int,sys.stdin.readline().split())
boss=list(map(int,sys.stdin.readline().split()))
company=collections.defaultdict(list)
member=collections.defaultdict(int)

for i in range(1,len(boss)+1):
    company[boss[i-1]].append(i)
    member[i]=0

def compliment(who,how):
    member[who]+=how
    next=company[who]
    for i in range(len(next)):
        compliment(next[i],how)
    return

grade=collections.defaultdict(int)

for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    grade[a]+=b

for key,value in grade.items():
    compliment(key,value)


for i in member.values():
    print(i,end=' ')
