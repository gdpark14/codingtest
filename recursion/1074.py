import sys

nums=list(map(int,sys.stdin.readline().split()))

def route(start_num,end_num,garo,sero,minus):
    
    

    if (start_num==end_num):
        if(garo-1==nums[2]) and(sero-1==nums[1]):
            print(start_num)
        return


    value=(end_num-start_num+1)//4


    if (nums[2]<=garo-minus-1) and (nums[1]<=sero-minus-1):
        route(start_num,start_num+value-1,garo-minus,sero-minus,minus//2)
    elif (nums[2]<=garo-1) and (nums[1]<=sero-minus-1):
        route(start_num+value,start_num+2*value-1,garo,sero-minus,minus//2)
    elif (nums[2]<=garo-minus-1) and (nums[1]<=sero-1):
        route(start_num+2*value,start_num+3*value-1,garo-minus,sero,minus//2)
    else:
        route(start_num+3*value,start_num+4*value-1,garo,sero,minus//2)

route(0,4**nums[0]-1,2**nums[0],2**nums[0],2**(nums[0]-1))

