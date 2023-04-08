import sys


def main():
    extension = '.txt'
    filename = sys.argv[1]
    res = open(filename + extension, "w")
    res.close()


main()
