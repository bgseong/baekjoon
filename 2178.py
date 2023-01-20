import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())

map=[]
visit=[]
for _ in range(n):
    visit.append([0 for i in range(m)])
for _ in range(n):
    map.append(sys.stdin.readline().replace("\n",""))

def bfs(visit,map,start):
    a = [-1, 1, 0, 0]
    b = [0, 0, -1, 1]
    li=deque([start])
    visit[start[0]][start[1]] = 1
    while li:
        x,y,c=li.popleft()
        for i in range(4):
            x_i=x+a[i]
            y_i=y+b[i]
            if x_i< n and x_i>=0 and y_i< m and y_i>=0:
                if map[x_i][y_i] == "1":
                    if visit[x_i][y_i] == 0:
                        li.append([x_i,y_i,c+1])
                        visit[x_i][y_i]+=c+1

bfs(visit,map,[0,0,0])
print(visit[n-1][m-1]+1)
