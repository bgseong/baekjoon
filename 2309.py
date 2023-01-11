import sys
li=[]

for _ in range(9):
    li.append(int(sys.stdin.readline()))

total=sum(li)
a=0
for i in range(9):
    for j in range(i+1,9):
        if total-(li[i]+li[j]) == 100:
            a=1
            li[i]=0
            li[j]=0
            break
    if a==1:
        break
li.sort()
for i in range(2,9):
    print(li[i])



