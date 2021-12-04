def calculateCommon(binaries):
    common = ''
    for i in range(0, len(binaries[0])):
        count = {'0': 0, '1': 0 }
        for binary in binaries:
            if binary[i] == '0':
                count['0'] = count['0'] + 1
            else:
                count['1'] = count['1'] + 1
        
        if count['0'] > count['1']:
            common = common + '0'
        else:
            common = common + '1'
    
    return int(common, 2)

def calculateEpsilon(binaries):
    epsilon = ''
    for i in range(0, len(binaries[0])):
        count = {'0': 0, '1': 0 }
        for binary in binaries:
            if binary[i] == '0':
                count['0'] = count['0'] + 1
            else:
                count['1'] = count['1'] + 1
        
        if count['0'] < count['1']:
            epsilon = epsilon + '0'
        else:
            epsilon = epsilon + '1'
    
    return int(epsilon, 2)

def readLines():
    # Read Lines from 1_1.txt
    file = open('3.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines]
    return temp

def main():
    binaries = readLines()
    commonValue = calculateCommon(binaries)
    epsilonValue = calculateEpsilon(binaries)
    print(commonValue)
    print(epsilonValue)
    print(commonValue * epsilonValue)

if __name__ == '__main__':
    main()
