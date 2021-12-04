
instructions = []

position_sub = { "x":0, "y":0 }

def movement(instructions):
    for com in instructions:
        if com[0] == 'forward':
            position_sub['x'] = position_sub['x'] + int(com[1])
        elif com[0] == 'down':
            position_sub['y'] = position_sub['y'] + int(com[1])  
        elif com[0] == 'up':
            position_sub['y'] = position_sub['y'] - int(com[1])
        
    print(position_sub)
    print(position_sub['x'] * position_sub['y'])

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
