# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.

import argparse
import sys


sys.argv = ['text', '7', '--verbose', '--repeat']

def main():

    parser = argparse.ArgumentParser(prog='Options and flags',
                                     description='Handing options and flags',
                                     epilog='Task4, HomeWork15')

    parser.add_argument('text', type=str, help='Строка для вывода')
    parser.add_argument('number', type=int, help='Число для вывода')

    parser.add_argument('--verbose',
                        action='store_true',
                        help='Вывод дополнительной информации о процессе')

    parser.add_argument('--repeat',
                        type=int,
                        default=1,
                        help='количество повторений строки в выводе')

    args = parser.parse_args()


    if args.verbose:
        print(f'Полученные аргументы: \nчисло - {args.number}, \nстрока - "{args.text}", \nповторения - {args.repeat}')

    print(f'Число - {args.number}, \nстрока - {args.text * args.repeat}')

if __name__ == '__main__':
    main()