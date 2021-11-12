n = int(input())
a = [i for i in range(n)]
print(a)

a = [1, 2, 3, 4, 5, 6, 7]
b = list(map(lambda x: x**2, a))
print(f'a = {a}\nb={b}')