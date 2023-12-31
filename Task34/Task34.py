# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова. Если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам  

arrayAmountSyllables = [] # массив количества слогов во фразе, каждому элементу массива frazesArray соответствует элемент массива количества слогов
currentNumberOfSyllables = int() # текущее значение количества слогов
vowels = ['А','а','Е','е','Ё','ё','И','и','О','о','У','у','Ы','ы','Э','э','Ю','ю','Я','я'] # словарь гласных букв

poem = input(f'Введите набор фраз (слова разделяются дефисами, фразы разделяются пробелами)\n')
k = int(0)
currentNumberOfSyllables = 0
# цикл по всему набору фраз с формированием массива количества слогов
while (k<len(poem)): # цикл по всему набору фраз
    if (poem[k] == ' '): 
       arrayAmountSyllables.append(currentNumberOfSyllables)
       currentNumberOfSyllables = 0 
    else:
        for j in range(0,len(vowels)-1): # проверка текущего символа на гласную
            if (poem[k] == vowels[j]):
                currentNumberOfSyllables += 1
    k += 1
arrayAmountSyllables.append(currentNumberOfSyllables) # присоединение количества слогов в последней фразе
flagIsRhythm = bool(True) # флаг наличия ритма во фразе
# цикл проверки равенства количества слогов во фразах
for i in range(1,len(arrayAmountSyllables)):
    if (arrayAmountSyllables[i-1] != arrayAmountSyllables[i]):
        flagIsRhythm = False
        break
#print(arrayAmountSyllables)
#print(flagIsRhythm)
if flagIsRhythm:
    print(f'Парам пам-пам')
else:
    print(f'Пам парам')

