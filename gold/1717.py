import sys
import collections
import copy

def get_parent(index):
    if jiphop[index]==index:
        return index
    parent=jiphop[index]
    index=get_parent(parent)

    return index

n,m=map(int,sys.stdin.readline().split())
jiphop=collections.defaultdict(int)
for i in range(n+1):
    jiphop[i]=i

for i in range(m):
    temp=list(sys.stdin.readline().split())


    oper=int(temp[0])
    a=int(temp[1])
    b=int(temp[2])

    if oper==0:
        parent_a=get_parent(a)
        parent_b=get_parent(b)

        if parent_a>=parent_b:
            jiphop[parent_b]=parent_a
        else:
            jiphop[parent_a]=parent_b

    if oper==1:
        parent_a=get_parent(a)
        parent_b=get_parent(b)

        if parent_a==parent_b:
            print("yes")
        else:
            print("no")
