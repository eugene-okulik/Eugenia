hidden_number = 13

while True:
    user_input = int(input("Введите число от 1 до 20 (или 0 для выхода): "))
    if user_input == hidden_number:
        print("Поздравляю! Вы угадали!")
        break
    elif user_input == 0:
        print("Пока!")
        break
    else:
        print("Попробуйте снова")
hidden_number = 13
