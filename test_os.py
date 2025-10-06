import os
import math
os.makedirs("C:/1/demo", exist_ok=True)

my_dir = "D:/"

my_list = os.listdir(my_dir)

# Задача - среди всех папок и файлов на диске Д найти только текстовые файлы

txt_files = []

for item in my_list:
    if os.path.isfile(os.path.join(my_dir,item)) and item.endswith(".txt"):
        txt_files.append(item)
print(txt_files)
