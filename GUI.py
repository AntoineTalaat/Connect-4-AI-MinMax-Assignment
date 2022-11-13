import numpy as np
import pygame
import sys
import math

from Heuristic import Heuristic
from MinMax import*
import State
import Converter
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (232, 14, 14)
YELLOW = (238, 227, 78)
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE


class Game:
    def create_board(self):
        board = [['w' for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
        return board

    def drop_piece(self, board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(self, board, col):
        return board[ROW_COUNT - 1][col] == 'w'

    def get_next_open_row(self, board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 'w':
                return r

    def winning_move(self, board, piece):
        score = 0
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    score += 1
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][ c] == piece:
                    score += 1
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    score += 1
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    score += 1
        return score

    def print_board(self, board):
        print(np.flip(board, 0))

    def draw_board(self, board):
        # Button(330, 450, 100, 50, "Step forward", RED, YELLOW, 15).draw(screen)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE,
                                 (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 'r':
                    pygame.draw.circle(self.screen, RED, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                elif board[r][c] == 'y':
                    pygame.draw.circle(self.screen, YELLOW, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
        pygame.display.flip()
    def start_window(self):
        pygame.init()
        size = (width, height)
        self.screen = pygame.display.set_mode(size)
        self.start = True
        self.game_over = False
    def new(self):

        self.game_over = False
        self.finish = False
        self.turn = 0
        self.turns = 42
        self.player_1_Score = 0
        self.player_2_Score = 0


        if self.start == False:
            self.board = self.create_board()
            self.print_board(self.board)
            self.draw_board(self.board)


    def printBoardConsole(self,board):
        print()
        for row in range(0, len(board)):
            print(board[len(board) - row - 1])
        print()
    def gameloop(self):
        self.start_window()
       # self.new()

        # pygame.display.update()

        myfont = pygame.font.SysFont("monospace", 30)

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.start:
                     if event.type == pygame.KEYUP:
                         if event.key == pygame.K_s:
                             self.start =False
                             self.new()
                             print("S")
                else:
                    if self.finish:
                        if event.type == pygame.KEYUP:
                            if event.key == 110:
                                print("N")
                                self.new()
                    else:
                        if event.type == pygame.MOUSEMOTION:
                             pygame.draw.rect(self.screen, BLACK, (0,0, width, SQUARESIZE))
                             posx = event.pos[0]
                             if self.turn == 0:
                                 pygame.draw.circle(self.screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
                             else:
                                pygame.draw.circle(self.screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                             pygame.display.flip()    
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pygame.draw.rect(self.screen, BLACK, (0, 0, width, SQUARESIZE))

                            if self.turn == 0:
                                posx = event.pos[0]
                                col = int(math.floor(posx / SQUARESIZE))

                                if self.is_valid_location(self.board, col):
                                    row = self.get_next_open_row(self.board, col)
                                    self.drop_piece(self.board, row, col, 'r')
                                    self.turns -= 1
                                    self.draw_board(self.board)
                                    s = State.State()
                                    conv = Converter.Converter()
                                    print("sending this to algorithm")
                                    self.printBoardConsole(self.board)

                                    s.rep = conv.convertArrayToState(self.board)
                                    print(bin(s.rep))
                                    print("run algo")
                                    algo = MinMax()
                                    value, move = algo.MinMax(5, s, False, True)

                                    self.board = conv.convertStateToArray(move.rep)
                                    h = Heuristic(self.board)
                                    print("The Heuristic of the screen as a value = " ,h.getHeuristicScore())

                                    self.printBoardConsole(self.board)
                                    self.turns -= 1

                           #     posx = event.pos[0]
                            #    col = int(math.floor(posx / SQUARESIZE))

                             #   if self.is_valid_location(self.board, col):
                              #      row = self.get_next_open_row(self.board, col)
                               #     self.drop_piece(self.board, row, col, 'y')
                                   
                                   
                                    

                            self.draw_board(self.board)

                            if self.turns == 0:
                                self.finish = True
                                self.player_1_Score = self.winning_move(self.board, 'r')
                                self.player_2_Score = self.winning_move(self.board, 'y')
                                print(self.player_1_Score, self.player_2_Score)
                                label = myfont.render("Red score = " + str(self.player_1_Score), 1, RED)
                                label2 = myfont.render("Yellow score = " + str(self.player_2_Score), 1, YELLOW)
                                self.screen.blit(label, (10, 10))
                                self.screen.blit(label2, (10, 60))
                                self.draw_board(self.board)
                                pygame.display.update()

                            

                            if self.finish:
                                # pygame.time.wait(5000)
                                # game_over = False
                                # board = self.create_board()
                                # self.draw_board(board)
                                turn = 0
                                turns = 42



game = Game()
game.gameloop()