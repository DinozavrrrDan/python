# TODO Найдите количество книг, которое можно разместить на дискете
kilobytes_in_megabyte = 1024
bytes_in_kilobyte = 1024
disk_memory = 1.44 * kylpbytes_in_megabyte * bytes_in_kilobyte
book_pages = 100
string_on_page = 50 
symbols_in_string = 25
memory_one_symbol = 4
book_size_in_memory = memory_one_symbol * symbols_in_string * string_on_page * book_pages
print("Количество книг, помещающихся на дискету:", round(disk_memory / book_size_in_memory))
