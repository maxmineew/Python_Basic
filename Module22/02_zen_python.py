file_zen = open("zen.txt", "r")
lines = file_zen.readlines()

for line in reversed(lines):
    print(line, end='')
file_zen.close()