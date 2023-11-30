#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    # args: number of args
    n = len(sys.argv) - 1
    # prl: args plural
    p = 's' if n != 1 else ''

    print('{0} argument{1}{2}'.format(n, p, '.' if n == 0 else ':'))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print('{}: {}'.format(i, arg))
