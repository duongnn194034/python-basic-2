s = str(input())
n0 = n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = 0
for i in range(0, len(s)):
    if s[i] == "0":
        n0 = n0 + 1
    elif s[i] == "1":
        n1 = n1 + 1
    elif s[i] == "2":
        n2 = n2 + 1
    elif s[i] == "3":
        n3 = n3 + 1
    elif s[i] == "4":
        n4 = n4 + 1
    elif s[i] == "5":
        n5 = n5 + 1
    elif s[i] == "6":
        n6 = n6 + 1
    elif s[i] == "7":
        n7 = n7 + 1
    elif s[i] == "8":
        n8 = n8 + 1
    elif s[i] == "9":
        n9 = n9 + 1
print("Số chữ số '0':", n0)
print("Số chữ số '1':", n1)
print("Số chữ số '2':", n2)
print("Số chữ số '3':", n3)
print("Số chữ số '4':", n4)
print("Số chữ số '5':", n5)
print("Số chữ số '6':", n6)
print("Số chữ số '7':", n7)
print("Số chữ số '8':", n8)
print("Số chữ số '9':", n9)