class Converter:

    def convertStateToArray(self,inState):
       # state = bin(state)
       #  print("works on ",inState)
        state = "{0:b}".format(inState)
        # print(state)
        rows, cols = (6, 7)
        arrayState = [['w' for i in range(cols)] for j in range(rows)]
        state = str(state)
        index = len(state)
        col = 0
        while col != 7:
            nextIndex = int(state[index - 3: index], 2)  # convert binary rep of empty space to decimal
            i = 0
            startIndex = index - 4
            while nextIndex != 0:
                if state[startIndex] == '0':
                    arrayState[i][col] = 'y'
                else:
                    arrayState[i][col] = 'r'
                startIndex = startIndex - 1
                i = i + 1
                nextIndex = nextIndex - 1

            index = index - 9
            col = col + 1

        return arrayState

    def convertArrayToState(self, arr):
        representation = ""
        rows = len(arr)
        columns = len(arr[0])
        for j in range(columns-1,-1,-1):
            index = 7
            for i in range(rows):
              #  print("i ", i, " j ", j)
                if arr[i][j] == 'w':
                    index = i
                    #print("find white at ", index)
                    break

           # print("start of spaces >> ", index)
            binary = "{0:03b}".format(index)
           # print("Binary representaion ", binary)



            for x in range(rows-1,-1,-1):
                if arr[x][j] == 'y':
                    representation += "0"
                else:
                    representation += "1"


            representation += binary
           # print("Board representaion ", representation)

        representation = int(representation,2)
        return representation


if __name__ == '__main__':
    conv = Converter()
    input =  int('111111000111111001111100011110111100111111001111000100111100010', 2)
    print(input)
    arr = conv.convertStateToArray(input)
  #  print(int(bin(111111000111111001111100011110111100111111001111000100111100010),2))
    for row in arr:
        print(row)

    state = conv.convertArrayToState(arr)
    print(state)

