from ast import literal_eval
from itertools import chain

# Пример преобразованного массива JackBack
JackBack = "[32, 50, 112, 51, 77, 114, 105, 98, 111, 110, 116, 48, 115, 46, 107, 41, 101, 10, 109, 52, 97, 34, 121, 61, 102, 40, 103, 44, 75, 58, 100, 49, 66, 164, 6, 15, 17, 40, 42, 45, 49, 50, 51, 52, 70, 72, 75, 79, 80, 81, 82, 97, 98, 99, 103, 105, 108, 112, 113, 114, 115, 132, 133, 134, 135, 136, 140, 142, 145, 149, 150, 151, 152, 169, 170, 171, 172, 173, 164, 109, 164, 2, 53, 83, 116, 127, 153, 164, 146, 164, 90, 164, 4, 7, 18, 25, 54, 84, 117, 154, 162, 164, 0, 29, 38, 55, 68, 85, 101, 118, 138, 155, 164, 164, 163, 164, 3, 11, 22, 61, 91, 124, 126, 161, 164, 9, 20, 27, 30, 56, 86, 119, 156, 164, 5, 31, 57, 62, 87, 92, 120, 125, 157, 164, 33, 46, 164, 129, 166, 164, 24, 164, 64, 94, 164, 36, 66, 96, 131, 168, 164, 128, 165, 164, 13, 37, 48, 67, 78, 100, 111, 137, 148, 174, 164, 1, 12, 23, 164, 35, 164, 8, 19, 26, 164, 59, 65, 89, 95, 122, 130, 159, 167, 164, 63, 93, 164, 16, 43, 44, 73, 74, 106, 107, 143, 144, 164, 39, 69, 102, 139, 164, 32, 58, 88, 121, 158, 164, 14, 41, 71, 104, 141, 164, 34, 164, 60, 123, 164, 47, 77, 110, 147, 164, 10, 21, 28, 164, 76, 164, 160]"

# Преобразование JackBack из строки в список чисел
JackBackList = literal_eval(JackBack)

# Найдем максимальный индекс, который будет служить маркером
sdf = max(JackBackList)-10   # Например, как в ваших данных, замените на max(JackBackList)

# Преобразуем JackBackList в строку и разделим по sdf
JackBack_str = str(JackBackList)
BackJack = literal_eval("[" + JackBack_str.replace(str(sdf), "], [").replace(", ], [, ","], [").replace(", [], [,","], [").replace("]], [ ","], [")+"]")
print(BackJack)
# Получение символов обратно из их кодов
BackJackSymbols = [chr(xxxx) for xxxx in BackJack[0]]

def get_text_from_symbol_and_index_arrays(symbols, indexes):
    result = ['' for _ in range(max(chain.from_iterable(indexes)) + 1)]
    for symbol, symbol_indexes in zip(symbols, indexes):
        for index in symbol_indexes:
            result[index] = symbol
    print(''.join(result))

get_text_from_symbol_and_index_arrays(BackJackSymbols, BackJack[1:])
