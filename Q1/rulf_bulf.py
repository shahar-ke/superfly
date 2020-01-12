import argparse


def read_user_args():
    parser = argparse.ArgumentParser(description='rulf bulf, '
                                                 'prints numbers from 1 to n (inclusive). '
                                                 'prints "Rulf" for multiples of 3, '
                                                 'prints "Bulf" for multiples of 5, '
                                                 'prints "RulfBulf" for both')
    parser.add_argument('--n', dest='n', type=int, default=100, help='the number to count to from 1')
    return parser.parse_args()


def main():
    user_args = read_user_args()
    for i in range(1, user_args.n+1):
        print_str = str(i)
        multi_3 = False
        multi_5 = False
        if i % 3 == 0:
            multi_3 = True
        if i % 5 == 0:
            multi_5 = True
        if multi_3:
            print_str = 'Rulf'
        if multi_5:
            print_str = 'Bulf'
        if multi_3 and multi_5:
            print_str = "RulfBulf"
        print(print_str)


if __name__ == "__main__":
    main()