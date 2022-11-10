
class Converter:
    def convertStateToArray(self, state):
        rows, cols = (6, 7)
        arrayState = [['white' for i in range(cols)] for j in range(rows)]
        state = str(state)
        index = 0
        col = 0
        while col != 7:
            print(state[index: index+3])
            emptyIndex = int(state[index: index+3], 2)  # convert binary rep of empty space to decimal

            if emptyIndex != 0:
                for i in range(0, emptyIndex - 1):
                    print("d5alt")
                    if state[index + i] == '0':
                        arrayState[i][col] = 'yellow'
                    else:
                        arrayState[i][col] = 'red'
            index = index + emptyIndex + 2
            col = col + 1
            for row in arrayState:
                print(row)
        return arrayState


if __name__ == '__main__':
    conv = Converter()
    arr = conv.convertStateToArray(101110001010000100100001000000)


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






