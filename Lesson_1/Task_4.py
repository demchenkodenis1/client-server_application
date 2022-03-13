# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    word_in_byte = i.encode('utf-8')
    word_in_str = word_in_byte.decode('utf-8')
    print(f'{word_in_byte}, {word_in_str}')