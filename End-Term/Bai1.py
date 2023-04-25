inp = open('Ten.txt')
ten = str(inp.read())
oup = open('InHoa.txt', 'w')
oup.write(ten.upper())
