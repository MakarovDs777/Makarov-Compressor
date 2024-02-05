
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
        self.submit_button = ttk.Button(self.new_window, text="Submit", command=self.generate_text_file)
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
    exit(0)
