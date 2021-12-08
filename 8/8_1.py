def processLines(lines):
    items = []
    for line in lines:
        temp = line.split(' | ')
        temp2 = temp[0].split(' ')
        temp3 = temp[1].split(' ')
        items.append((temp2, temp3))

    return items

def readTextFile():
    # Read Lines from text file
    file = open('8/8.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines]
    return temp

def main():
    lines = readTextFile()
    items = processLines(lines)

    count = 0
    for item in items:
        for val in item[1]:
            if len(val) in (2,3,4,7):
                count += 1

    print(count)

if __name__ == '__main__':
    main()