s = str(input())
res = ""
count = 0
for i in range(0, len(s)):
    if s[i] == "A" or s[i] == "a":
        res = res + str(i) + " "
        count = count + 1
print(res)
print(count)