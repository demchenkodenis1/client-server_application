# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


words = ['class', 'function', 'method']
for i in words:
    print(i)
    word = eval(f"b'{i}'")
    print(f'type({type(word)}), {word}, {len(word)}')