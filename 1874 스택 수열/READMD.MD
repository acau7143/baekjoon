# 📚 스택 수열 (Stack Sequence)

## 📝 문제 설명
1부터 n까지의 정수를 스택에 오름차순으로 push 했다가 pop 하여 특정 수열을 만드는 문제입니다.  
주어진 수열이 스택을 이용해 만들 수 있는지 판단하고, 만들 수 있다면 push (`+`)와 pop (`-`) 연산 순서를 출력합니다.  
만들 수 없다면 `NO`를 출력합니다.

## 💡 입력 설명
- 첫째 줄에 수열의 길이 `n`이 주어집니다. (1 ≤ n ≤ 100,000)
- 다음 n개의 줄에는 수열의 각 원소가 한 줄에 하나씩 주어집니다.

## ✅ 출력 설명
- 만들 수 있다면 각 연산을 한 줄에 하나씩 출력 (`+` 또는 `-`)
- 만들 수 없다면 `NO` 출력



## 🧠 코드 설명 (Python)
```python
n = int(input())
list = []       # 연산 기록 리스트
stack = []      # 스택
point = 1       # 다음에 push할 숫자
find = True     # 수열을 만들 수 있는지 여부

for i in range(n):
    num = int(input())

    while point <= num:         # num까지 push
        stack.append(point)
        list.append("+")
        point += 1

    if stack[-1] == num:        # 원하는 숫자면 pop
        stack.pop()
        list.append("-")
    else:
        find = False            # 만들 수 없는 경우
        break

if not find:
    print("NO")
else:
    for i in list:
        print(i)