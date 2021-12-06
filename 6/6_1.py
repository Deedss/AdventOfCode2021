
def readTextFile():
    # Read Lines from text file
    file = open('6.txt', 'r')
    line = file.readline()
    temp = [int(x) for x in line.split(',')]
    return temp

def days(prevCount : dict, day):
    newCount = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
    if day < 81:
        # Add new 0-days
        newCount["0"] = prevCount["1"]
        # Add new 1-days
        newCount["1"] = prevCount["2"]
        # Add new 2-days
        newCount["2"] = prevCount["3"]
        # Add new 3-days
        newCount["3"] = prevCount["4"]
        # Add new 4-days
        newCount["4"] = prevCount["5"]
        # Add new 5-days
        newCount["5"] = prevCount["6"]
        # Add new 6-days
        newCount["6"] = prevCount["7"] + prevCount["0"]
        # Add new 7-days
        newCount["7"] = prevCount["8"]
        # Add new 8-days
        newCount["8"] = prevCount["0"]

        days(newCount, day + 1)

    else:
        print(sum(prevCount.values()))
        
        
def countFishPerDay(fishes):
    countFishes = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
    for fish in fishes:
        countFishes[str(fish)] += 1
    return countFishes

def main():
    fishes = readTextFile()
    days(countFishPerDay(fishes), 1)


if __name__ == '__main__':
    main()
