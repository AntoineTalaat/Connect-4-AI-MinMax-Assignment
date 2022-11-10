class Converter:

    def convertStateToArray(self, state):
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


if __name__ == '__main__':
    conv = Converter()
    arr = conv.convertStateToArray(111111000111111001111100011110111100111111001111000100111100010)
    for row in arr:
        print(row)
    '''
    def convertArrayToStarte(arr):
        representation = ""
        rows = len(arr)
        columns = len(arr[0])
        for j in range (columns):
           index = 7
           for i in range (rows):
               print("i ",i," j ",j)
               if arr[i][j] == 'w':

                   index = i
                   print("find white at ",index)
                   break

           print("start of spaces >> ",index)
           binary = "{0:03b}".format(index)
           print("Binary representaion ",binary)
           representation +=binary
           print("Board representaion ",representation)

           for x in range(index):
               if arr[x][j] == 'r':
                   representation+="1"
                   print(representation)
               elif arr[x][j] == 'y':
                   representation+="0"
                   print(representation)

        representation = int(representation)
        return representation

    '''
