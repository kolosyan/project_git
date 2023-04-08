import sys


def main():
    filename = sys.argv[1]
    res = open(filename + ".txt", "w")
    res.close()


main()
