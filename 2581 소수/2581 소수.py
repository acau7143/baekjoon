m = int(input())
n = int(input())
num = []

for i in range(m, n+1):  
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                if i == j:
                    num.append(i)
                break

if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)