S = 0
avr = 0
money = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
res = ""
for i in range(0, 12):
    money[i] = int(input())
    S = S + money[i]
avr = float(S / 12)
print("Tổng:", S)
print("TBC:", avr)
print("Các tháng nhiều hơn TBC:")
for i in range(0, 12):
    if money[i] > avr:
        res = res + str(i + 1) + " "
print(res)