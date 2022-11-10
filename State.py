class State:
    rep = 111111000111111000111111000111111000111111000111111000111111000
    #alpha = int('-inf')
    #beta = int ('int')

    def changeBit(self, pos, bit):
        mask = 1 << pos
        self.rep =(self.rep & ~mask) | ((bit << pos) & mask)

    def addToColumn (self, col, playerColour):
        print(bin(self.rep))
        chunckShift = col*9
        temp = 7 << chunckShift
        indexPlace = self.rep & temp

        print("Temp ",bin(temp))
        print("Temp ",len( bin(temp)))
        print("inde ", bin(indexPlace))
        print("index ",indexPlace)

        position =chunckShift + indexPlace + 3
        print(position)

        # Modify the bit it self
        if playerColour=='y':
            self.changeBit(position, 0)
        elif playerColour =='r':
            self.changeBit(position, 1)

        print(self.rep)

        # modify the index in representation
        binary = "{0:03b}".format(indexPlace)    #101
        for i in range(len(binary)):
            self.changeBit(chunckShift+i,int(binary[i]))

if __name__ == '__main__':
    state = State()
    state.rep = 111111000111111001111100011110111100111111001111000100111100010
    state.addToColumn(6,'y')
    print("????????????????????",state.rep)

    '''
        def addTOColumn (self,col,playerColour):
            temp = str(self.rep)
            print(temp)
            chunckShift = (6-col) * 9
            indexPlaceBinary = temp[chunckShift+6 : chunckShift+9]
            print(indexPlaceBinary)

            if playerColour == 'y':

            elif playerColour == 'r':
    '''















