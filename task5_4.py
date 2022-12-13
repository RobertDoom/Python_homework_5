#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('task5_4data.txt', 'r') as datafile:
    my_text = ''.join(line.strip() for line in datafile)

temp_str, result_str = my_text[0], ''
i = 0

for dchar in my_text:
    if dchar != temp_str[-1]:
        result_str += str(i) + temp_str[-1]
        i = 1
        temp_str = dchar
    else:
        i += 1
        temp_str += dchar
result_str += str(i) + temp_str[-1]

with open('task5_4data.txt', 'w') as datafile:
    datafile.writelines(result_str)

with open('task5_4data.txt', 'r') as datafile:
    my_text2 = ''.join(line.strip() for line in datafile)
result_str = ''
for dchar in my_text2:
    if dchar.isalpha():
        pchar = my_text2.index(dchar)
        num = int(my_text2[0:pchar])
        result_str += dchar * num
        my_text2 = my_text2[pchar + 1:]

with open('task5_4result.txt', 'w') as datafile:
    datafile.writelines(result_str)