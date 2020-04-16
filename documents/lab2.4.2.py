from random import randint as random
numbers = [random(1, 100) for i in range(int(input("some len: ")))]
print(numbers)
file1 = open("lab4file3.txt", "w+")
for i in range(len(numbers)):
    file1.write(str(numbers[i])+str(" "))
file1.close()

list = []
list2 = []
num = str("")
file1 = open("lab4file3.txt", "r+")
file2 = open("lab4file4.txt", "w+")
strF = str(file1.read())

for i in strF:
    if i != (" "):
        num += i
    elif i == (" "):
        list.append(int(num))
        num = ""
print(list)

unique = set(strF)
for i in unique:
    if i == " ":
        continue
    else:
        list2.append(i)
print(list2)
list2.reverse()
print(list2)

for i in list2:
    file2.write(str(i) + str(" "))