from pydoc import tempfilepager
import sys
import collections
from collections import deque

gwalho=deque()
temp=sys.stdin.readline()
for i in temp:
    gwalho.append(i)

stack=[]
flag=1
for i in range(len(gwalho)):
    elem=gwalho.popleft()

    if elem=='(' or elem=='[':
        stack.append(elem)
    else:
        if elem==')':
            if stack and stack[-1]=='(':
                stack.pop()
                stack.append(2)
            else:
                temp=0
                if not stack:
                    flag=0
                    break
                while stack:
                    if stack[-1]=='(':
                        stack.pop()
                        stack.append(temp*2)
                        break
                    elif stack[-1]=='[':
                        flag=0
                        break
                    else:
                        temp+=stack[-1]
                        stack.pop()
        if elem==']':
            if stack and stack[-1]=='[':
                stack.pop()
                stack.append(3)
            else:
                temp=0
                if not stack:
                    flag=0
                    break
                while stack:
                    if stack[-1]=='[':
                        stack.pop()
                        stack.append(temp*3)
                        break
                    elif stack[-1]=='(':
                        flag=0
                        break
                    else:
                        temp+=stack[-1]
                        stack.pop()

        if flag==0:
            break
for i in stack:
    if type(i)!=int:
        flag=0
        break
if flag==1:
    print(sum(stack))
if flag==0:
    print(0)