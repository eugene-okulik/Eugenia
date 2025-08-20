result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

# First Line
index1 = result1.index(':') + 2
print(int(result1[index1:]) + 10)

# Second line
index2 = result2.index(':') + 2
print(int(result2[index2:]) + 10)

# Third line
index3 = result3.index(':') + 2
print(int(result3[index3:]) + 10)
