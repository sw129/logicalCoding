
# Функция для перевода строки в десятичные числа
def GetString():
    # Запрашиваем у пользователя строку на русском
    s = input("Введите строку на русском: ")
    # Кодируем строку в windows-1251
    b = s.encode('windows-1251')

    # Создаем пустой список для хранения десятичных кодов
    codes = []

    # Проходим по каждому байту в закодированной строке
    for byte in b:
        # Применяем функцию ord, чтобы получить десятичный код байта
        code = byte
        # Добавляем код в список
        codes.append(code)

    # Выводим список десятичных кодов на экран
    print("Буквы: ", s)
    print("Десятичный код: ", codes)
    return codes

# Функция для перевода десятичного числа в двоичное
def decimal_to_binary(decimal):
    # Инициализируем пустую строку для результата
    result = ""
    # Пока десятичное число больше нуля
    while decimal > 0:
        # Делим его на 2 и записываем остаток от деления (0 или 1) в начало результата
        result = str(decimal % 2) + result
        # Делим частное от предыдущего деления нацело на 2 и присваиваем его десятичному числу
        decimal = decimal // 2
    # Возвращаем результат
    return result

def WordToCode():
    code = []
    for item in GetString():
        code += decimal_to_binary(item)
    code = list(map(int,code))
    print(f"Двоичный код: {code}")
    return code