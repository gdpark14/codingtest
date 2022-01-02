import sys

num=int(sys.stdin.readline())
length=list(map(int,sys.stdin.readline().split()))
price=list(map(int,sys.stdin.readline().split()))

temp=price[0]
gas=temp*length[0]
for i in range(1,num-1):
    if price[i]<temp:
        temp=price[i]
    gas+=temp*length[i]

print(gas)