#import os
import sys

def interpret(args):
    if not args:
        return 1
    f = open(args[0], 'r')
    instructions = f.read()
    #print(instructions)
    lines = instructions.splitlines()
    data = []
    for i in range(256):
        data.append(0)
    i = 0
    for x in lines:
        for y in x.split():
            data[i] = int(y)
            i += 1
    print(data)

    pc = 0
    while not data[255]:
       #print("step")
        val = data[data[(pc+1)%256]] - data[data[pc]]
        data[data[(pc+1)%256]] = (val+256)%256
        if val<=0: 
            pc = data[(pc+2)%256]
        else:
            pc = (pc+3)%256
        if data[254]:
            print(chr(int(data[254])),end='')
            data[254] = 0

    return data[255]

if __name__ == "__main__":
    sys.exit(interpret(sys.argv[1:]))


