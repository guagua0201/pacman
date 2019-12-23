
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

		g.drawAll()

		


main()