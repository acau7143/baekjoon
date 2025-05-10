n = int(input())
list = []
stack = []
point = 1
find = True
for i in range(n):
    num = int(input())
    while point <= num:
        stack.append(point)
        list.append("+")
        point += 1

    if stack[-1] == num:
        stack.pop()
        list.append("-")

    else:
        find = False

if not find:
    print("NO")
else:
    for i in list:
        print(i)
