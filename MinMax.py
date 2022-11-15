import math

import State
from treelib import Node, Tree


class MinMax:
    AIcolor = 'y'
    tree = Tree()

    def maxValue(self, k, state, withAlphaBeta, alpha , beta):
        v = float('-inf')

        move = None
        if k == 0 or state.isFull():
            return state.getScore(self.AIcolor), state
        children = state.findMyChildren()

        for child in children:
            value, futureMove = self.minValue(k - 1, child, withAlphaBeta,alpha,beta)
            if value > v:
                v = value
                move = child

            if withAlphaBeta :
                alpha = max(alpha, value)
            # print(v , " >= " , beta)
            if withAlphaBeta and alpha>=beta:
                # print("PRUNED in max")
                return (v, move)

        return (v, move)

    def minValue(self, k, state, withAlphaBeta , alpha, beta):
        v = float('inf')
        move = None
        if k == 0 or state.isFull():
            return state.getScore(self.AIcolor), state
        children = state.findMyChildren()

        for child in children:
            value, futureMove = self.maxValue(k - 1, child, withAlphaBeta,alpha,beta)
            if value < v:
                v = value
                move = child
            if withAlphaBeta:
                beta = min(beta, v)
            # print(v , " <= " , alpha)
            if withAlphaBeta and alpha>=beta:
                # print("PRUNED in min")
                return v, move
        return (v, move)

    def MinMax(self, k, currentState, withAlphaBeta, userColor) -> (int,State):
        if(userColor=='y'):
            self.AIcolor='r'
        alpha = -math.inf
        beta = math.inf
        v, move = self.maxValue(k, currentState, withAlphaBeta,alpha,beta)
        return v, move
