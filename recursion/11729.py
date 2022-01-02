import sys

num=int(sys.stdin.readline())
count=0

def move(from_,to,nums):
    global count

    if nums==0:
        return
    move(from_,6-(from_+to),nums-1)
    count+=1
    move(6-(from_+to),to,nums-1)

def move_count(from_,to,nums):
    global count

    if nums==0:
        return
    move_count(from_,6-(from_+to),nums-1)
    print(from_,to)
    move_count(6-(from_+to),to,nums-1)

move(1,3,num)
print(count)
move_count(1,3,num)