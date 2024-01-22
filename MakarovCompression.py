import matplotlib.pyplot as plt
import numpy as np

def create_geometric_shape(numbers):
    num_segments = len(numbers)
    angles = np.linspace(0, 2*np.pi, num_segments+1)[:-1]  # равномерно распределяем углы
    radii = np.array(numbers) * 10  # масштабируем числа для определения радиусов отрезков

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    # Рисуем отрезки с номерами
    for i in range(num_segments):
        ax.plot([angles[i], angles[i]], [0, radii[i]], label=str(numbers[i]))

    # Устанавливаем радиус и угол для совпадения с последним отрезком
    r = radii[-1] / 2
    theta = angles[-1] + np.pi/2

    plt.legend()
    plt.show()

    return r, theta, fig


def get_numbers_from_geometric_shape(r, theta, fig):
    ax = fig.gca()
    lines = ax.get_lines()

    numbers = []
    for line in lines:
        label = line.get_label()
        if label:
            numbers.append(int(label))

    return numbers


numbers = [2, 4, 3, 1, 5]
r, theta, fig = create_geometric_shape(numbers)
result = get_numbers_from_geometric_shape(r, theta, fig)

print("Исходный массив чисел:", numbers)
print("Результат:", result)