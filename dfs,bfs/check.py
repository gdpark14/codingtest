a=[0,0,0,0,0]

def check(i,b):
    print(id(b))
    if i==4:
        return
    b[i]=0
    check(i+1,b)
check(0,a)
