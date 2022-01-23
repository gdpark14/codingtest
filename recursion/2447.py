import sys
import collections

N=int(input())

stars=[[' ' for _ in range(N)] for _ in range(N)] 
def fill_stars(size,x,y):
    if size==1:
        stars[y][x]='*'
    else:
        next_size=size//3
        for dy in range(3):
            for dx in range(3):
                if dx!=1 or dy!=1:
                    fill_stars(next_size,x+dx*next_size,y+dy*next_size)
fill_stars(N,0,0)
for star in stars:
    print(''.join(star))