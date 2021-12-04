from os import remove


def findCommon(binaries, index):
    common = ''
    count = {'0': 0, '1': 0 }
    for binary in binaries:
        if binary[index] == '0':
            count['0'] = count['0'] + 1
        else:
            count['1'] = count['1'] + 1
    
    if count['0'] > count['1']:
        common = '0'
    else:
        common = '1'

    return common

def findLeastCommon(binaries, index):
    # Find most common values
    common = ''
    count = {'0': 0, '1': 0 }
    for binary in binaries:
        if binary[index] == '0':
            count['0'] = count['0'] + 1
        else:
            count['1'] = count['1'] + 1
    
    if count['0'] <= count['1']:
        common = '0'
    else:
        common = '1'

    return common

def remove_all_by_values(binaries, values):
    for value in values:
        while value in binaries:
            binaries.remove(value)

def oxygenRating(binaries):
    # Find most common values
    for index in range(0, len(binaries[0])):
        common = findCommon(binaries, index)

        tempList = [binary for binary in binaries if binary[index] == common]

        remove_all_by_values(binaries, tempList)

        if len(binaries) == 1:
            break

    return binaries[0]


def scrubberRating(binaries):
    for index in range(0, len(binaries[0])):
        leastCommon = findLeastCommon(binaries, index)

        tempList = [binary for binary in binaries if binary[index] == leastCommon]

        remove_all_by_values(binaries, tempList)

        if len(binaries) == 1:
            break

    return binaries[0]


def readLines():
    # Read Lines from 1_1.txt
    file = open('3.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines]
    return temp

def main():
    binaries = readLines()

    oxygenList = binaries.copy()
    scrubberList = binaries.copy()

    # Find the bit criteria
    oxygen = oxygenRating(oxygenList)
    scrubber = scrubberRating(scrubberList)
    
    print(int(oxygen, 2))
    print(int(scrubber, 2))
    print(int(oxygen, 2) * int(scrubber,2))

if __name__ == '__main__':
    main()
