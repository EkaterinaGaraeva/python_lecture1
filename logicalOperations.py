# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^

# is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)

b = 'qwe'
c = 'qwe'
print(b == c)

d = [1,2]
e = [1,2]
print(d == e)

f = 1 < 3 < 5 < 10
print(f)

func = 1
T = 4
x = 2
print(func<T>(x))

g = 1 > 2 or 4 < 6
print(g)

h = [1,2,3,4]
print(h)
print(not 2 in h)

is_odd = not h[0] % 2
print(is_odd)
