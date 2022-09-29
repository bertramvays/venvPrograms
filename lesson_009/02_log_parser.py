# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class ParseNokFile:

    def __init__(self, input_log_file):
        self.input_log_file = input_log_file
        self.nok_events = {}

    def get_nok_ivents(self):
        with open(self.input_log_file, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    s = line.split(' ')
                    self.nok_event_time = s[0][1:] + " " + s[1][:5]
                    if self.nok_event_time in self.nok_events:
                        self.nok_events[self.nok_event_time] += 1
                    else:
                        self.nok_events[self.nok_event_time] = 1
        print("Nok events is selected.")
        return self.nok_events

    def write_nok_events_file(self, otput_log_file):
        self.otput_log_file = otput_log_file
        with open(self.otput_log_file, 'w', encoding='utf8') as self.out_file:
            for el in self.nok_events:
                formated_string = f'\t\t\t\t\t[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created.")


class NokFile_grouped(ParseNokFile):
    def __init__(self, input_log_file):
        super().__init__(input_log_file)

    def get_nok_ivents(self):
        super().get_nok_ivents()

    def write_nok_group_year(self, otput_log_file):
        self.otput_log_file = otput_log_file
        with open(self.otput_log_file, 'w', encoding='utf8') as self.out_file:
            self.year = list(self.nok_events.keys())[0][0:4]
            self.out_file.write(f'Year: {self.year}\n')
            for el in self.nok_events:
                self.curent_year = el[0:4]
                if self.curent_year != self.year:
                    self.year = self.curent_year
                    self.out_file.write(f'Year: {self.year}\n')
                formated_string = f'\t\t\t\t\t[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created. Grouped by Year.")

    def write_nok_group_month(self, otput_log_file):
        self.otput_log_file = otput_log_file
        with open(self.otput_log_file, 'w', encoding='utf8') as self.out_file:
            self.month = list(self.nok_events.keys())[0][5:7]
            self.out_file.write(f'\tmonth: {self.month}:\n')
            for el in self.nok_events:
                self.curent_month = el[5:7]
                if self.curent_month != self.month:
                    self.month = self.curent_month
                    self.out_file.write(f'\tmonth: {self.month}:\n')
                formated_string = f'\t\t\t\t\t[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created. Grouped by month")

    def write_nok_group_day(self, otput_log_file):
        self.otput_log_file = otput_log_file
        with open(self.otput_log_file, 'w', encoding='utf8') as self.out_file:
            self.day = list(self.nok_events.keys())[0][8:10]
            self.out_file.write(f'\t\tday: {self.day}:\n')
            for el in self.nok_events:
                self.curent_day = el[8:10]
                if self.curent_day != self.day:
                    self.day = self.curent_day
                    self.out_file.write(f'\t\tday: {self.day}:\n')
                formated_string = f'\t\t\t\t\t[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created. Grouped by day")

    def write_nok_group_hour(self, otput_log_file):
        self.otput_log_file = otput_log_file
        with open(self.otput_log_file, 'w', encoding='utf8') as self.out_file:
            self.hour = list(self.nok_events.keys())[0][11:13]
            self.out_file.write(f'\t\t\thour: {self.hour}:\n')
            for el in self.nok_events:
                self.curent_hour = el[11:13]
                if self.curent_hour != self.hour:
                    self.hour = self.curent_hour
                    self.out_file.write(f'\t\t\thour: {self.hour}:\n')
                formated_string = f'\t\t\t\t\t[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created. Grouped by hour")


if __name__ == '__main__':
    log_file = ParseNokFile('events.txt')
    log_file.get_nok_ivents()
    log_file.write_nok_events_file('Nok_events_per_minute.txt')
    log_file2 = NokFile_grouped('events.txt')
    log_file2.get_nok_ivents()
    log_file2.write_nok_group_year('Year_goruped.txt')
    log_file2.write_nok_group_month('Month_goruped.txt')
    log_file2.write_nok_group_day('Day_goruped.txt')
    log_file2.write_nok_group_hour('Hour_goruped.txt')
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
