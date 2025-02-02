'''import numpy as np

def get_numbers_from_geometric_shape(r, theta):
    num_segments = 10  # Количество сегментов, можно изменить
    angles = np.linspace(0, 2 * np.pi, num_segments + 1)[:-1]

    # Генерация радиусов на основе r и угла theta
    radii = r * np.abs(np.sin(angles + theta))  # Используем abs, чтобы избежать отрицательных значений

    # Преобразуем радиусы в список чисел для возвращения
    numbers = [float(radius) for radius in radii]

    return numbers

# Параметры
r = 175.0
theta = 7.827910325645937
fig = '640,480'  # Здесь fig не используется, но можно добавить логику при желании

# Получаем массив чисел
result = get_numbers_from_geometric_shape(r, theta)

print("Результат:", result)
'''
