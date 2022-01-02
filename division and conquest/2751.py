import sys
import collections
from collections import deque

num=int(sys.stdin.readline())

nums=[]
for i in range(num):
    temp=int(sys.stdin.readline())
    nums.append(temp)

def merge_sort(obj):
    if len(obj)<=1:
        return obj

    mid=len(obj)//2
    temp_obj=obj.copy()
    left_sorted=merge_sort(temp_obj[0:mid])
    right_sorted=merge_sort(temp_obj[mid:])
    ans=merge(left_sorted,right_sorted)

    return ans

def merge(left,right):
    new_list=[]
    left_index=0
    right_index=0

    left=collections.deque(left)
    right=collections.deque(right)
    while left or right:
        if not left:
            new_list.append(right[right_index])
            right.popleft()
        elif not right:
            new_list.append(left[left_index])
            left.popleft()

        elif left[left_index]<right[right_index]:
            new_list.append(left[left_index])
            left.popleft()
        else:
            new_list.append(right[right_index])
            right.popleft()
    return new_list

x=merge_sort(nums)
for i in x:
    print(i)