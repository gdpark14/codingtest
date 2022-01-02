import sys

nums=list(map(int,sys.stdin.readline().split()))


def remainder(x,y,z):
    if y==1:
        return x%z

    next_y=y//2
    result=remainder(x,next_y,z)
    
    if y%2==0:
        return (result*result)%z
    else:
        return (result*result*x)%z

answer=remainder(nums[0],nums[1],nums[2])
print(answer)