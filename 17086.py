import sys
from collections import deque
import copy

n,m=map(int,sys.stdin.readline().split())
maps=[]
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

def bfs(maps,start):

    a=[-1,1,0,0,-1,1,-1,1]
    b=[-1,1,-1,1,0,0,1,-1]
    li=deque([start])
    while li:
        x,y=li.popleft()
        for i in range(8):
            x_i=x+a[i]
            y_i=y+b[i]
            if 0<=x_i<n and 0<=y_i<m:
                if maps[x_i][y_i] == 0:
                    maps[x_i][y_i] = maps[x][y]+1
                    li.append([x_i,y_i])
                elif maps[x_i][y_i] > maps[x][y]+1:
                    maps[x_i][y_i] = maps[x][y]+1
                    li.append([x_i,y_i])

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            bfs(maps,[i,j])

print(max(map(max,maps))-1)


