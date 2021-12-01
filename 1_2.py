

numbers = []


def calculateMeasurements(numbers):
    count = 0
    sums = []
    for i in range(2, len(numbers)):
        tup = (numbers[i], numbers[i-1], numbers[i-2])
        sums.append(sum(tup))

    for i in range(1, len(sums)):
        if sums[i] > sums[i-1]:
            count+=1

    print(count)

def readLines():
    # Read Lines from 1_1.txt
    file = open('1.txt', 'r')
    words = file.readlines()
    numbers = [int(x.strip()) for x in words]
    calculateMeasurements(numbers)

def main():
    readLines()

if __name__ == '__main__':
    main()
