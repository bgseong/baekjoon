import sys
n,m=map(int,sys.stdin.readline().split())

n_li=[]
for _ in range(n):
    P,L=map(int,sys.stdin.readline().split())
    li=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
    if L<len(li):
        n_li.append(li[L-1])
    else:
        n_li.append(1)
c=0
for i in sorted(n_li):
    if m < i:
        break
    else:
        m-=i
        c+=1
print(c)
