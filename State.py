import math
import sys
import Converter
import Heuristic

class State:
    rep = int('0b111111000111111000111111000111111000111111000111111000111111000', 2)
    children = []
    max = True

    alpha = -math.inf
    beta = math.inf

    def getScore(self):
        # if self.isFull():
        #     return 0#score mn mark
        # else:
        #     return 0#heuristic mn tony
        c= Converter.Converter()
        arrayState = c.convertStateToArray(self.rep)
        h=Heuristic.Heuristic(arrayState)
        return h.getHeuristicScore()


    def changeBit(self,parent, pos, bit):
       # print("pos ", pos)
       # print("bit ", bit)
       # print("parent ",bin(parent))

        mask = 1 << pos
        parent = (parent & ~mask) | ((bit << pos) & mask)
       # print("edited ",bin(parent))
        return parent

    def addToColumn(self, parent, col, playerColour):
     #   print("parent ",parent)
      #  print("coln ",col)

        chunckShift = col * 9
        temp = 7 << chunckShift
        indexPlace = parent & temp
        indexPlace = indexPlace >> chunckShift
        position = chunckShift + indexPlace + 3


       # print("chunck  ",chunckShift)
       # print("index place ",indexPlace)
       # print("position ",position)
        # Modify the bit itself
        if playerColour == 'y':
            parent = self.changeBit(parent, position, 0)
        elif playerColour == 'r':
            parent = self.changeBit(parent, position, 1)

        # modify the index in representation
        binary = "{0:03b}".format(indexPlace + 1)  # 101

        for i in range(len(binary)):
          #  print("loop counter ",i)
            parent = self.changeBit(parent, chunckShift + i, int(binary[2 - i]))

        return parent

    def findMyChildren(self):
        myChildMax = not self.max
        for i in range(7):
            child = State()
            if (self.max == True):
               # print("i ", i)
                child.rep = self.addToColumn(self.rep, i, 'y')
                child.max = myChildMax
                child.children=[]
            else:
              #  print("i ", i)
                child.rep = self.addToColumn(self.rep, i, 'r')
                child.max = myChildMax
                child.children = []

            #conv = Converter.Converter()

            #print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            #arr = conv.convertStateToArray(child.rep)
            #for row in arr:
             #   print(row)
            self.children.append(child)

    def isFull(self):
        converter = Converter.Converter()
        arrayState = converter.convertStateToArray(self.rep)
        for row in arrayState:
            for i in range(len(row)):
                if arrayState[row][i] == 'w':
                    return False
        return True


if __name__ == '__main__':
    state = State()
    state.rep = int('111111000111111001111100011110111100111111001111000100111100010', 2)
    print(len(state.children))
    # print(bin(state.rep))
    # state.addToColumn(6, 'y')
    state.findMyChildren()
    print(len(state.children))

    for i in range(7):
        print(state.children[i].rep)
        print("has x children : " + str(len(state.children[i].children)))

    for i in range(7):
      #  print(state.children[i].rep)
        state.children[i].findMyChildren()

    print("b3d ma l2oo 3ilahom")
    for i in range(7):
        print(state.children[i].rep)
        print("has x children : " + str(len(state.children[i].children)))

    #conv = Converter.Converter()
    #for child in state.children:
    #    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #    arr = conv.convertStateToArray(child.rep)
    #    for row in arr:
    #        print(row)


    # print(sys.getsizeof(state))
    # print(sys.getsizeof(state.rep))
    # x=5
    # print(sys.getsizeof(x))
    # for child in state.children:
    #     child.findMyChildren()
    #     print(len(child.children))
    # print(bin(state.rep))
