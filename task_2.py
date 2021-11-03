def find_sum(arr):
    lst_of_elm = []

    for ind, elem in enumerate(arr):
        if float(elem) < 0:
            lst_of_elm.append(ind)
        if len(lst_of_elm) >= 2:
            break

    sum = 0

    i = lst_of_elm[0] + 1
    while i < lst_of_elm[1]:
        sum = sum + float(arr[i])
        i += 1

    return sum


def find_maximal(arr):
    max = float(arr[0])

    for el in arr:
        elem = float(el)
        if elem < 0:
            elem = elem * (-1)
        if elem > max:
            max = elem
    return max


lst = input('Write list: ')
lst = lst.split()

sum_of_el = find_sum(lst)
max_el = find_maximal(lst)

print(f'Maximal element: {max_el}')
print(f'Sum of elements: {sum_of_el}')
