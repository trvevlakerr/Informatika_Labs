# Дано
# Характеристики дискеты
disk_size_mb = 1.44
bytes_in_mb = 1024 * 1024
disk_size_bytes = disk_size_mb * bytes_in_mb

# Характеристики книги
pages = 100
lines_on_page = 50
symbols_in_line = 25
symbol_bytes = 4 # 4 байта для хранения одного кода символа

# Посчитаем объём одной книги в байтах
symbols_in_book = pages * lines_on_page * symbols_in_line
book_size_bytes = symbols_in_book * symbol_bytes

#Вычислим итоговое количество книг

number_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", number_books)