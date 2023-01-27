import sys
from collections import deque
n,m,k=map(int,sys.stdin.readline().split())

maps=[[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    r,c=map(int,sys.stdin.readline().split())
    maps[r][c] = "!"


maxi=0
def bfs(maps,start,maxi):
    a = [-1, 1, 0, 0]
    b = [0, 0, -1, 1]
    count=1
    li=deque([start])
    maps[start[0]][start[1]] = 1
    while li:
        x,y=li.popleft()
        for i in range(4):
            x_i=x+a[i]
            y_i=y+b[i]
            if x_i< n+1 and x_i>0 and y_i< m+1 and y_i>0:
                if maps[x_i][y_i] == "!":
                    if maps[x_i][y_i] != 1:
                        li.append([x_i,y_i])
                        maps[x_i][y_i] = 1
                        count+=1
    return max(maxi,count)

for i in range(1,n+1):
    for j in range(1,m+1):
        if maps[i][j] == "!":
            maxi=bfs(maps,[i,j],maxi)

print(maxi)


