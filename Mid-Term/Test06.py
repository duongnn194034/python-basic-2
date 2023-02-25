S = 0
avr = 0
money = []
res = ""
for i in range(1, 13):
    money[i] = int(input())
    S = S + money[i]
avr = float(S / 12)
print("Tổng:", S)
print("TBC:", avr)
print("Các tháng nhiều hơn TBC:")
for i in range(1, 13):
    if money[i] > avr:
        res = res + str(money[i]) + " "
print(res)