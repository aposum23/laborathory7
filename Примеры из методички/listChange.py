my_list = ['один', 'два', 'три', 'четыре', 'пять']
my_list[2] = 'ноль'

my_list = ['один', 'два', 'три', 'четыре', 'пять']
elem = my_list[-1]
print(elem)

my_list = [1, 2, 3, 4, 5]
my_list.insert(1,'Привет')
print(my_list)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
my_list.append('ещё один')
print(my_list)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
list_2 = ['шесть', 'семь']
my_list.extend(list_2)
print(my_list)

my_list = ['cde', 'fgh', 'abc', 'klm', 'opq']
list_2 = [3, 5, 2, 4, 1]
my_list.sort()
list_2.sort()
print(my_list)
print(list_2)

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
removed = my_list.pop(2)
print(my_list)
print(removed)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
removed = my_list.pop()
print(my_list)
print(removed)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
my_list.remove('два')
print(my_list)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
del my_list[2]
print(my_list)

my_list = ['один', 'два', 'три', 'четыре', 'пять']
del my_list[1:3]
print(my_list)
