def is_even(n):
    return True if n % 2 == 0 else False

def print_board(s):
    print('=' * len(s))
    print(s)
    print('=' * len(s))

def sum_of_list(lst):
    s = 0
    for i in lst:
        s += i
    return s

if __name__ == '__main__':
    print_board("Starting from functions module")