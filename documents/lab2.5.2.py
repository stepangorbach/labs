f1 = open('LoremIpsum.txt', 'r+')
f2 = open('Lab5Text2.txt', 'w+')
symbol = str(input("symbol: "))
string = f1.readlines()

for i in range(len(string)):
    if string[i][0].upper() == symbol.upper():
        print(string[i])
        f2.write(string[i])
f1.close()
f2.close()