from time import time
list_fibonacci = [1, 1]


def get_next_fibonachi(list_f: list = None):
    if list_f is not None:
        list_fibonacci = list_f
    next_list = [list_fibonacci[-1], sum(list_fibonacci)]
    return next_list


def get_divider(number: int):
    divider = 2
    top_divisor = number
    count = 2
    while divider < top_divisor:
        if number % divider == 0:
            count += 1
            next_divisor = number // divider
            if divider != next_divisor:
                count += 1
        top_divisor = number // divider
        divider += 1
    return count

if __name__ == '__main__':
    start_time = time()
    while True:
        list_fibonacci = get_next_fibonachi()
        count_divider = get_divider(list_fibonacci[-1])

        if count_divider >= 1000:
            print(count_divider, list_fibonacci[-1])
            break
    elapsed_time = time() - start_time
    print('End Process: ', elapsed_time)
