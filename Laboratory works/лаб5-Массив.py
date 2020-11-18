my_numbers = list(map(int, input('Введите одномерный массив:').split()))
x = int(input('Введите один целое число:'))
z = max(my_numbers)

i = 0
while i < len(my_numbers):
    if my_numbers[i] == z:
        my_numbers.insert(i + 1, x)
        i += 2
    else:
        i += 1

print(my_numbers)



#Массивийн элментийг солих
numbers[3] = 'a'
print(numbers)

#Хуудсанд элемент нэмэх
numbers.append('7')
print(numbers)

numbers.insert(4,'b')
print(numbers)

#Хуудаснаас элемент хасах
del numbers[3]
print(numbers)
numbers.remove('b')
print(numbers)

#Массивийн элементүүдийн байрийг солих
numbers.reverse()
print(numbers)

my_numbers = list(map(int, input('Введите одномерный массив:').split()))
x = int(input('Введите один целое число:'))
z = max(my_numbers)

i = 0
while i < len(my_numbers):
    if my_numbers[i] == z:
        my_numbers.insert(i + 1, x)
        i += 2
    else:
        i += 1

print(my_numbers)
