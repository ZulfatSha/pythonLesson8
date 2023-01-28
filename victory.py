#МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание:
#Написать или улучшить программу Викторина из предыдущего дз
# (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
#Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') -
# предлагаю для тренировки пока использовать строку
#Программа выбирает из этих 10-и 5 случайных людей,
# это можно реализовать с помощью модуля random и функции sample
#Пример использования sample:
#import random
#numbers = [1, 2, 3, 4, 5]
# 2 - количество случайных элементов
#result = random.sample(numbers, 2)
#print(result) # [5, 1]
#После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
#пользователь вводит дату в формате 'dd.mm.yyyy'
#Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
# но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
#В конце считаем количество правильных и неправильных ответов и предлагаем начать снова

import random

def victory_games():

    dict_celebrity = {
                '1': ['Гамид Агаларов', '16.07.2000', 'Шестнадцатое июля 2000 года'],
                '2': ['Андрей Аршавин', '29.05.1981', 'Двадцать девятое мая 1981 года'],
                '3': ['Динияр Билялетдинов', '27.02.1985', 'Двадцать седьмое февраля 1985 года'],
                '4': ['Дмитрий Сычев', '26.10.1983', 'Двадцать шестое октября 1983 года'],
                '5': ['Александр Кержаков', '27.11.1982', 'Двадцать седьмое ноября 1982 года'],
                '6': ['Игорь Акинфеев', '08.04.1986', 'Восьмое апреля 1986 года'],
                '7': ['Артем Дзюба', '22.08.1988', 'Двадцать второе августа 1988 года'],
                '8': ['Александр Головин', '30.05.1996', 'Тридцатое мая 1996 года'],
                '9': ['Денис Черышев', '26.12.1990', 'Двадцать шестое декабря 1990 года'],
                '10': ['Федор Смолов', '09.02.1990', 'Девятое февраля 1990 года']
                      }

    print('Добро пожаловать в мини-викторину!')
    print('Она посвящена российским футболистам.')
    print('Вам будет предложено отгадать дату рождения пятерых футболистов. Итак, приступим!')

    quantity = 0
    error = 0
    all_question = 5

    result = random.sample(dict_celebrity.keys(), 5)

    for i in result:
        if i in dict_celebrity.keys():
            print()
            data = input('Футболист: ' + str(dict_celebrity[i][0]) + ' - Введите его дату рождения (в формате \'dd.mm.yyyy\'): ')
            if data == dict_celebrity[i][1]:
                print('Верно')
                quantity = quantity + 1
            else:
                print(dict_celebrity[i][2])
                error = error + 1
    print()
    print('Ваш результат:')
    print('Верных ответов: ', quantity)
    print('Неверных ответов: ', 5 - quantity)
    no_correct_answers = (error * 100)/all_question
    print(no_correct_answers, '% неправильных ответов')

    if quantity == 100.0:
        print("Поздравляем! Вы справились со всеми вопросами верно")
    else:
        print("Не отчаивайтесь, в следующий раз вы точно справитесь!")
    print("Попробуйте снова.")