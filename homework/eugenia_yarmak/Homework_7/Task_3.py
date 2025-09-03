def result_line(line):
    get_num = int(line.split()[-1]) + 10
    return get_num


print(result_line("результат операции: 42"))
print(result_line("результат операции: 54"))
print(result_line("результат работы программы: 209"))
print(result_line("результат: 42"))
