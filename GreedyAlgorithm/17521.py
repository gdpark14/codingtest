import sys

days,seed=map(int,sys.stdin.readline().split())
coin=0
price=[]
for i in range(days):
    temp=int(sys.stdin.readline())
    price.append(temp)

for i in range(len(price)-1):
    if price[i+1]>price[i]:
        if seed>=price[i]:
            coin=seed//price[i]
            seed=seed%price[i]
    if price[i+1]<price[i]:
        seed=seed+coin*price[i]
        coin=0


if coin:
    seed=seed+coin*price[days-1]
    coin=0
print(seed)