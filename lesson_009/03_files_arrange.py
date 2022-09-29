# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class SortPhotos:
    def __init__(self, sorce_folder, dest_folder):
        self.sorce_folder = sorce_folder
        self.dest_folder = dest_folder

    # функция которая почает директорию и имя файла
    def main(self):
        for dirpath, dirnames, photosnames in os.walk(self.sorce_folder):
            ...

    # функция которая получает год и дату создания фотографии
    def get_photo_data(self, self.dirpath, self.photo_name):
        self.photo_path = self.dirpath + os.sep + self.photo_name
            self.photo_year, self.photo_month, *other_photo_data = time.gmtime(os.path.getmtime(self.photo_path))
            if self.photo_month < 10:
                self.photo_month = '0' + str(self.photo_month)
        return self.photo_year, self.photo_month

    # функция которая создает каталог елси он не существует и копирует туда фотографию



c = SortPhotos('./icons', './icons_by_year')
c.basefunc()
# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
