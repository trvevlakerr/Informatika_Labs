# TODO решите задачу

import json  # импортируем модуль для работы с JSON
def task() -> float:  # функция для вычисления суммы произведений score * weight

    with open("input.json","r",encoding="utf-8") as f:  # открываем JSON файл на чтение
        data = json.load(f)  # читаем содержимое файла и превращаем в список словарей

    total = 0  # переменная для суммы произведений

    for item in data:  # item - это словарь с ключами score и weight

        total += item["score"] * item["weight"]  # вычисляем произведение и добавляем к total

    return round(total, 3)  # возвращаем сумму, округлённую до 3 знаков после запятой

print(task())  # вызываем функцию и печатаем результат
