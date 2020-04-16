f = open("LoremIpsum.txt", 'r+')
word1 = str(f.read())
f.close()
symbol = input("input your symbol: ")
n = 0
for i in word1:
    if i == symbol:
        n += 1
print(word1)
print("\nдлинна текста: ", len(word1), "символов")
print("количество повторений символа ", str("'") + str(symbol) + str("'") + str(":"), n)
n = round((100/float(len((word1))))*n, 2)
print(n,"%")

