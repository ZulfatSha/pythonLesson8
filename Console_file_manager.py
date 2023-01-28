"""
1. Создать новый проект ""Консольный файловый менеджер"
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.

Описание пунктов:
- создать папку
после выбора пользователь вводит название папки, создаем её в рабочей директории;
- удалить (файл/папку)
после выбора пользователь вводит название папки или файла, удаляем из рабочей директории если такой есть;
- копировать (файл/папку)
после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
- просмотр содержимого рабочей директории
вывод всех объектов в рабочей папке;
- посмотреть только папки
вывод только папок которые находятся в рабочей папке;
- посмотреть только файлы
вывод только файлов которые находятся в рабочей папке;
- просмотр информации об операционной системе
вывести информацию об операционной системе (можно использовать пример из 1-го урока);
- создатель программы
вывод информации о создателе программы;
- играть в викторину
запуск игры викторина из предыдущего дз;
- мой банковский счет
запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы управлением счетом в главной программе сумму и историю покупок можно не запоминать);
- смена рабочей директории (*необязательный пункт)
усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь. Меняем рабочую директорию на ту что ввели и работаем уже в ней;
- выход
выход из программы.
Так же можно добавить любой другой интересный или полезный функционал по своему желанию
После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
"""
import os
import shutil
import sys


def new_folder(folder_name):
    '''    Создать папку    '''
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Такая папка уже существует')

def delete_folder(folder_name):
    '''    Удалить папку    '''
    try:
        os.rmdir(folder_name)
    except FileNotFoundError:
        print('Такая папка отсутствует')

def copy_file_or_folder(fpath, file_name, folder_name):
    '''    Копировать файл/папку    '''
    try:
        if os.path.isdir(fpath):
            shutil.copytree(file_name, folder_name, copy_function=shutil.copy)
        else:
            shutil.copy(file_name, folder_name)
    except FileNotFoundError:
        print('Такой папки или файла не существует')


def show_files_and_folders():
    '''    Просмотр содержимого рабочей директории    '''
    print(os.listdir())

def save_files_and_folders():
    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'
    files_list = [i for i in files_and_folders_list if os.path.isfile(folder_path + i)]
    folders_list = [i for i in files_and_folders_list if os.path.isdir(folder_path + i)]
    files_and_folders = open("listdir.txt", "w")
    files_and_folders.write(f'files: {files_list}\n dirs: {folders_list}')
    files_and_folders.close()


def show_folders():
    '''    Посмотреть только папки    '''

    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'
    folders_list = [i for i in files_and_folders_list if os.path.isdir(folder_path + i)]
    print(folders_list)

def show_files():
    '''    Посмотреть только файлы    '''

    files_and_folders_list = os.listdir()
    folder_path = os.getcwd() + '/'
    files_list = [i for i in files_and_folders_list if os.path.isfile(folder_path + i)]
    print(files_list)

def system_info():
    '''    Просмотр информации об операционной системе    '''
    print('My system is ', sys.platform, '(', os.name, ')')

def creator():
    '''    Создатель программы    '''
    uldinium = open('uldinium')
    print(uldinium.read())

def change_directory():
    '''    Смена рабочей директории    '''
    new_dir = input('введите новую директорию')
    os.chdir(new_dir)