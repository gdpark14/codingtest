from random import *

i=randint(1,100)
while True:
    temp=int(input())
    if i<temp:
        print("too big")
    elif i>temp:
        print("too small")
    else:
        print("입력한 숫자는 ",temp," 입니다.")
    