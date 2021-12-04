

numbers = []


def calculateMeasurements(numbers):
    count = 0
    print(str(numbers[0]) + " no previous measurement")
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            print(str(numbers[i]) + " increased")
            count+=1
        else:
            print(str(numbers[i]) + " decreased")
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
