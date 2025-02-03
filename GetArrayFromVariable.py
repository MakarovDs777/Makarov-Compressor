import numpy as np
import matplotlib.pyplot as plt

def generate_numbers_from_shape(r, theta, fig):
    # Устанавливаем количество сегментов равным r
    num_segments = int(r)  # Приводим r к целому числу
    angles = np.linspace(0, 2 * np.pi, num_segments, endpoint=False) + theta  # Распределяем углы равномерно
    
    # Генерация радиусов на основе углов
    radii = np.arange(1, num_segments + 1)  # Здесь можно использовать любое преобразование для получения значений
    scaled_radii = radii * 10  # Масштабируем числа для определения радиусов отрезков

    # Рисуем отрезки с номерами
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)

    for i in range(num_segments):
        ax.plot([angles[i], angles[i]], [0, scaled_radii[i]], label=str(scaled_radii[i]))

    # Устанавливаем радиус и угол для совпадения с последним отрезком
    r_value = scaled_radii[-1] / 2
    theta_value = angles[-1] + np.pi / 2

    plt.legend()
    plt.show()

    # Возвращаем значение радиусов
    return scaled_radii.tolist(), r_value, theta_value

# Параметры
r = 175.0  # Количество сегментов
theta = 7.827910325645937
fig = 'Figure(640,480)'  # Здесь fig используется для создания графика

# Получаем массив чисел
result, r_value, theta_value = generate_numbers_from_shape(r, theta, fig)

print("Результат:", result)
print("r:", r_value)
print("theta:", theta_value)

