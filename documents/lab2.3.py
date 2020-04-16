def task1(symbol):
     n = 0
     word = str("GNALSGKBJIPSBISDJBSNB")
     word2 = str("")
     word3 = word[0]
     print(word)
     word = word.replace(symbol,"")
     print(word)
     for i in range(len(word)):
         word2 += word[i]*2
     print(word2)
     for i in range(len(word)):
         for j in range(len(word3)):
             if word[i] != word3[j]:
                 n += 1
         if n == (len(word3)):
             word3 += word[i]
         n = 0
     print("Количество всех символов: ", len(word))
     print("Количество уникальных символов: ", len(word3))
     print(word3)

 task1(str(A))