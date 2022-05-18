# типы данных и переменные
# int, float, boolean, str, list, None

value = None
print(type(value))
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 12334
print(type(value))

s = 'helo world'
# s = 'helo \nworld'
# s = 'helo \'world' 
# s = "hello 'world'" 
# s = 'hello "world"'
print(s) # вывод строки

# print(a, b, s)
print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

# list = [1, 2, 3]
list = ['1', '2', '3', 'hello']
col = ['hello', 1, 2, 4.5, True]
print(list)
print(col)
