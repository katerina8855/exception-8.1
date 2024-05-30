print(f'\n***** Исключение: обработка ValueError (Ошибка определения значения) *****')


def string_int(s):
    try:
        return int(s)
    except:
        print(f'Ошибка: необходимо ввести  ЦЕЛОЕ ЧИСЛО !!! Попробуй еще раз.')


s = input('Введите целое число: ')
print('Проверка на входе типа переменной s: ', type(s))
print(f'Проверка после вызова функции, тип переменной s: {type(string_int(s))}')

print(f'\n******* Исключение: обработка (Ошибка "Файл не найден"), IOError (Ошибка ввода-вывода) *******')


def read_file(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            return file.read()
    except FileNotFoundError:
        print('Ошибка: Ты не указал путь к файлу или перемести файл в текущую папку проекта')
    except IOError:
        print('Ошибка: Неправильно ввел название файла')



filename = ('08_dom_zadan_26.txt')
print(read_file(filename))  # чтение содержимого файла

print('\n**** Исключение: обработка ZeroDivisionError(Ошибка деления на ноль), TypeError(Ошибка типа) ****')


def divide_numbers(a, b):
    try:
        print(f'Результат = {a / b:0.0f}')  # округлил до целого числа
    except ZeroDivisionError as z:
        print(f'Ошибка: второй аргумент функции = {b} (деление на ноль)... будь внимательнее !!!...{z}')
    except TypeError as z:
        print('Ошибка: аргументы функции должны быть числовыми, а не текст...', z)
    else:  # 'этот блок исполняется только, если нет исключений
        print('Ты молодец!!!! Исключений не произошло')


divide_numbers(26, 13)

print('\n****** Исключение: обработка IndexError (Ошибка индексирования), TypeError(Ошибка типа) ******')


def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        print('Ошибка: элементов в списке меньше. Указывай индекс правильно')
    except TypeError:
        print('Ошибка: обрати внимание на Индекс - он должен быть целым числом')
    finally:  # выходит всегда, при любом раскладе... как напоминалка или когда нужно что-то сделать обязательно (к примеру закрыть файл)
        print('Внимание : работаем только со списком.')


my_list = ['Мартини', 12, 'LibeFrauMilch', 8]
my_index = 22
print(access_list_element(my_list, my_index))