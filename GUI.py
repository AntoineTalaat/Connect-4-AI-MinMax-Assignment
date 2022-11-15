import numpy as np
import pygame
import sys
import math
import time

from Heuristic import Heuristic
from MinMax import*
import State
import Converter
from button import*
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
    colorUser='r'
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
        self.turn = any
        self.alphaBeta = any
        self.screen = pygame.display.set_mode(size)
        self.start = True
        self.game_over = False
        self.base_font = pygame.font.SysFont("Consolas", 24)
        self.user_text=''
        self.input_txt = pygame.Rect(100,200,140,32)
        pygame.draw.rect(self.screen,(255,255,255),self.input_txt,2)
        self.text = self.base_font.render('K level pruning', True, MINTGREEN)
        self.screen.blit(self.text,(100,150))
        button1  =Button(100, 400, 200, 50, "Red", RED, BLACK,30)
        button2  =Button(400, 400, 200, 50, "Yellow", YELLOW, BLACK,30)
        self.button_list=[]
        self.button_list.append(button1)
        self.button_list.append(button2)
        button1.draw(self.screen)
        button2.draw(self.screen)
        self.text2 = self.base_font.render('Alpha-beta pruning:', True, MINTGREEN)
        self.screen.blit(self.text2,(400,150))
        checkbox1 = Checkbox(self.screen , 400,200, 0, caption='YES' ,font_color= (255,255,255), font_size=30)
        checkbox2 = Checkbox(self.screen, 400, 250, 1, caption='NO' ,font_color= (255,255,255), font_size=30)
        self.boxes=[]
        self.boxes.append(checkbox1)
        self.boxes.append(checkbox2)
        for box in self.boxes:
            box.render_checkbox()  
           
        pygame.display.flip()
    def new(self):
        
        self.game_over = False
        self.finish = False
        
        self.turns = 42
        self.player_1_Score = 0
        self.player_2_Score = 0
        self.avgTime = 0
        self.expandedNodes = 0
       
        

        if self.start == False:
            self.board = self.create_board()
            self.print_board(self.board)
            self.draw_board(self.board)

        if self.turn == 1:
            s = State.State()
            s.max=False
            conv = Converter.Converter()
            s.rep = conv.convertArrayToState(self.board)
            algo = MinMax()
            start = time.time()
            value, move = algo.MinMax(int(self.user_text), s, self.alphaBeta,self.colorUser)
            end = time.time()
            self.avgTime+= (end - start)
            self.expandedNodes += algo.expandedNode
            print("Expanded Nodes: ", self.expandedNodes)
            self.board = conv.convertStateToArray(move.rep)
            h = Heuristic(self.board)
            print("The Heuristic of the screen as a value = " ,h.getHeuristicScore())
            self.printBoardConsole(self.board)
            self.turns -= 1
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
                         if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                         else:
                             if (event.key == pygame.K_0 or event.key == pygame.K_1  or event.key ==pygame.K_2 or event.key ==pygame.K_3 or event.key ==pygame.K_4 or event.key ==pygame.K_5 or event.key ==pygame.K_6 or event.key ==pygame.K_7 or event.key ==pygame.K_8 or event.key == pygame.K_KP_0 or event.key == pygame.K_KP_1  or event.key ==pygame.K_KP_2 or event.key ==pygame.K_KP_3 or event.key ==pygame.K_KP_4 or event.key ==pygame.K_KP_5 or event.key ==pygame.K_KP_6 or event.key ==pygame.K_KP_7 or event.key ==pygame.K_KP_8 ) and len(self.user_text)<9 : 
                                 self.user_text+= event.unicode   
                                 self.text_surface = self.base_font.render(self.user_text,True,(255,255,255))
                                 self.screen.blit(self.text_surface,(self.input_txt.x+5,self.input_txt.y+5))
                                 pygame.display.flip()
                                 print(self.user_text) 
                     if event.type== pygame.MOUSEBUTTONDOWN:
                         mouse_x, mouse_y = pygame.mouse.get_pos()
                         for button in self.button_list:
                            if button.click(mouse_x,mouse_y):
                                if button.text== "Red":
                                     for method in self.boxes:
                                         if(method.checked == True and self.user_text != ''): 
                                            if method.caption== "YES":
                                                self.alphaBeta = True
                                            if method.caption == "NO":
                                                self.alphaBeta=False
                                
                                            self.start =False
                                            self.colorUser='r'

                                            self.turn=0
                                            self.new()
                                          
                                if button.text== "Yellow":
                                     for method in self.boxes:
                                         if(method.checked == True and self.user_text != ''): 
                                            if method.caption== "YES":
                                                self.alphaBeta = True
                                            if method.caption == "NO":
                                                self.alphaBeta=False                                    
                                            self.start =False
                                            self.turn=1
                                            self.colorUser='y'
                                            self.new()
                                     
                                     print("Yellow") 
                         if self.start:            
                             for box in self.boxes:
                                box.update_checkbox(event)
                                if box.checked is True:
                                   print(box.caption)
                                   for b in self.boxes:
                                        if b != box:
                                            b.checked = False 
                                   for box in self.boxes:
                                        box.render_checkbox()
                                        pygame.display.flip()          
                                           

                            
                                  
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

                            
                                posx = event.pos[0]
                                col = int(math.floor(posx / SQUARESIZE))

                                if self.is_valid_location(self.board, col):
                                    row = self.get_next_open_row(self.board, col)
                                    s = State.State()
                                    if self.turn == 0:
                                        self.drop_piece(self.board, row, col, 'r')
                                        s.max = True
                                    else:
                                        self.drop_piece(self.board, row, col, 'y')
                                        s.max =False

                                    self.turns -= 1
                                    self.draw_board(self.board)
                                    conv = Converter.Converter()
                                    print("sending this to algorithm")
                                    self.printBoardConsole(self.board)

                                    s.rep = conv.convertArrayToState(self.board)
                                    print(bin(s.rep))
                                    print("run algo")
                                    algo = MinMax()
                                    start = time.time()
                                    value, move = algo.MinMax(int(self.user_text), s, self.alphaBeta,self.colorUser)
                                    end = time.time()
                                    self.avgTime+= (end - start)
                                    self.expandedNodes += algo.expandedNode
                                    print("Expanded Nodes: ", self.expandedNodes)
                                    self.board = conv.convertStateToArray(move.rep)
                                    h = Heuristic(self.board)
                                    print("The Heuristic of the screen as a value = " ,h.getHeuristicScore())

                                    self.printBoardConsole(self.board)
                                    if self.turns !=0:
                                        self.turns -= 1
                             
                                self.draw_board(self.board)

                                if self.turns == 0:
                                    self.finish = True
                                    self.player_1_Score = self.winning_move(self.board, 'r')
                                    self.player_2_Score = self.winning_move(self.board, 'y')
                                    print(self.player_1_Score, self.player_2_Score)
                                    label = myfont.render("Red = " + str(self.player_1_Score), 1, RED)
                                    label2 = myfont.render("Yellow = " + str(self.player_2_Score), 1, YELLOW)
                                    label3 = myfont.render("Avg time = " + str(round((self.avgTime/21),3)) + " sec", 1, (255,255,255))
                                    label4 = myfont.render("Expanded Nodes " + str(self.expandedNodes), 1, MINTGREEN)
                                    self.screen.blit(label, (10, 10))
                                    self.screen.blit(label2, (10, 60))
                                    self.screen.blit(label3, (300, 60))
                                    self.screen.blit(label4,(300,10))
                                    self.draw_board(self.board)
                                    pygame.display.update()






game = Game()
game.gameloop()