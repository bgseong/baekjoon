import sys
from collections import deque


n,m=map(int,sys.stdin.readline().split())

dic={}

def bfs(start,dic):
    a=[2,1]
    li=deque([[start,1]])
    while li:
        x,c=li.popleft()
        for i in a:
            if i == 2:
                x_i=x*2
            else:
                x_i=int(f'{x}{i}')
            if x_i < m:
                li.append([x_i,c+1])
                dic[x_i]=c+1
            if x_i == m:
                li.append([x_i,c+1])
                dic[x_i]=c+1
                return 0


bfs(n,dic)
try:
    print(dic[m])
except:
    print(-1)

