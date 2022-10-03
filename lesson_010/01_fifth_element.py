# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
leeloo = True
while leeloo:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    try:
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS * leeloo
        print(f"- Leeloo Dallas! Multi-pass № {result}!")

    except ValueError:
        print('Невозможно преобразовать к числу.')
    except IndexError:
        print('К сожалению вы вышли за границы списка.')
    except Exception:
        print('К сожалению возникла ошибка, но я пока не понимаю какая.')


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




