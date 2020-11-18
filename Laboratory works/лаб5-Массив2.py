my_numbers = list(map(int, input('Введите одномерный массив:').split()))
a = my_numbers[0]
for i in range(len(my_numbers)):
    if my_numbers[i] > 0:
        count = 1
        while i + count < len(my_numbers):
            del my_numbers[i+count]
            count += 1
        break
print(my_numbers)

