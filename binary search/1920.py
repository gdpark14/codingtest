import sys

num=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

num_arr=int(sys.stdin.readline())
nums_arr=list(map(int,sys.stdin.readline().split()))

nums=sorted(nums,key=lambda x:x)

def search(start,end,value):
    if start>end:
        return 0

    mid=(start+end)//2

    if value==nums[mid]:
        return 1
    else:
        if nums[mid]>value:
            return search(start,mid-1,value)
        elif nums[mid]<value:
            return search(mid+1,end,value)

for i in nums_arr:
    print(search(0,num-1,i))