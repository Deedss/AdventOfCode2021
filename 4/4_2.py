



def readLines():
    # Read Lines from 1_1.txt
    file = open('4.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines]
    return temp

def main():
    binaries = readLines()

if __name__ == '__main__':
    main()
