import sys
import collections



line,time=map(int,sys.stdin.readline().split())
num_ant=int(sys.stdin.readline())


state=collections.defaultdict(list)

for i in range(num_ant):
    index,dirc=map(str,sys.stdin.readline().split())
    state[int(index)]=[dirc]

for i in range(time):
    new_state=collections.defaultdict(list)

    for index,dirc in state.items():
        if dirc==['L','D'] or dirc==['D','L']:
            new_state[index-1].append("L")
            new_state[index+1].append("D")

        elif dirc==['L']:
            if index==0:
                new_state[1].append("D")
            else:
                new_state[index-1].append("L")
        elif dirc==['D']:
            if index==line:
                new_state[line-1].append("L")
            else:
                new_state[index+1].append("D")
    state=new_state

ans=[]
for keys,values in state.items():
    if len(values)>1:
        ans.append(keys)
    ans.append(keys)
print(sorted(ans))

