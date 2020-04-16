from random import randint as random
numbers = [random(-100, 100) for i in range(int(input("some len: ")))]
print(numbers)
file1 = open("lab4file1.txt", "w+")
for i in range(len(numbers)):
    file1.write(str(numbers[i])+str(" "))
file1.close()

f = open("lab4file1.txt", "r+")
f1 = open("lab4file2.txt", "w+")

strF = str(f.read())
list = []
num = str("")
n = int(input("введите кратное число: "))

for i in strF:
    if i != (" "):
        num += i
    elif i == (" "):
        list.append(int(num))
        num = ""
print(list)

for i in range(len(list)):
    if list[i]%n == 0:
        f1.write(str(list[i]) + str(" "))

f.close()
f1.close()

