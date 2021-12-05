from dataclasses import dataclass
import numpy as np

@dataclass
class Vent:
    startNode = [] # Node for x1,y1
    endNode = [] # Node for x2,y2
    delta = [] # Movement from point to point

    def determineBetweenPoints(self):
        self.delta[0] =  self.endNode[0] - self.startNode[0]
        self.delta[1] =  self.endNode[1] - self.startNode[1]

@dataclass
class Diagram:
    field = [] # Field for lines

    def drawField(self, botright):
        self.field = np.zeros((botright[0], botright[1]), dtype=int)

    def findOverlapping(self):
        total = 0
        for row in self.field:
            for point in row:
                if point >= 2:
                    total += 1

        return total


vents : list[Vent] = []
diagram = Diagram()

def fillVents(text):
    # For each line in text file
    for line in text:
        # Make a new vent, split at ->, and then the ,
        temp = line.split('->')

        vent = Vent()
        vent.startNode = [int(x) for x in temp[0].split(',')]
        vent.endNode = [int(x) for x in temp[1].split(',')]

        vents.append(vent)

def readTextFile():
    # Read Lines from text file
    file = open('5.txt', 'r')
    lines = file.readlines()
    temp = [line.strip() for line in lines if line.strip()]
    while('' in temp):
        temp.remove('')
    return temp

def findHighestXY():
    # Find highest values in botright and make a diagram
    # from topleft [0,0] to bottom right with highest
    botright = [0, 0]
    for vent in vents:
        if vent.startNode[0] > botright[0]:
            botright[0] = vent.startNode[0]
        if vent.startNode[1] > botright[1]:
            botright[1] = vent.startNode[1]
        if vent.endNode[0] > botright[0]:
            botright[0] = vent.endNode[0]
        if vent.endNode[1] > botright[1]:
            botright[1] = vent.endNode[1]
    diagram.drawField(botright)

def checkOverlapping():
    # check delta??
    pass

def main():
    # Fill a list with Vents
    fillVents(readTextFile())
    findHighestXY()

if __name__ == '__main__':
    main()
