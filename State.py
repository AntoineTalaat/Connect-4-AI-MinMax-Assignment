import math
import Converter
import Heuristic


class State:
    max = True
    rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
    alpha = -math.inf
    beta = math.inf
    def __init__(self):
        max = True
        rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
        alpha = -math.inf
        beta = math.inf

    def getScore(self):
        c = Converter.Converter()
        arrayState = c.convertStateToArray(self.rep)
        h = Heuristic.Heuristic(arrayState)
        return h.getHeuristicScore()

    def changeBit(self, parent, pos, bit):
        mask = 1 << pos
        parent = (parent & ~mask) | ((bit << pos) & mask)
        return parent

    def addToColumn(self, parent, col, playerColour):
        chunckShift = col * 9
        temp = 7 << chunckShift
        indexPlace = parent & temp
        indexPlace = indexPlace >> chunckShift
        position = chunckShift + indexPlace + 3

        if indexPlace < 6:
            # Modify the bit itself
            if playerColour == 'y':
                parent = self.changeBit(parent, position, 0)
            elif playerColour == 'r':
                parent = self.changeBit(parent, position, 1)

            # modify the index in representation
            binary = "{0:03b}".format(indexPlace + 1)  # 101

            for i in range(len(binary)):
                parent = self.changeBit(parent, chunckShift + i, int(binary[2 - i]))

            return True, parent
        return False, parent

    def findMyChildren(self):
        children = []
        myChildMax = not self.max
        for i in range(7):
            child = State()
            if self.max == True:
                # print("i ", i)
                flag, child.rep = self.addToColumn(self.rep, i, 'y')
                child.max = myChildMax

            else:
                #  print("i ", i)
                flag, child.rep = self.addToColumn(self.rep, i, 'r')
                child.max = myChildMax

            if flag == True:
                children.append(child)
        return children

    def isFull(self):
        converter = Converter.Converter()
        arrayState = converter.convertStateToArray(self.rep)
        for row in arrayState:
            for i in range(len(row)):
                if arrayState[row][i] == 'w':
                    return False
        return True
