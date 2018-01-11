import sys

info = sys.argv
number = int(info[1])

binary = [0,0,0,0,0,0,0,0]

if number >= 256:
    print("The number is too large")
    sys.exit("number >= 256")
if number >= 128 and number < 256:
    binary[0] = 1
    number -= 128
    print(number)
if number >= 64:
    binary[1] = 1
    number -= 64
    print("yes")
if number >= 32:
    binary[2] = 1
    number -= 32
if number >= 16:
    binary[3] = 1
    number-= 16
if number >= 8:
    binary[4] = 1
    number -= 8
if number >= 4:
    binary[5] = 1
    number -= 4
if number >= 2:
    binary[6] = 1
    number -= 2
if number == 1:
    binary[7] = 1
    number -= 1
print("".join(map(str,binary)))

sys.exit("This is working")
