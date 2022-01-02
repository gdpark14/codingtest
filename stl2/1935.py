import sys
import collections

num=int(sys.stdin.readline())
equation=sys.stdin.readline().rstrip()

nums=[]
for i in range(num):
    nums.append(int(sys.stdin.readline()))

check=collections.defaultdict(int)

new_equation=[]
for i in range(len(equation)):
    if equation[i] in ['*','+','-','/']:
        new_equation.append(equation[i])
    else:
        if equation[i] in check:
            new_equation.append(check[equation[i]])
        else:
            check[equation[i]]=nums.pop(0)
            new_equation.append(check[equation[i]])

temp_num=[]
while new_equation:
    temp=new_equation.pop(0)
    if temp not in ['*','+','-','/']:
        temp_num.append(temp)
    else:
        b=temp_num.pop()
        a=temp_num.pop()
        if temp=='*':
            temp_num.append(b*a)
        elif temp=='/':
            temp_num.append(a/b)
        elif temp=='-':
            temp_num.append(a-b)  
        elif temp=='+':
            temp_num.append(a+b)    


# while temp_cal:
#     i=temp_cal.pop()
#     if i=='-':
#         b=temp_num.pop()
#         a=temp_num.pop()
#         temp_num.append(a-b)
#     else:
#         b=temp_num.pop()
#         a=temp_num.pop()
#         temp_num.append(a+b)

print(f"{temp_num[0]:.2f}")
        