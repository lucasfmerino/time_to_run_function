from time import time


def f_master(func):
    def time_tbe(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total = (end_time - start_time) * 1000
        print(f'The function {func.__name__} took {total:.2f} ms to be executed')
        return result

    return time_tbe


@f_master
def f_printr(int_range):
    for i in range(int_range):
        print(i)


if __name__ == '__main__':

    f_printr(1000000)
