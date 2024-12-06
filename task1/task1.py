# Задание 1. 
# Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы. 
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, 
# а логи уровня WARNING и выше — в warnings_errors.log.


import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

letter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


debug_info = logging.FileHandler('debug_info.log')
debug_info.setLevel(logging.DEBUG)
debug_info.setFormatter(letter)
logger.addHandler(debug_info)


warning_error = logging.FileHandler('warning_error.log')
warning_error.setLevel(logging.WARNING)
warning_error.setFormatter(letter)
logger.addHandler(warning_error)


logger.debug('Level DEBUG')
logger.info('Level INFO')
logger.warning('Level WARNING')
logger.error('Level ERROR')
logger.critical('Level CRITICAL')