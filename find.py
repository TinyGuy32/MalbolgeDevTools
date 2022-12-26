import sys

numbers = open(sys.argv[1],"r").read().split("\n")

position = 0

while position<len(numbers):
    wanted_number = int(numbers[position])

    for i in range(33,126):
        if (position+i)%94 == wanted_number:
            print(chr(i),end='')
    position += 1
