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
                formated_string = f'[{el}] {self.nok_events[el]}\n'
                self.out_file.write(formated_string)
        print(f"Nok file is created.")


if __name__ == '__main__':
    log_file = ParseNokFile('events.txt')
    log_file.get_nok_ivents()
    log_file.write_nok_events_file('Nok_events_per_minute.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
