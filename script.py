import sys


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print('вы не ввели аргумент')
        return
    res = open(filename + ".txt", "w")
    res.close()


main()
