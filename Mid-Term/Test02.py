s = str(input())
index = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == ".":
        index = i + 1
        break
if s[index:] == "py":
    print("YES")
else:
    print("NO")