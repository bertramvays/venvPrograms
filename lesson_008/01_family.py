# -*- coding: utf-8 -*-

from termcolor import cprint, colored
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# +Все они живут в одном доме, дом характеризуется:
# +  кол-во денег в тумбочке (в начале - 100)
# +  кол-во еды в холодильнике (в начале - 50)
# +  кол-во грязи (в начале - 0)
#
# +У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# +Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# +Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# +Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# +Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# +Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# +Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# +Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# +Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# +Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def act(self):
        self.dirt += 5

    def __str__(self):
        return colored(f'В доме:\n\t >>>денег: {self.money}, >>>еды:{self.food},'
                        f' >>>грязи:{self.dirt}', color='blue')


class Human:
    total_eated_food = 0

    def __init__(self, name, house):
        self.fullness = 30
        self.happiness = 100
        self.name = name
        self.house = house

    def __str__(self):
        return (colored(f'{self.name} >> '
                        f'уровень сытости: {self.fullness}, '
                        f'уровень счатья: {self.happiness}.', color='yellow'))


class Husband(Human):
    total_earned_money = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food > 30:
            self.fullness += 30
            self.house.food -= 30
            Human.total_eated_food += 30
            cprint(f'{self.name} - поел.', color='blue')
        else:
            self.fullness -= 10
            self.happiness -= 10
            cprint(f'В доме не хватает еды.'
                   f'{self.name} не может поесть.', color='red')

    def work(self):
        self.house.money += 150
        Husband.total_earned_money += 150
        self.fullness -= 10
        cprint(f'{self.name} - поработал.', color='blue')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(f'{self.name} - поиграл.', color='blue')

    def act(self):
        if self.fullness < 0:
            print(colored(f'{self.name} умер!!!!', color='red'))
            return
        elif self.happiness < 10:
            print(colored(f'{self.name} умер от депресии!!!!', color='red'))
            return
        elif self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness < 20:
            self.eat()
            return
        elif self.house.money < 90:
            self.work()
            return
        dice = randint(1, 6)
        if dice == 1 or dice == 2:
            self.work()
        elif dice == 3:
            self.eat()
        else:
            self.gaming()


class Wife(Human):
    total_fur_coats = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food > 25:
            self.fullness += 25
            self.house.food -= 25
            Human.total_eated_food += 25
            cprint(f'{self.name} - поела.', color='magenta')
        else:
            cprint(f'В доме не хватает еды.'
                   f'{self.name} не может поесть.', color='red')

    def shopping(self):
        if self.house.money >= 90:
            self.house.food += 90
            self.house.money -= 90
            self.fullness -= 10
            self.happiness += 15
            cprint(f'{self.name} - сходила за покупками.', color='magenta')
        else:
            cprint(f'В доме не хватает денег, '
                   f'{self.name} не может сходить за покупками.', color='red')

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.house.money -= 350
            self.fullness -= 10
            self.happiness += 60
            Wife.total_fur_coats += 1
            cprint(f'{self.name} - купила шубу.', color='magenta')
        else:
            self.happiness -= 30
            cprint(f'{self.name} хотела купить шубу. Но денег не нее нехватает. '
                   f'Она расcтроена, будет просить мужа,'
                   f' чтобы он сходил на работу', color='magenta')

    def clean_house(self):
        self.house.dirt -= 50
        self.fullness -= 10
        cprint(f'{self.name} - сделала уборку в доме.', color='magenta')

    def act(self):
        if self.fullness < 0:
            print(colored(f'{self.name} умерла!!!!', color='red'))
            return
        elif self.happiness < 10:
            print(colored(f'{self.name} умерла от депресии!!!!', color='red'))
            return
        elif self.house.dirt > 90:
            self.happiness -= 10
        if self.house.food < 55:
            self.shopping()
            return
        elif self.fullness < 20:
            self.eat()
            return
        dice = randint(1, 6)
        if dice == 1 or dice == 2:
            if self.house.dirt > 80:
                self.clean_house()
            else:
                self.eat()
        elif dice == 3 or dice == 4:
            self.shopping()
        elif dice == 5:
            self.buy_fur_coat()
        else:
            self.eat()


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='green')
    serge.act()
    masha.act()
    home.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

print(f'За год семья заработала денег: {Husband.total_earned_money}, '
      f'сьела еды: {Human.total_eated_food} , купила шуб: {Wife.total_fur_coats}.')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
