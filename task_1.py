if __name__ == '__main__':
    lst = input('Write list: ')
    lst = lst.split()

    num = 0

    for ind, elem in enumerate(lst):
        if elem == '0':
            print(f"Zero's index: {ind}")
            num += 1

    print(f'Number of elements: {num}')
