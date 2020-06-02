#------#
#Import#
#------#

from pygame.locals import *
import pygame

#---------#
#Variables#
#---------#

BLUE    = (  0,  0,255)
RED     = (255,  0,  0)
YELLOW  = (255,255,  0)

board=[[0 for y in range(6)] for x in range(7)]

#---------#
#Fonctions#
#---------#

def main(board,done=False,size=(700,600)):
    player=0
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Puissance 4")
    tx,ty=(size[0]/7,size[1]/6)
    win=False
    try:
        while not done and not win:
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y]==0:
                        COLOR=BLUE
                        #ex,ey=(tx,ty)
                    if board[x][y]==1:
                        COLOR=YELLOW
                        #ex,ey=(tx//3,ty//3)
                    if board[x][y]==2:
                        COLOR=RED
                        #ex,ey=(tx//3,ty//3)
                    pygame.draw.rect(screen, COLOR, (x*tx,y*ty,tx-1,ty-1), 0)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True

                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    mx=int(event.pos[0]//tx)
                    my=int(event.pos[1]//ty)
                    ny=max_height(board[mx])
                    if ny!=None:
                        board[mx][ny]=player+1
                        player=(player+1)%2
                        win=check(board)
    finally:
        if win:
            player=(player+1)%2
            if player==0:
                print("Yellow wins")
            if player==1:
                print("Red wins")
        else:
            print("No one wins")
        pygame.quit()



def max_height(column):
    h=None
    for y in range(len(column)):
        if column[y]==0:
            h=y
    return h

def check(board):
    win=False
    for y in range(6):
        for x in range(4):
            if board[x][y]==board[x+1][y]==board[x+2][y]==board[x+3][y]!=0:
                win=True
    for y in range(3):
        for x in range(7):
            if board[x][y]==board[x][y+1]==board[x][y+2]==board[x][y+3]!=0:
                win=True
    for y in range(3):
        for x in range(4):
            if board[x][y]==board[x+1][y+1]==board[x+2][y+2]==board[x+3][y+3]!=0:
                win=True
            if board[x+3][y]==board[x+2][y+1]==board[x+1][y+2]==board[x][y+3]!=0:
                win=True
    return win

#-------#
#Actions#
#-------#

main(board)
