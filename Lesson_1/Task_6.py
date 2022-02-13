# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед
# нами файл в неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

from chardet.universaldetector import UniversalDetector

words = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as f:
    for i in words:
        f.write(f'{i}\n')

detector = UniversalDetector()
with open('test_file.txt', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
enc_file = detector.result.get('encoding')

words = []
with open('test_file.txt', 'r', encoding=enc_file) as f:
    for line in f:
        words.append(line.rstrip())
print(words)