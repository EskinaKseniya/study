'''
Дана база данных о продажах некоторого интернет магазина. 
Каждая строка входного файла представляет собой запись вида:
покупатель товар кол-во
где Покупатель - имя покупателя (строка без пробелов),
товар - название товара (строка без пробелов),
кол-во - кол-во приобретенных единиц товара.
Создайте список всех покупателей, а для каждого покупателя
подсчитайте кол-во приобретенных им единиц каждого вида товаров.

'''
file = open('open.txt')
usersDictionary = {}
str = ""
while True : # цикл прохода по файлику
    productsDictionary = {}
    str = file.readline()
    date = str.split() # список, в котором date[0] - фамилия покупателя, date[1] - товар, date[2] - кол-во товара
    if not str : # условие выхода из цикла (прочли весь файл)
        break
    if not (date[0] in usersDictionary) : # если такого покупателя еще не было
       productsDictionary[date[1]] = date[2] # заполняем словарь продуктов
       usersDictionary[date[0]] = productsDictionary # кладем в значение словаря пользователей словарь продуктов

    else :
        if not (date[1] in usersDictionary[date[0]].keys()) : # если такой покупатель есть, но товара нет
            productsDictionary[date[1]] = date[2]
            usersDictionary[date[0]].update(productsDictionary) # добавляем еще одну пару ключ-значение в значение словаря пользователей
        else : # если такой покупатель есть и товар есть
            productsDictionary[date[1]] = int(date[2]) + int(usersDictionary[date[0]][date[1]]) # складываем кол-во одного и того же товара
            del(usersDictionary[date[0]][date[1]]) # удаляем старые ключ значение
            usersDictionary[date[0]].update(productsDictionary) # добвавляем новые ключ значение
file.close()
usersDictionary = dict(sorted(usersDictionary.items())) #сортирую словарь по ключам -> получаю список кортежей -> преобразовываю его в словарь с помощью dict()
for key, value in usersDictionary.items() :
    print(f"{key}:")
    value = dict(sorted(value.items()))
    for key1, value1 in value.items() :

        print(f"{key1} {value1}")

