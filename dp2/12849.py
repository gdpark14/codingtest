import sys
import collections

D=int(input())
soongsil={
    'jeongbo':['jeonsan','mirae'],
    'jeonsan':['jeongbo','mirae','sinyang'],
    'mirae':['jeonsan','jeongbo','sinyang','hangyung'],
    'sinyang':['jeonsan','jinri','mirae','hangyung'],
    'jinri':['sinyang','student','hangyung'],
    'hangyung':['sinyang','jinri','hyungnam','mirae'],
    'student':['jinri','hyungnam'],
    'hyungnam':['hangyung','student']
    }

dp=[[1,'jeonsan'],[1,'mirae']]
index=1
while index<D:
    check=collections.defaultdict(int)
    while dp:
        temp=dp.pop()
        start=temp[1]
        before_num=temp[0]
        for next_temp in soongsil[start]:
            if next_temp not in check:
                check[next_temp]=before_num
            else:
                check[next_temp]+=before_num
    dp=[]
    for key,value in check.items():
        dp.append([value,key])
    index+=1
for ans in dp:
    if ans[1]=='jeongbo':
        print(ans[0]%1000000007)
