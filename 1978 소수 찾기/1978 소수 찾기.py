a = int(input())
b = list(map(int,input().split()))

cnt = 0
for n in b:
    for j in range(2,n+1):
        if n % j == 0:
            if n == j:
                cnt +=1
            break
print(cnt)