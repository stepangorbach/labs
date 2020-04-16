from random import randint as random
def show(x):
    max_len = max([len(str(e)) for r in x for e in r])
    for row in x:
        print(*list(map('{{:>{length}}}'.format(length=max_len).format, row)))

def transpose(matr):
    res=[]
    n=len(matr)
    m=len(matr[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matr[i][j]]
        res=res+[tmp]
    return res

def task1(long):
    list = [random(-100, 100) for i in range(long)]; print(list)
    list.sort(reverse = True); print(list)
    print("\n")
task1(5)

def sort2(x):
    matrix = [[random(0,100) for i in range(x)] for i in range(x)]
    m = 0; a1 = 0; a2 = 0; id = 0
    mList = 0; aList = 0
    show(matrix)
    matrix = transpose(matrix)
    #print("\n")
    #show(matrix)
    for i in range(x):
        m = matrix[i][0]
        mList = matrix[i]
        for j in range(i, x):
            a1 = matrix[j][0]
            if m <= a1 and a1 >= a2:
                a2 = a1
                aList = matrix[j]
                id = j
        matrix[i] = aList
        matrix[id] = mList
        a1 = 0; a2 = 0
    #print("\n")
    #show(matrix)
    matrix = transpose(matrix)
    print("\n")
    show(matrix)
sort2(5)
    
            
        
