import random
from time import time


def get_days(km: int):
    if km < 100:
        return 0
    if km < 200:
        return get_days(km=(km-100)) + 1
    return get_days(km=(km-100)) + get_days(km=(km-200))

 
if __name__ == '__main__':
    start_time = time()
    km = random.randint(0, 2000)
    print(f'Total de KM {km}')
    days = get_days(km=km)
    print(f'Días para la entrega: {days} días')

    elapsed_time = time() - start_time
    print('End Process: ', elapsed_time)