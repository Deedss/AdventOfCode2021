import sys

def getTotalFuel(crabs):
    totalFuel = sys.maxsize
    bestPosition = 0
    for pos in range(0, max(crabs) + 1):
        tempFuel = 0
        for crab in crabs:
            tempFuel += abs(crab - pos)

        if tempFuel < totalFuel:
            totalFuel = tempFuel
            bestPosition = pos
    
    print(f'Fuel at pos:{bestPosition} is {totalFuel}')

def readTextFile():
    # Read Lines from text file
    file = open('7/7.txt', 'r')
    line = file.readline()
    temp = [int(x) for x in line.split(',')]
    return temp

def main():
    crabs = readTextFile()
    getTotalFuel(crabs)


if __name__ == '__main__':
    main()
