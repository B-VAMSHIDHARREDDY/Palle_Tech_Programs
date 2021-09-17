n = int(input())
li=[]
for i in range(n):
    li.append(input())
for i in range(n):
    count = 0
    for k in range(len(li[i])-1):
        if li[i][k+1] == li[i][k]:
            count+=1
    print(count)
