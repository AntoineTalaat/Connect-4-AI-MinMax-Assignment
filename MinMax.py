import math
import Converter
import State
from treelib import Node, Tree


class MinMax:
    AIcolor = 'y'
    expandedNodes = 0
    tree = Tree()
    conv = Converter.Converter()

    def maxValue(self, k, state, withAlphaBeta, alpha , beta):
        self.expandedNodes=self.expandedNodes+1
        v = float('-inf')

        move = None
        if k == 0 or state.isFull():
            return state.getScore(self.AIcolor), state
        children = state.findMyChildren()

        for child in children:
            self.tree.create_node(self.conv.convertStateToString(child.rep), child, parent=state)
            value, futureMove = self.minValue(k - 1, child, withAlphaBeta,alpha,beta)
            self.tree.update_node(child, tag=self.conv.convertStateToString(child.rep) + " : " + str(value))
            if value > v:
                v = value
                move = child

            if withAlphaBeta :
                alpha = max(alpha, value)
            if withAlphaBeta and alpha>=beta:
                return (v, move)

        return (v, move)

    def minValue(self, k, state, withAlphaBeta , alpha, beta):
        self.expandedNodes = self.expandedNodes + 1
        v = float('inf')
        move = None
        if k == 0 or state.isFull():
            return state.getScore(self.AIcolor), state
        children = state.findMyChildren()
        for child in children:
            self.tree.create_node(self.conv.convertStateToString(child.rep), child, parent=state)
            value, futureMove = self.maxValue(k - 1, child, withAlphaBeta,alpha,beta)
            self.tree.update_node(child, tag=self.conv.convertStateToString(child.rep) + " : " + str(value))
            if value < v:
                v = value
                move = child
            if withAlphaBeta:
                beta = min(beta, v)
            if withAlphaBeta and alpha>=beta:
                return v, move
        return (v, move)

    def MinMax(self, k, currentState, withAlphaBeta, userColor) -> (int,State):
        if(userColor=='y'):
            self.AIcolor='r'
        alpha = -math.inf
        beta = math.inf
        self.tree = Tree()
        self.tree.create_node(self.conv.convertStateToString(currentState.rep), currentState)
        v, move = self.maxValue(k, currentState, withAlphaBeta,alpha,beta)
        self.tree.update_node(currentState, tag=self.conv.convertStateToString(currentState.rep) + " : " + str(v))
        return v, move
