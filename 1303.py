import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())

map=[]
visit=[]
for _ in range(m):
    visit.append([0 for i in range(n)])
for _ in range(m):
    map.append(sys.stdin.readline().replace("\n",""))

def bfs(visit,map,w,start):
    a = [-1, 1, 0, 0]
    b = [0, 0, -1, 1]
    li=deque([start])
    visit[start[0]][start[1]] = 1
    count=1
    while li:
        x,y=li.popleft()
        for i in range(4):
            x_i=x+a[i]
            y_i=y+b[i]
            if x_i< m and x_i>=0 and y_i< n and y_i>=0:
                if visit[x_i][y_i] == 0:
                    if map[x_i][y_i] == w:
                        count+=1
                        li.append([x_i,y_i])
                        visit[x_i][y_i]=1
    return count
dic={"W":0,"B":0}
for i in range(n):
    for j in range(m):
        if visit[j][i] == 0:
            c=bfs(visit,map,map[j][i],[j,i])
            dic[map[j][i]]+=c**2
print(f'{dic["W"]} {dic["B"]}')
