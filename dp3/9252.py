import sys
import collections

a=sys.stdin.readline().strip().upper()
b=sys.stdin.readline().strip().upper()


matrix=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            matrix[i+1][j+1]=matrix[i][j]+1
        else:
            matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])

ans=matrix[len(a)][len(b)]
print(ans)
count=0
result=[]
index=[len(a),len(b)]
while count!=ans:
    if matrix[index[0]][index[1]-1]==matrix[index[0]][index[1]]-1 and matrix[index[0]-1][index[1]]==matrix[index[0]][index[1]]-1:
        result.append(a[index[0]-1])
        count+=1
        index=[index[0]-1,index[1]-1]
    elif matrix[index[0]][index[1]-1]>matrix[index[0]-1][index[1]]:
        index=[index[0],index[1]-1]
    else:
        index=[index[0]-1,index[1]]
for i in range(len(result)):
    print(result[-(i+1)],end='')

