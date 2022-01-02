import sys
import collections

n=int(input())
paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

global white
global blue

white=0
blue=0

def end(temp,which):
    count=0
    for i in range(len(temp)):
        if which in temp[i]:
            break
        count+=1
    if count==len(temp):
        return True

def check(small_page):
    global blue
    global white

    if end(small_page,0):
        blue+=1
        return
    if end(small_page,1):
        white+=1
        return

    length=len(small_page)//2
    first=[]
    second=[]
    third=[]
    fourth=[]
    for i in range(length):
        first.append(small_page[i][0:length])
        second.append(small_page[i][length:])
        third.append(small_page[i+length][0:length])
        fourth.append(small_page[i+length][length:])
    check(first)
    check(second)
    check(third)
    check(fourth)

check(paper)
print(white,blue)