# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# import zipfile
#
# file =  './python_snippets/voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(file, "r")
# for file in zfile.namelist():
#     zfile.extract(file)

class Count_letters:
    def __init__(self, file):
        self.file = file

    def cnt_letters(self):
        self.characters_count = {}
        with open(self.file, 'r', encoding='1251') as file:
            for line in file:
                for ch in line:
                    if ch.isalpha():
                        if ch in self.characters_count.keys():
                            self.characters_count[ch] += 1
                        else:
                            self.characters_count[ch] = 0

        return dict(sorted(self.characters_count.items()))


class FineLineSeparator:
    n = 30  # ширина ячейки

    def __init__(self, char_dict):
        self.char_dict = char_dict

    def separate_line(self):
        sep_line = f'+{"":-^30}+{"":-^30}+'
        print(sep_line)

    def header(self):
        header_line = f'|{"буква":^30}|{"частота":^30}|'
        print(header_line)

    def key_line(self, key, value):
        k_line = f'|{key:^30}|{value:^30}|'
        print(k_line)

    def footer(self, value_list):
        footer_line = f'|{"Итого":^30}|{sum(value_list):^30}|'
        print(footer_line)

    def result_table(self):
        self.separate_line()
        self.header()
        self.separate_line()
        for key in self.char_dict:
            self.key_line(key, self.char_dict[key])
        self.separate_line()
        self.footer(self.char_dict.values())
        self.separate_line()


voyna_i_mir_counting = Count_letters('voyna-i-mir.txt')
voyna_counted_dict = Count_letters.cnt_letters(voyna_i_mir_counting)
c = FineLineSeparator(voyna_counted_dict)
FineLineSeparator.result_table(c)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
