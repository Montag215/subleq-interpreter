#import os
import sys

def interpret(args):
    if not args:
        print("usage: interpreter.py FILENAME")
        return 1 # no input file
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
            data[i] = abs(int(y)+512)%256
            i += 1
            if i>252:
                break
        if i>252:
            break
    print(data) # prints the program

    pc = 0
    while True: # main program
        #print("step")
        data[252] = 0 # constant zero byte
        x = data[data[(pc+1)%256]] # collect referenced data

        if data[(pc+1)%256] == 253: # std input
            x = ord(sys.stdin.read(1))
        y = data[data[pc]]
        if data[pc] == 253:
            y = ord(sys.stdin.read(1))

        val = x - y
        if data[(pc+1)%256] == 255: # return if written to
            return (val+256)%256
        
        data[data[(pc+1)%256]] = (val+256)%256 # assignment
        if val<=0: # branch?
            pc = data[(pc+2)%256]
        else:
            pc = (pc+3)%256

        if data[254]: # std output
            print(chr(int(data[254])),end='')
            data[254] = 0

if __name__ == "__main__":
    sys.exit(interpret(sys.argv[1:]))


