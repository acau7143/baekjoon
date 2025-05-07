n = int(input())
num = list(map(int,input().split()))

num.sort()

m = int(input())
X = list(map(int,input().split()))


for i in X:
    start = 0
    end = len(num) - 1
    mid = (start + end) // 2
    result = 0
    while start <= end:
        if i == num[mid]:
            result += 1
            break
        elif i < num[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    print(result)