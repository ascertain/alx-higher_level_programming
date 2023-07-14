#!/usr/bin/python3
""" define function to reads from input """


def print_st(size, status):
    """ print the matrix """

    print("File size: {}".format(size))

    for k in sorted(status):
        print("{}: {}".format(k, status[k]))


if __name__ == "__main__":
    import sys

    size = 0
    status = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num = 0

    try:
        for li in sys.stdin:
            if num == 10:
                print_st(size, status)
                num = 1
            else:
                num += 1

            li = li.split()

            try:
                size += int(li[-1])

            except (IndexError, ValueError):
                pass

            try:
                if li[-2] in codes:
                    if status.get(li[-2], -1) == -1:
                        status[li[-2]] = 1

                    else:
                        status[li[-2]] += 1

            except IndexError:
                pass

        print_st(size, status)

    except KeyboardInterrupt:
        print_st(size, status)
        raise
