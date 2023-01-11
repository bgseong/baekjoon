import sys
li=[0,0]
for _ in range(10):
    n,k=map(int,sys.stdin.readline().split())
    li[0]=max(li[0],li[1]+k-n)
    li[1]=li[1]+k-n
print(li[0])
