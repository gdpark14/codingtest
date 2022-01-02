import sys
import collections

k=int(input())
x,y=map(int,sys.stdin.readline().split())
length=2**k

i=(length-1)-(y-1)
j=x-1

matrix=[[0]*length for _ in range(length)]
matrix[i][j]=-1

def list_sum(list1,list2,list3,list4):
    up=list(map(list.__add__,list1,list2))
    down=list(map(list.__add__,list3,list4))
    ans=up+down
    return ans

def check(temp):
    length=len(temp)
    count=0
    for i in range(length):
        for j in range(length):
            if temp[i][j]!=0:
                count=1
                break
    return count

global num
num=0

def divide_conquer(temp):


    if len(temp)==1:
        return temp
    
    global num
    num+=1

    mid=len(temp)//2
    first=[i[0:mid] for i in temp[0:mid]]
    second=[i[mid:] for i in temp[0:mid]]
    third=[i[0:mid] for i in temp[mid:]]
    fourth=[i[mid:] for i in temp[mid:]]

    if check(first)!=1:
        first[mid-1][mid-1]=num
    if check(second)!=1:
        second[mid-1][0]=num
    if check(third)!=1:
        third[0][mid-1]=num
    if check(fourth)!=1:
        fourth[0][0]=num
    

    x=divide_conquer(first)
    y=divide_conquer(second)
    z=divide_conquer(third)
    k=divide_conquer(fourth)

    result=list_sum(x,y,z,k)
    return result

ans=divide_conquer(matrix)


for i in ans:
    for j in range(len(i)):
        if j==len(i)-1:
            print(i[j])
        else:
            print(i[j],end=' ')