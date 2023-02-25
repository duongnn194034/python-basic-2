res = ""
max = -99999
min = 99999
for i in range(1, 8):
    t = float(input())
    if t < 10:
        res = res + str(i) + " "
    if t < min:
        min = t
    if t > max:
        max = t
print(res)
print(min)
print(max)

