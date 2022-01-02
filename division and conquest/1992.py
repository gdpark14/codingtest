import sys
import collections

num=int(sys.stdin.readline())
maps=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(num)]

## flag==len(map) 이면 완성
def check(map):
    length=len(map)
    white_flag=0
    black_flag=0

    for i in range(length):
        if 0 in map[i]:
            break
        else:
            black_flag+=1
    
    for i in range(length):
        if 1 in map[i]:
            break
        else:
            white_flag+=1
    
    return [white_flag,black_flag]

def return_check(obj):

    value=check(obj)
    if value[0]==len(obj):
        print(0,end='')
        return
    elif value[1]==len(obj):
        print(1,end='')
        return
    else:
        print("(",end='')
        mid=len(obj)//2
        first=[]
        second=[]
        third=[]
        fourth=[]
        for i in range(mid):
            first.append(obj[i][0:mid])
            second.append(obj[i][mid:])
            third.append(obj[i+mid][0:mid])
            fourth.append(obj[i+mid][mid:])
        return_check(first)
        return_check(second)
        return_check(third)
        return_check(fourth)
        print(")",end='')
return_check(maps)