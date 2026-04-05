# TODO импортировать необходимые молули
import csv  # Импортируем модуль csv для работы с CSV файлами
import json  # Импортируем модуль json для сериализации данных в JSON формат

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:   # Открываем csv-файл для чтения ('r'), говорим что он в кодировке utf-8, и называем его csv_file

        reader = csv.DictReader(csv_file) # Создаем объект DictReader, который превращает строки CSV в словари

        # Читаем все строки из CSV и превращаем их в список словарей
        data = list(reader)
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:  # Открываем json-файл для записи ('w'), кодировка utf-8, называем его json_file
        # Записываем список словарей в файл в формате JSON
        # indent=4 делает отступ 4 пробела
        # ensure_ascii=False сохраняет символы в исходной кодировке
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # Команда json.dump берёт наши данные (список data) и записывает их в файл json_file, делая отступы по 4 пробела

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
