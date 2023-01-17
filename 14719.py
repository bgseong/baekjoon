import sys

h,w=map(int,sys.stdin.readline().split())

num=list(map(int,sys.stdin.readline().split()))

total=0
for i in range(h):
    stats=0
    last=0
    for j in range(w):
        if num[j]-i > 0:
            if stats == 0:
                stats=1
                last=j
            else:
                total+=j-last-1
                last=j

print(total)
