import Converter
import State


class MinMax:

    def buildKLevels(self, k, currentState):
        if k != 0:
            currentState.findMyChildren()
            k = k - 1
            for i in range(len(currentState.children)):
                self.buildKLevels(k, currentState.children[i])

    def maxValue(self, k, state, withAlphaBeta):
        v = float('-inf')
        for child in state.children:
            value, futureMove = self.MinMax2(k - 1, child, withAlphaBeta, False)
            if value > v:
                v = value
                move = child
            if withAlphaBeta and value >= state.beta:
                return (value, move)
            if withAlphaBeta:
                state.beta = max(state.alpha, value)
        return (v, move)

    def minValue(self, k, state, withAlphaBeta):
        v = float('inf')

        for child in state.children:
            value, futureMove = self.MinMax2(k - 1, child, withAlphaBeta, True)
            if value < v:
                v = value
                move = child
            if withAlphaBeta and v <= state.alpha:
                return v, move
            if withAlphaBeta:
                state.beta = min(state.beta, v)

        return (v, move)
    '''
        def MinMax(self, k, currentState, withAlphaBeta):
            self.buildKLevels(k, currentState)
            if k == 0:
                return currentState.getScore()
            if currentState.max:
                v, move = self.minValue(currentState)
            else:
                v, move = self.maxValue(currentState)
    
            return move
    '''
    def MinMax2(self, k, currentState, withAlphaBeta, isAITurn):
        currentState.findMyChildren()

      #  print("State Start: " + str(currentState.rep))
        # self.buildKLevels(k, currentState)
      #  print(currentState.children.__len__())
        if k == 0:
            return currentState.getScore(), currentState
        if not isAITurn:
            v, move = self.minValue(k, currentState, withAlphaBeta)
        else:
            v, move = self.maxValue(k, currentState, withAlphaBeta)
        # print()
        # print(v)
        return v, move


if __name__ == '__main__':
    s = State.State()
    conv = Converter.Converter()
    s.rep = int('111111000111111001111100011110111100111111001111000100111100010', 2)
    arr = conv.convertStateToArray(s.rep)
    for row in arr:
        print(row)

    s.max = False
    algo = MinMax()
    value, move = algo.MinMax2(4, s, False, True)

    arr = conv.convertStateToArray(move.rep)
    for row in arr:
        print(row)
    # algo.MinMax2(k=3,currentState=s,withAlphaBeta=False,isAITurn=True)
