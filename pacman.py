
import pygame
import sys
import time
import random

from pygame.locals import *

from allClass import *

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,20)



def main():

	g = game()
	print(g)

	ms = moveSelector()

	p = pac( g.startX, g.startY )

	while(True):
		nowMove = ms.getMove(g)
		if(nowMove == -1):
			nowMove = g.pac.d
		if(nowMove == 0):
			g.pac.move(1,0,g.map,0)
		elif(nowMove == 1):
			g.pac.move(0,-1,g.map,1)
		elif(nowMove == 2):
			g.pac.move(-1,0,g.map,2)
		elif(nowMove == 3):
			g.pac.move(0,1,g.map,3)

		for ghost in g.ghosts:
			nowMove = ghost.getMove(g)
			if(nowMove == 0):
				ghost.move(1,0,g.map,0)
			elif(nowMove == 1):
				ghost.move(0,-1,g.map,1)
			elif(nowMove == 2):
				ghost.move(-1,0,g.map,2)
			elif(nowMove == 3):
				ghost.move(0,1,g.map,3)			

		state = g.drawAll()
		if( state == 0 ):
			print("End! Scores = " + str(g.points) + ", Time = " + str(g.frameCnt//10) + "." + str(g.frameCnt%10))
			break
		elif(state == 2):
			print("Win! Scores = " + str(g.points) + ", Time = " + str(g.frameCnt//10) + "." + str(g.frameCnt%10))
			break


main()