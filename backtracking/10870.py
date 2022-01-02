import sys
import collections

num=int(input())

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        value=fib(num-1)+fib(num-2)
        return value

print(fib(num))