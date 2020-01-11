# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется
# столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов
# последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел
# в одну строку.
#
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

input_number = int(input())
counter = 1
digit = 1
initial_string = ''

while counter <= input_number:
    initial_string += (str(digit)+' ')*digit
    counter += digit
    digit += 1

srt_without_last_space = initial_string[:-1]
list_of_nums = srt_without_last_space.split(' ')
cropped_list = list_of_nums[0:input_number]
result = ' '.join(cropped_list)

print(result)


# the most elegant:
n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])
