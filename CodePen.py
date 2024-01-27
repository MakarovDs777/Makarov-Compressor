from itertools import chain
from ast import literal_eval

text = """import random
g = random.randint(0,4)
if g == 0:
    print("Kotyk")
if g == 1:
    print("Motyk")   
if g == 2:
    print("Kotopes")     
if g == 3:
    print("Borbies")     
"""

def get_indexes(text):
    chars = list(set(text))
    indexes = []
    for char in chars:
        indexes.append([i for i, c in enumerate(text) if c == char])
    return chars, indexes

def get_text_from_symbol_and_index_arrays(symbols, indexes):
    result = ['' for _ in range(max(chain.from_iterable(indexes)) + 1)]
    for symbol, symbol_indexes in zip(symbols, indexes):
        for index in symbol_indexes:
            result[index] = symbol
    print(''.join(result))
    
symbols, indexes = get_indexes(text)
#print(symbols, indexes)
# Добавляет массив с символами в массив с массивами индексов всех символов, и превращает их в один массив
JackBack=str([ord(xxx) for xxx in symbols]+[(max(indexes)[0])+1]+indexes).replace('], [',', '+str((max(indexes)[0])+1)+", ")
# Превращает массив с массивами в просто массив
JackBack="["+str(JackBack[1:len(JackBack)-1]).replace("[","").replace("]","")+"]"
# Превращает просто массив обратно в массив с массивами
BackJack=literal_eval("["+JackBack.replace(str((max(indexes)[0])+1), "], [").replace(", ], [, ","], [").replace(", [], [,","], [").replace("]], [ ","], [")+"]")
BackJackSymbols=[chr(xxxx) for xxxx in BackJack[0]]
#print(BackJack)
get_text_from_symbol_and_index_arrays(BackJackSymbols, BackJack[1:])
