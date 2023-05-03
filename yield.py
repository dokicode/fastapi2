# Код на Python3 для демонстрации
# использования ключевого слова yield
 
# генерация нового списка, состоящего
# только из четных чисел
def get_even(list_of_nums) :
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
 
# инициализация списка
list_of_nums = [1, 2, 3, 8, 15, 42]
 
# вывод начального списка
print ("До фильтрации в генераторе: " +  str(list_of_nums))
 
# вывод только четных значений из списка
print ("Только четные числа: ", end = " ")
# for i in get_even(list_of_nums):
#     print (i, end = " ")

aaa = get_even(list_of_nums)
# print(aaa.__next__())
# print(aaa.__next__())
# print(aaa.__next__())
print(next(aaa))
print(next(aaa))
print(next(aaa))
print(next(aaa))