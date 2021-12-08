def sortedItems(items):
    for item in items:
        pass

def readTextFile():
    # Read Lines from text file
    file = open('8/8.txt', 'r')
    lines = file.readlines()
    return lines

def main():
    lines = readTextFile()
    sorted_items = sortedItems(lines)

if __name__ == '__main__':
    main()