import sys

a=sys.stdin.readline().replace("\n","")
b=sys.stdin.readline().replace("\n","")

cnt=0
c=0

while c+len(b) <= len(a):
    aa=a[c:c+len(b)]
    if aa == b:
        cnt+=1
        c+=len(b)
    else:
        c+=1
print(cnt)
