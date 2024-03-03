![animation](https://github.com/MakarovDs777/Makarov-Compressor/assets/42496353/76f1a5ed-a3cf-469e-81b1-53b04cb9c09e)
# Посыл мысли
Не имеет значения то что мы считаем, а имеет значение то как мы это считаем, и для того что-бы сжимать, и разжимать данные мне не нужно их ни сжимать, ни разжимать мне достаточно просто сгенерировать файлы ведь любую информацию я могу превратить в последовательность чисел, и эту последовательнсоть чисел я могу превратить обратно в ту же самую информацию это мне напоминает тот мем с Катющиком про академическое суммирование, и континиум мерностей в пространстве- "Как посчитать количество мерностей в пространстве? Одна картошка, вторая картошка, три картошка, четыре штангенсциркуль, пять пассатижи, ну и т.д. (ссылка: https://youtu.be/l5oYbA8mQl4?si=n2Rf3kTZTxTzs_Po&t=182)". 

# ФУНДАМЕНТАЛИЗМ ПРОГРАММИСТОКОГО НАГУАЛИЗМА
Ну и как продолжение к предудший мысли так вот если подразумевает исходный код как некоторое паранормальное явление, и точку сборки в это паранормальном явлении исходного кода то по сути можно даже миллиаржы строчек исходного кода прогрузить как нечто одно целое

![Azat-Shub](https://github.com/MakarovDs777/Makarov-Compressor/assets/42496353/a5cb67b5-faa1-4518-bb8d-1f5631253fb5)

Скоро все допишу...

# Концепция компрессора Макарова
Как я уже и говорил ранее значения имеет то как мы считаем, и считать то мы на самом-то деле можем как угодно! А следовательно можно вычислить что угодно! Ну например можно же там допустим взять пистолет, и он выстрелит пулей, и пуля соберет нужные числа в своем полете расчитать траекторию движения пули мы можем, градус рикошета тоже, силу инерции пули можем соответсвенно весь путь траекторию движения пули а также место где она остановится тоже, ну и всё говно вопрос тогда! Чё там стоит написать геометрию пространства, и маяки в пространстве в которые попадает пуля... Это всё можно сделать двумя переменными, и если понадобится можно вообще превратить в одну... Но а теперь немного предистории... Поначалу у меня была идея написать функцию f(x) с двумя волнистыми я поискал в интернете и нашел такое определенние как интерполяционный многочлен Лагранжа, но потом я понял что это бессмысленная затея, и я начал искать дальше и нашел такую штуку как Архимедовые спирали, и хоть у Архимеда не то что компьютера - миллиметровки не было, то у меня была идея написать две спирали Архимеда они попадают на отрезок оси асцисс одна спираль собирает отклонения в одну сторону а другая в противоположну, и установиив взаимозавиисиомсть двух спиралей я бы смог собрать любую нужную мне последовательность чисел но потом я в принципе подумал спирали Архимеда то даже и не нужны. Достаточно просто иметь отрезок N длины, и кривую тупо запульнуть на полярной системы координат и при каждой последующей итерации она будет на какое-то число градусов тета отклоняться типа массив и там есть значения отклонений при каждой последующей итерации расстояния кривой на которую она отклоняется [20%, -5%, etc...] на какое-то значение таким образом попадая на отрезке в нужные числа массива. И когда она заканчивается она начинается считать с начала массива, и всё вообще можно не париться в принципе... Самого количества чисел отклонений тета не так много нужно что-бы выстроить нужную траекторию. А подумал и понял что в принципе можно вторую кривую такую же сделать и просто запереть её в какую нибудь геометрическую фигуру типа круга, или другой геометрической фигурой, и даже просто менять эту геометрическую фигуру при каждой последующей итерации, и разделить эту геометрическую фигуру на отрезки значений градусов тета, и когда она будет попадать на отрезки круга то будет вносить значение этого отрезка градуса тета в отклонение итерации первой кривой, и рикошетить к следующей нужной итерации для отклонения на то количество градусов для которого нужно попасть первой кривой на отрезок что-бы выдать нужное следующие число в массиве N чисел. Или как вариант можно это делать в трехмерном пространстве создать 3-x мерную фигуру разделив её на отрезки значений, выстрелить пулей, и заставить фигуру вращаться с какой нибудь скорость типа постоянной или переменной по какой нибудь траектории типа вперед-назад, влево ~ вправо, и сопоставив скорость ~ траекторию движения пули изначально, скорость ~ траекторию ~ движение фигуры, и градус рикошета пули при столкновении можно вычислить в какие отрезки фигуры она попадет, и найти нужные неизвестные переменные которые выдадут любые нужные числа. Чем тоже не вариант!? Вообщем есть к чему стремиться...

# MakarovCompressor
Основная идея программы заключается в использовании библиотеки matplotlib для визуализации геометрической фигуры на полярных координатах. В первой функции create_geometric_shape создается фигура на основе переданного массива чисел, разделенная на отрезки с помощью функции plot. Затем она возвращает радиус r, угол theta и переменную fig, представляющую собой созданную геометрическую фигуру.

Во второй функции get_numbers_from_geometric_shape мы получаем объекты линий из созданной фигуры, получаем метки (номера) каждой линии, и возвращаем массив чисел. Эта функция принимает радиус r, угол theta и переменную fig, возвращаемую из первой функции.

В приведенном примере массив чисел [2, 4, 3, 1, 5] подается на вход первой функции, строится геометрическая фигура и сохраняется радиус r, угол theta и переменная fig. Затем вызывается вторая функция, которая извлекает массив чисел из геометрической фигуры. Полученный результат [2, 4, 3, 1, 5] выводится на экран.

# MakarovCompressorApplication

Данный код представляет собой простое приложение GUI (графического интерфейса пользователя) на основе библиотеки Tkinter в Python. Вот краткое описание этого кода:

1. **Импорт библиотек**:
   - tkinter - для создания графического интерфейса.
   - matplotlib.pyplot и numpy - для построения графиков.

2. **Класс App**:
   - Этот класс представляет главное окно приложения.
   - В конструкторе инициализируется главное окно с названием "Makarov Compressor" и размером 450x350 пикселей.
   - Добавляется метка (Label) и кнопка (Button), которая при нажатии вызывает метод button_clicked.

3. **Класс MenuBar**:
   - Этот класс представляет меню приложения.
   - В конструкторе создаются два пункта меню: "Сгенерировать текст" и "Создать ключ", каждый с соответствующими подпунктами.
   - Методы generate_text и create_key вызываются при выборе соответствующих опций в меню.

4. **Методы generate_text и create_key**:
   - Эти методы создают новые окна для ввода данных и генерации текста или создания ключа соответственно.
   - После ввода данных и нажатия кнопки "Отправить", данные записываются в текстовый файл или обрабатываются для создания ключа.

5. **Метод create_geometric_shape**:
   - Этот метод создает геометрическую фигуру на основе входных чисел.
   - Он использует библиотеку matplotlib для построения графика сегментов с заданными значениями.
   - Значения радиусов и углов вычисляются на основе входных чисел.

6. **Основной блок**:
   - В основном блоке кода создается экземпляр класса App, после чего запускается главный цикл обработки событий (mainloop) для отображения приложения.

Этот код создает простое приложение с GUI, которое позволяет пользователю генерировать текст или создавать ключи, а также визуализировать геометрические фигуры на основе введенных данных.

# CodePen
Данный код разделяет текст на массив символов, и массив с массивами всех индексов всех символов массива, и превратив это в единый массив по нему создать обратно массив с массивами по которому обратно создать тот самый текст обратно. 
