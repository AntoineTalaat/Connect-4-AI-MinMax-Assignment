import State
from treelib import Node, Tree


class MinMax:
    AIcolor = 'y'
    tree = Tree()

    def maxValue(self, k, state, withAlphaBeta, userColor):
        v = float('-inf')
        move = None
        children = state.findMyChildren()
        '''
        print("Tree")
        for child in children:
            print(bin(child.rep))
        print(">>>>>>>>")
        '''



        for child in children:
            value, futureMove = self.MinMax(k - 1, child, withAlphaBeta, False,userColor)
            if value > v:
                v = value
                move = child
            if withAlphaBeta and v >= state.beta:
                return (value, move)
            if withAlphaBeta:
                state.alpha = max(state.alpha, value)
        return (v, move)

    def minValue(self, k, state, withAlphaBeta, userColor):
        v = float('inf')
        move = None
        children = state.findMyChildren()
        '''
        print("Tree")
        for child in children:
            print(bin(child.rep))
        print(">>>>>>>>")
        '''
        for child in children:
            value, futureMove = self.MinMax(k - 1, child, withAlphaBeta, True, userColor)
            if value < v:
                v = value
                move = child
            if withAlphaBeta and v <= state.alpha:
                return v, move
            if withAlphaBeta:
                state.beta = min(state.beta, v)

        return (v, move)

    def MinMax(self, k, currentState, withAlphaBeta, isAITurn, userColor) -> (int,State):
        if(userColor=='y'):
            self.AIcolor='r'

        if k == 0 or currentState.isFull():
            return currentState.getScore(self.AIcolor), currentState
        if not isAITurn:
            v, move = self.minValue(k, currentState, withAlphaBeta,userColor)
        else:
            v, move = self.maxValue(k, currentState, withAlphaBeta,userColor)

        return v, move
