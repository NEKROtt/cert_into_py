Погружение в Python (семинары)

Задание 1. Логирование с использованием нескольких файлов
Напишите скрипт, который логирует разные типы сообщений в разные файлы. Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня WARNING и выше — в warnings_errors.log.

Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер недели в году.

Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и возвращает дату, которая наступит через указанное количество дней. Дополнительно, выведите эту дату в формате YYYY-MM-DD.

Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать, сколько раз повторить строку в выводе.

Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит: имя файла без расширения или название каталога, расширение, если это файл, флаг каталога, название родительского каталога. В процессе сбора сохраните данные в текстовый файл используя логирование.