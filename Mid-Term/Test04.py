s1 = str(input())
s2 = ""
for i in range(len(s1) - 1, -1, -1):
    s2 = s2 + s1[i]
if s2 == s1:
    print("YES")
else:
    print("NO")
