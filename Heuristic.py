import sys


class Window:
    yellows = 0
    reds = 0

    def __init__(self):
        yellows = 0
        reds = 0

    def getWindowScore(self):
        if self.reds > 0 and self.yellows > 0:
            return 0
        ## print(self.reds - self.yellows)
        return self.reds - self.yellows

    def addToWindow(self, input):
        ## print("window now " + str(self.reds) + " " + str(self.yellows))
        if input == 'y':
            self.yellows = self.yellows + 1
        elif input == 'r':
            self.reds = self.reds + 1

    def removeFromWindow(self, out):
        if out == 'y':
            self.yellows = self.yellows - 1
        elif out == 'r':
            self.reds = self.reds - 1


class Heuristic:
    stateBoard = [[]]
    redCount = [0, 0, 0, 0, 0]
    yellowCount = [0, 0, 0, 0, 0]
    colorAI = ''

    def __init__(self, color, board):
        self.colorAI = color
        self.stateBoard = board

    def updateCounters(self, partialScore):
        ## print("score is " + str(partialScore))

        if (partialScore > 0):
            self.redCount[partialScore] = self.redCount[partialScore] + 1
        elif (partialScore < 0):
            s = partialScore * (-1)
            self.yellowCount[s] = self.yellowCount[s] + 1

    # def checkColumns(self):
    #     for x in range(0, len(self.stateBoard[0])):
    #         window = Window()
    #         for y in range(0, 4):  # starting window
    #             window.addToWindow(self.stateBoard[y][x])
    #         self.updateCounters(window.getWindowScore())
    #         for y in range(0, len(self.stateBoard) - 4):
    #             elemOut = self.stateBoard[y][x]
    #             elemIn = self.stateBoard[y + 4][x]
    #             window.removeFromWindow(elemOut)
    #             window.addToWindow(elemIn)
    #             self.updateCounters(window.getWindowScore())
    #
    # def checkRows(self):
    #     for y in range(0, len(self.stateBoard)):
    #         window = Window()
    #         for x in range(0, 4):  # starting window
    #             window.addToWindow(self.stateBoard[y][x])
    #         self.updateCounters(window.getWindowScore())
    #         for x in range(0, len(self.stateBoard[0]) - 4):
    #             elemOut = self.stateBoard[y][x]
    #             elemIn = self.stateBoard[y][x + 4]
    #             window.removeFromWindow(elemOut)
    #             window.addToWindow(elemIn)
    #             self.updateCounters(window.getWindowScore())

    def checkLine(self, startx, starty, dx, dy):
        counter = 0
        y = starty
        x = startx
        window = Window()
        while x < len(self.stateBoard[0]) and y < len(self.stateBoard) and x >= 0 and y >= 0:
            ## print("Checking "+str(x) + " " + str(y))
            counter = counter + 1
            window.addToWindow(self.stateBoard[y][x])
            if (counter > 4):
                window.removeFromWindow(self.stateBoard[y - 4 * dy][x - 4 * dx])
                self.updateCounters(window.getWindowScore())
            elif (counter == 4):
                self.updateCounters(window.getWindowScore())
            x = x + dx
            y = y + dy

    def checkDownwardDiagonals(self):
        for i in range(len(self.stateBoard)):
          #  print("Checking downdiagonal startin at: 0," + str(i))
            self.checkLine(0, i, 1, -1)
          #  print(self.redCount)
          #  print(self.yellowCount)
        for i in range(1, len(self.stateBoard[0])):
          #  print("Checking downdiagonal startin at: " + str(i) + ",size-1")

            self.checkLine(i, len(self.stateBoard) - 1, 1, -1)
          #  print(self.redCount)
          #  print(self.yellowCount)

    def checkUpwardDiagonals(self):
        for i in range(len(self.stateBoard)):
          #  print("Checking updiagonal startin at: 0," + str(i))
            self.checkLine(0, i, 1, 1)
          #  print(self.redCount)
          #  print(self.yellowCount)
        for i in range(1, len(self.stateBoard[0]) ):
          #  print("Checking updiagonal startin at: " + str(i) + ",0")
            self.checkLine(i, 0, 1, 1)
          #  print(self.redCount)
          #  print(self.yellowCount)

    def checkDiagonals(self):
        ## print("Diags")

        self.checkUpwardDiagonals()
        self.checkDownwardDiagonals()

    def checkRows(self):
        ## print("ROWS")
        for i in range(0, len(self.stateBoard)):
            self.checkLine(0, i, 1, 0)

    def checkColumns(self):
        ## print("COLS")

        for i in range(0, len(self.stateBoard[0])):
            self.checkLine(i, 0, 0, 1)

    def getHeuristicScore(self):
        self.checkColumns()
        self.checkRows()
      #  print(self.redCount)
      #  print(self.yellowCount)
        self.checkDiagonals()

        print(self.redCount)
        print(self.yellowCount)
        score = self.redCount[4]*20 - self.yellowCount[4]*20
        score = score + self.redCount[3]*9 - self.yellowCount[3]*9
        score = score + self.redCount[2]*3 - self.yellowCount[2]*3
        score = score + self.redCount[1]   - self.yellowCount[1]
        return score


if __name__ == '__main__':
    board = []
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'y'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['w', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['y', 'w', 'w', 'w', 'w', 'w', 'w'])
    board.insert(0, ['r', 'r', 'r', 'r', 'r', 'r', 'r'])

    # print(board)
    # print(len(board))
    # print(len(board[0]))

    h = Heuristic('', board)
    h.getHeuristicScore()
    # str = "wwwwwwwrrrrrrryyyyyyywwwwwwwrrrrrrryyyyyyy"
    # x = sys.getsizeof(str)
    ## print(x)
    #
    # y = 1
    # long
