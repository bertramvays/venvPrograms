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

input_log_file = 'events.txt'
nok_events = {}
with open(input_log_file, 'r', encoding='utf8') as file:
    for line in file:
        if 'NOK' in line:
            s = line.split(' ')
            nok_event_time = s[0][1:] + " " + s[1][:5]
            if nok_event_time in nok_events:
                nok_events[nok_event_time] += 1
            else:
                nok_events[nok_event_time] = 1

otput_log_file = 'nok_events_per_minute.txt'
with open(otput_log_file, 'w', encoding='utf8') as out_file:
    for el in nok_events:
        formated_string = f'[{el}] {nok_events[el]}\n'
        out_file.write(formated_string)


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828