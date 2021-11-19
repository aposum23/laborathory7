#!/usr/bin/env python3
def find_sum(arr):
    lst_of_elm = []

    for ind, elem in enumerate(arr):
        if float(elem) == 0:
            lst_of_elm.append(ind)
        if len(lst_of_elm) >= 2:
            break

    srz = arr[lst_of_elm[0]:lst_of_elm[1]]

    return sum(map(float, srz))


def find_maximal_heand(arr):
    max = float(arr[0])

    for el in arr:
        elem = float(el)
        if elem < 0:
            elem = elem * (-1)
        if elem > max:
            max = elem
    return max


def find_maximal(arr):
    abs_lst = map(abs, arr)
    return max(abs_lst)


if __name__ == '__main__':
    lst = input('Write list: ')
    lst = lst.split()

    sum_of_el = find_sum(lst)
    max_el_heand = find_maximal_heand(lst)
    max_el = find_maximal(lst)

    print(f'Maximal element heandmade: {max_el_heand}')
    print(f'Maximal element: {max_el}')
    print(f'Sum of elements: {sum_of_el}')
