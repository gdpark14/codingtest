import sys
in_list=list(map(str,sys.stdin.readline().split()))

temp=[]

for char in in_list:
    if char=="(" or char=="[":
        temp.append(char)

    elif char==")" or char=="]":
