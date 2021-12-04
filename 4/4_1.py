from typing import List
import numpy as np
from dataclasses import dataclass


@dataclass
class Card:
    identifier : int = 0
    winning_number = 0
    items = []

    def checkItems(self, number):
        for x in range(0, 5):
            for y in range(0, 5):
                if self.items[x][y] == (number, "0"):
                    self.items[x][y] = (number, "1")
                    self.winning_number = int(number)

    def checkWin(self):
        for x in range(0, 5):
            if self.items[x][0][1] == '1' and self.items[x][1][1] == '1' and self.items[x][2][1] == '1' and self.items[x][3][1] == '1' and self.items[x][4][1] == '1':
                return True

        for y in range(0, 5):
            if self.items[0][y][1] == '1' and self.items[1][y][1] == '1' and self.items[2][y][1] == '1' and self.items[3][y][1] == '1' and self.items[4][y][1] == '1':
                return True

    def getSumUnmarked(self):
        sum = 0
        for list in self.items:
            for item in list:
                if item[1] == '0':
                    sum = sum + int(item[0])

        return sum

    

def readLines():
    # Read Lines from 1_1.txt
    file = open('4/4.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines if line.strip()]
    while('' in temp):
        temp.remove('')
    return temp

bingoCards : list[Card] = []

def Convert(lst):
    res_dct = {lst[i]: "unmarked" for i in range(0, len(lst), 2)}
    return res_dct

def getBingoCards(lines):
    count = 0
    while(count < len(lines)):
        temp = []
        temp2 = []
        for i in range(0, 5):
            temp2 = lines[count + i].split()
            while('' in temp2):
                temp2.remove('')

            temp3 = []
            for item in temp2:
                temp3.append((item, "0"))

            temp.append(temp3)

        card = Card()
        card.items = temp
        card.identifier = count
        bingoCards.append(card)
        count = count + 5            

    return bingoCards

def checkCards(bingoNumbers):
    winning_cards = []
    i = 0
    while i < len(bingoNumbers):
        for card in bingoCards:
            if card in winning_cards:
                continue
            card.checkItems(bingoNumbers[i])
            if card.checkWin() == True:
                winning_cards.append(card)
        i += 1
    return winning_cards

def main():
    bingoNumbers = readLines()[0].split(',')
    getBingoCards(readLines()[1: len(readLines())])
    cards = checkCards(bingoNumbers)

    print(cards[-1].getSumUnmarked())
    print(cards[-1].winning_number)

    print(cards[-1].getSumUnmarked() * cards[-1].winning_number)
if __name__ == '__main__':
    main()
