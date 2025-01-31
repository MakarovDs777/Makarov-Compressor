"""import tkinter as tk
from tkinter import messagebox
import os
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("Makarov Compressor")
        self.geometry("450x350")

        # Настройка формы
        self.mode_frame = self.create_mode_frame()
        self.mode_frame.pack(expand=True)

    def create_mode_frame(self):
        frame = tk.Frame(self)

        # Метки для полей ввода
        r_label = tk.Label(frame, text="Введите r:")
        r_label.pack(pady=5, anchor='w')

        self.r_var = tk.StringVar()
        self.r_entry = tk.Entry(frame, textvariable=self.r_var, width=30)
        self.r_entry.pack(pady=5)

        theta_label = tk.Label(frame, text="Введите theta:")
        theta_label.pack(pady=5, anchor='w')

        self.theta_var = tk.StringVar()
        self.theta_entry = tk.Entry(frame, textvariable=self.theta_var, width=30)
        self.theta_entry.pack(pady=5)

        fig_label = tk.Label(frame, text="Введите fig (по умолчанию 640x480):")
        fig_label.pack(pady=5, anchor='w')

        self.fig_var = tk.StringVar(value='640,480')  # Установка значения по умолчанию
        self.fig_entry = tk.Entry(frame, textvariable=self.fig_var, width=30)
        self.fig_entry.pack(pady=5)

        self.submit_btn = tk.Button(frame, text="Сгенерировать график и сохранить текст", command=self.generate_graph)
        self.submit_btn.pack(pady=10)

        return frame

    def create_geometric_shape(self, numbers):
        num_segments = len(numbers)
        angles = np.linspace(0, 2 * np.pi, num_segments + 1)[:-1]
        radii = np.array(numbers) * 10

        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

        for i in range(num_segments):
            ax.plot([angles[i], angles[i]], [0, radii[i]], label=str(numbers[i]))

        plt.legend()
        plt.show()

        return fig

    def get_numbers_from_geometric_shape(self, fig):
        ax = fig.gca()
        lines = ax.get_lines()

        numbers = []
        for line in lines:
            label = line.get_label()
            if label:
                numbers.append(float(label))

        return numbers

    def generate_graph(self):
        try:
            r_input = self.r_var.get()
            theta_input = self.theta_var.get()

            print(f"Ввод r: {r_input}, theta: {theta_input}")

            r = float(r_input)
            theta = float(theta_input)

            fig_dimensions = self.fig_var.get().split(',')
            width, height = (640, 480) if len(fig_dimensions) < 2 else map(int, fig_dimensions)

            numbers = [r, theta]

            fig = self.create_geometric_shape(numbers)
            result_numbers = self.get_numbers_from_geometric_shape(fig)

            result_text = self.process_codepen_style(result_numbers)
            self.save_text_file(result_text)

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Пожалуйста, вводите корректные числовые значения для r и theta.\n{e}")

    def process_codepen_style(self, numbers):
        text = ''.join([str(num) for num in numbers])
        symbols, indexes = self.get_indexes(text)

        # Обработка JackBack
        JackBack = [ord(ch) for ch in symbols] + [len(text) + 1] + indexes

        # Отдельная обработка индексов
        BackJackSymbols = JackBack[:len(symbols)]
        BackJackIndexes = JackBack[len(symbols)+1:]

        return self.get_text_from_symbol_and_index_arrays(BackJackSymbols, BackJackIndexes)

    def get_indexes(self, text):
        chars = list(set(text))
        indexes = []
        for char in chars:
            indexes.append([i for i, c in enumerate(text) if c == char])
        return chars, indexes

    def get_text_from_symbol_and_index_arrays(self, symbols, indexes):
        max_index = max(max(idx) for idx in indexes if idx) if indexes else 0
        result = [''] * (max_index + 1)  # Создаём список длиной равной макс. индексу

        for symbol, symbol_indexes in zip(symbols, indexes):
            for index in symbol_indexes:
                if index < len(result):  # Проверяем, что индекс в пределах
                    result[index] = str(symbol)  # Убеждаемся, что символ является строкой

        return ''.join(result)  # Объединяем только строковые элементы

    def save_text_file(self, content):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "сгенерированный_текст.txt")

        with open(file_path, "w") as file:
            file.write(content)

        messagebox.showinfo("Готово", "Файл успешно сохранён на рабочем столе!")

if __name__ == "__main__":
    app = App()
    app.mainloop()"""

import tkinter as tk
from tkinter import messagebox
import os
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from ast import literal_eval

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.title("Makarov Compressor")
        self.geometry("450x350")

        # Настройка формы
        self.mode_frame = self.create_mode_frame()
        self.mode_frame.pack(expand=True)

    def create_mode_frame(self):
        frame = tk.Frame(self)

        # Метки для полей ввода
        r_label = tk.Label(frame, text="Введите r:")
        r_label.pack(pady=5, anchor='w')

        self.r_var = tk.StringVar()
        self.r_entry = tk.Entry(frame, textvariable=self.r_var, width=30)
        self.r_entry.pack(pady=5)

        theta_label = tk.Label(frame, text="Введите theta:")
        theta_label.pack(pady=5, anchor='w')

        self.theta_var = tk.StringVar()
        self.theta_entry = tk.Entry(frame, textvariable=self.theta_var, width=30)
        self.theta_entry.pack(pady=5)

        fig_label = tk.Label(frame, text="Введите fig (по умолчанию 640x480):")
        fig_label.pack(pady=5, anchor='w')

        self.fig_var = tk.StringVar(value='640,480')  # Установка значения по умолчанию
        self.fig_entry = tk.Entry(frame, textvariable=self.fig_var, width=30)
        self.fig_entry.pack(pady=5)

        self.submit_btn = tk.Button(frame, text="Сгенерировать график и сохранить текст", command=self.generate_graph)
        self.submit_btn.pack(pady=10)

        return frame

    def create_geometric_shape(self, numbers):
        num_segments = len(numbers)
        angles = np.linspace(0, 2 * np.pi, num_segments + 1)[:-1]
        radii = np.array(numbers) * 10

        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)

        for i in range(num_segments):
            ax.plot([angles[i], angles[i]], [0, radii[i]], label=str(numbers[i]))

        plt.legend()
        plt.show()

        return fig

    def get_numbers_from_geometric_shape(self, fig):
        ax = fig.gca()
        lines = ax.get_lines()

        numbers = []
        for line in lines:
            label = line.get_label()
            if label:
                numbers.append(float(label))

        return numbers

    def generate_graph(self):
        try:
            r_input = self.r_var.get()
            theta_input = self.theta_var.get()

            print(f"Ввод r: {r_input}, theta: {theta_input}")

            r = float(r_input)
            theta = float(theta_input)

            fig_dimensions = self.fig_var.get().split(',')
            width, height = (640, 480) if len(fig_dimensions) < 2 else map(int, fig_dimensions)

            numbers = [r, theta]

            fig = self.create_geometric_shape(numbers)
            result_numbers = self.get_numbers_from_geometric_shape(fig)

            result_text = self.process_codepen_style(result_numbers)
            self.save_text_file(result_text)

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Пожалуйста, вводите корректные числовые значения для r и theta.\n{e}")

    def get_indexes(self, text):
        chars = list(set(text))
        indexes = []
        for char in chars:
            indexes.append([i for i, c in enumerate(text) if c == char])
        return chars, indexes

    def process_codepen_style(self, numbers):
        text = ''.join([str(num) for num in numbers])
        symbols, indexes = self.get_indexes(text)
        
        # Формируем JackBack
        JackBack = str([ord(xxx) for xxx in symbols] + [(max(indexes)[0]) + 1] + indexes).replace('], [', ', ' + str((max(indexes)[0]) + 1) + ', ')
        JackBack = "[" + str(JackBack[1:len(JackBack) - 1]).replace("[", "").replace("]", "") + "]"
        BackJack = literal_eval("[" + JackBack.replace(str((max(indexes)[0]) + 1), "], [").replace(", ], [, ", "], [").replace(", [], [, ", "], [") + "]")
        BackJackSymbols = [chr(xxxx) for xxxx in BackJack[0]]

        return self.get_text_from_symbol_and_index_arrays(BackJackSymbols, BackJack[1:])

    def get_text_from_symbol_and_index_arrays(self, symbols, indexes):
        result = ['' for _ in range(max(chain.from_iterable(indexes)) + 1)]
        for symbol, symbol_indexes in zip(symbols, indexes):
            for index in symbol_indexes:
                result[index] = symbol
        return ''.join(result)

    def save_text_file(self, content):
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, "сгенерированный_текст.txt")

        with open(file_path, "w") as file:
            file.write(content)

        messagebox.showinfo("Готово", "Файл успешно сохранён на рабочем столе!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
