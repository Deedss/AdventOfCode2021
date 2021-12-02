
instructions = []

position_sub = { "position":0, "aim":0, "depth":0 }

def movement(instructions):
    for com in instructions:
        if com[0] == 'forward':
            position_sub['position'] = position_sub['position'] + int(com[1])
            position_sub['depth'] = position_sub['depth'] + position_sub['aim'] * int(com[1])  
        elif com[0] == 'down':
            position_sub['aim'] = position_sub['aim'] + int(com[1])
        elif com[0] == 'up':
            position_sub['aim'] = position_sub['aim'] - int(com[1])
        
    print(position_sub)
    print(position_sub['position'] * position_sub['depth'])

def readLines():
    # Read Lines from 1_1.txt
    file = open('2.txt', 'r')
    lines = file.readlines()
    instructions = [tuple(line.strip().split()) for line in lines]
    movement(instructions)

def main():
    readLines()

if __name__ == '__main__':
    main()
