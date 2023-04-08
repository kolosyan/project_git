import sys

# filename = input()
filename = sys.argv[1]
# print(sys.argv[1])
res = open(filename + ".txt", "w")
res.close()
