"""Игра угадай число за минимальное количество попыток
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1 # определяем начальные значения счетчика и диапазона угадывания
    min = 1
    max = 101 
    number_predict = np.random.randint(min, max) # предполагаемое рандомное число в диапазоне от 1 до 100
    
    while number != number_predict:
        count += 1
 
        if number > number_predict: 
            min = number_predict # если загаданное число больше, то сужаем диапазон угадывания снизу
        elif number < number_predict: 
            max = number_predict + 1 # если загаданное число меньше, то сужаем диапазон угадывания сверху
        
        number_predict = np.random.randint(min, max) # определим предполагаемое число в новом диапазоне  
         
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score



score_game(random_predict)
