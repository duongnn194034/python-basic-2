inp = open('songuyen.txt')
content = str(inp.readline());
comma = [0, 0]
j = 0
for i in range(0, len(content)):
    if content[i] == ',':
        comma[j] = i
        j = j + 1
a = int(content[0:comma[0]])
b = int(content[comma[0] + 1:comma[1]])
c = int(content[comma[1] + 1:])
oup = open('tich.txt', 'w')
oup.write(str(a * b * c))