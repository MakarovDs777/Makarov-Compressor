'''
import tkinter as tk
from tkinter import ttk, Menu
from tkinter.messagebox import showinfo
import os
import sys
import matplotlib.pyplot as plt
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # настройте корневое окно
        self.title("Makarov Compressor")
        self.geometry("450x350")

        p1 = tk.PhotoImage(file='Compressor.png')
        self.iconphoto(False, p1)

        self.config(menu=MenuBar(self))

        # label
        self.label = ttk.Label(self, text="Информация")
        self.label.pack()

        # button
        self.button = ttk.Button(self, text="кликни меня")
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        showinfo(title="Информация", message="Компрессор Макарова - это приложение, которое позволяет сгенерировать текст или создать ключ.")

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        filemenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Сгенерировать текст", underline=0, menu=filemenu)
        filemenu.add_command(label="Новый текст", command=self.generate_text)

        helpmenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Создать ключ", menu=helpmenu)
        helpmenu.add_command(label="Выдать ключ", command=self.create_key)

    def generate_text(self):
        # Создайте новое окно для генерации текста
        self.new_window = tk.Toplevel(self)
        self.new_window.title("Генерировать текст")
        self.new_window.geometry("350x250")

        p22 = tk.PhotoImage(file='Compressor.png')
        self.new_window.iconphoto(False, p22)

        # Создание полей ввода
        self.r_label = ttk.Label(self.new_window, text="r:")
        self.r_label.pack()
        self.r_entry = ttk.Entry(self.new_window)
        self.r_entry.pack()

        self.theta_label = ttk.Label(self.new_window, text="theta:")
        self.theta_label.pack()
        self.theta_entry = ttk.Entry(self.new_window)
        self.theta_entry.pack()

        self.fig_label = ttk.Label(self.new_window, text="fig:")
        self.fig_label.pack()
        self.fig_entry = ttk.Entry(self.new_window)
        self.fig_entry.pack()

        # Создать кнопку отправки
        self.submit_button = ttk.Button(self.new_window, text="Отправить", command=self.generate_text_file)
        self.submit_button.pack()

    def generate_text_file(self):
        r = self.r_entry.get()
        theta = self.theta_entry.get()
        fig = self.fig_entry.get()

        # Создайте папку на рабочем столе
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_path = os.path.join(desktop_path, "Сгенерированный файл")
        os.makedirs(folder_path, exist_ok=True)

        # Создайте текстовый файл с входными значениями
        file_path = os.path.join(folder_path, "generated_text.txt")
        with open(file_path, "w") as file:
            file.write(f"r: {r}\n")
            file.write(f"theta: {theta}\n")
            file.write(f"fig: {fig}\n")

        showinfo(title="Информация", message="Текстовый файл успешно создан.")

    def create_key(self):
        # Создайте новое окно для создания ключа
        self.new_window = tk.Toplevel(self)
        self.new_window.title("Создание ключа")
        self.new_window.geometry("350x250")

        p11 = tk.PhotoImage(file='Compressor.png')
        self.new_window.iconphoto(False, p11)

        # Создать поле ввода файла
        self.file_label = ttk.Label(self.new_window, text="Выберите файл:")
        self.file_label.pack()
        self.file_entry = ttk.Entry(self.new_window)
        self.file_entry.pack()

        # Создать кнопку отправки
        self.submit_button = ttk.Button(self.new_window, text="Отправить", command=self.create_key_from_file)
        self.submit_button.pack()

    def create_key_from_file(self):
        file_path = self.file_entry.get()

        # Проверьте, существует ли файл
        if not os.path.isfile(file_path):
            showinfo(title="Ошибка!", message="Файл не найден.")
            return

        # Прочитайте файл и извлеките значения
        with open(file_path, "r") as file:
            lines = file.readlines()
            values = [line.strip().split(":")[1].strip() for line in lines]

        # Создайте геометрическую фигуру, используя значения переменных
        numbers = [int(value) for value in values]
        r, theta, fig = create_geometric_shape(numbers)

        # Отобразите клавиши
        showinfo(title="Keys", message=f"r: {r}\ntheta: {theta}\nfig: {fig}")

def create_geometric_shape(numbers):
    num_segments = len(numbers)
    angles = np.linspace(0, 2*np.pi, num_segments+1)[:-1]  # равномерно распределите углы
    radii = np.array(numbers) * 10  # масштабируйте числа, чтобы определить радиусы сегментов

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    # Нарисуйте сегменты с цифрами
    for i in range(num_segments):
        ax.plot([angles[i], angles[i]], [0, radii[i]], label=str(numbers[i]))

    # Установите радиус и угол так, чтобы они соответствовали последнему сегменту
    r = radii[-1] / 2
    theta = angles[-1] + np.pi/2

    plt.legend()
    plt.show()

    return r, theta, fig

if __name__ == "__main__":
    app = App()
    app.mainloop()
    exit(0)'''
import tkinter as tk
import PyPDF2
import os
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, asksaveasfile
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
from ast import literal_eval

root = tk.Tk()
root.title("Makarov Compressor")
root.geometry("650x900")
root.iconbitmap("F:\EVP-Spaces\PDFextract_text-main\PDFextract_text-main\starterFiles\logo.png")
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logo
logo = Image.open('F:\EVP-Spaces\PDFextract_text-main\PDFextract_text-main\starterFiles\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Выберите текстовый файл на вашем компьютере для обработки", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='r', title="Choose a file", filetypes=[("Text file", "*.txt")])
    if file:
        text = file.read()
        text_box.delete(1.0, tk.END)
        text_box.insert(1.0, text)
        browse_text.set("Browse")

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
    return ''.join(result)

def save_sequence_numbers():
    text = text_box.get(1.0, tk.END).strip()
    symbols, indexes = get_indexes(text)
    JackBack = str([ord(xxx) for xxx in symbols] + [(max(indexes)[0]) + 1] + indexes).replace('], [', ', ' + str((max(indexes)[0]) + 1) + ", ")
    JackBack = "[" + str(JackBack[1:len(JackBack) - 1]).replace("[", "").replace("]", "") + "]"
    BackJack = literal_eval("[" + JackBack.replace(str((max(indexes)[0]) + 1), "], [").replace(", ], [, ","], [").replace(", [], [,","], [").replace("]], [ ","], [") + "]")
    BackJackSymbols = [chr(xxxx) for xxxx in BackJack[0]]
    sequence_numbers = get_text_from_symbol_and_index_arrays(BackJackSymbols, BackJack[1:])

    with asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text file", "*.txt")], initialfile="SequenceNumbers.txt") as file:
        if file:
            file.write(sequence_numbers)

def create_geometric_shape(numbers):
    num_segments = len(numbers)
    angles = np.linspace(0, 2 * np.pi, num_segments + 1)[:-1]
    radii = np.array(numbers) * 10

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    for i in range(num_segments):
        ax.plot([angles[i], angles[i]], [0, radii[i]], label=str(numbers[i]))

    r = radii[-1] / 2
    theta = angles[-1] + np.pi / 2

    plt.legend()
    plt.savefig("generated_key.png", bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)

    return r, theta

def get_numbers_from_geometric_shape(r, theta, fig):
    img = plt.imread("generated_key.png")
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')

    lines = ax.get_lines()

    numbers = []
    for line in lines:
        label = line.get_label()
        if label:
            numbers.append(int(label))

    return numbers

def generate_key():
    sequence_numbers = text_box.get(1.0, tk.END).strip()
    numbers = [ord(x) for x in sequence_numbers]
    r, theta, fig = create_geometric_shape(numbers)
    with asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text file", "*.txt")], initialfile="GeneratedKey.txt") as file:
        if file:
            file.write(f"r: {r}\ntheta: {theta}\nfig: {fig}")

def generate_text():
    key_file = askopenfile(parent=root, mode='r', title="Choose a key file", filetypes=[("Text file", "*.txt")])
    if key_file:
        lines = key_file.readlines()
        r, theta = map(float, (lines[0].strip().split(': ')[1], lines[1].strip().split(': ')[1]))
        numbers = get_numbers_from_geometric_shape(r, theta, None)
        generated_text = get_text_from_symbol_and_index_arrays([chr(x) for x in numbers], ([i] for i, _ in enumerate(numbers)))
        with asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text file", "*.txt")], initialfile="GeneratedText.txt") as file:
            if file:
                file.write(generated_text)

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

# save sequence numbers button
save_btn = tk.Button(root, text="Save Sequence Numbers", command=lambda: save_sequence_numbers(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
save_btn.grid(column=1, row=3, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

# generate key button
generate_key_btn = tk.Button(root, text="Generate Key", command=lambda: generate_key(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
generate_key_btn.grid(column=1, row=4, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

# generate text button
generate_text_btn = tk.Button(root, text="Generate Text", command=lambda: generate_text(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
generate_text_btn.grid(column=1, row=5, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

# text box
text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
text_box.grid(column=1, row=6, padx=10, pady=10, sticky=tk.N + tk.S + tk.E + tk.W)

root.mainloop()
