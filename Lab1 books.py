# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
rows_on_page = 50
symbols_on_row = 25
bytes_on_symbol = 4
disk = 1.44 * 1024 * 1024
book = pages * rows_on_page * symbols_on_row * bytes_on_symbol
books_c = disk // book
print("Количество книг, помещающихся на дискету:", books_c)
