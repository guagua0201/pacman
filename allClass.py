import pygame
from pygame.locals import *

import sys
import time
import random

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,20)


class pac:
	def __init__( self, _x, _y ):
		pac.x = _x
		pac.y = _y
		pac.img = []
		for i in range(4):
			pac.img.append("./pacman" + str(i) + ".png")
		pac.d = 0

	def move(self, dx, dy, m, dd):
		if( m[self.x + dx][self.y + dy] == 1):
			return
		self.x += dx
		self.y += dy
		self.d = dd


class game:
	def __init__( self ):
		pygame.init()

		# self.map = [ [1,1,1,1,1], [1,0,2,0,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1] ]

		self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
,[1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1]
,[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1]
,[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1]
,[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1]
,[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
,[1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1]
,[1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1]
,[1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1]
,[1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1]
,[0,0,0,0,0,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,0,0,0,0,0]
,[0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0]
,[0,0,0,0,0,1,2,1,1,0,1,1,1,0,0,1,1,1,0,1,1,2,1,0,0,0,0,0]
,[1,1,1,1,1,1,2,1,1,0,1,1,1,0,0,1,1,1,0,1,1,2,1,1,1,1,1,1]
,[1,2,2,2,2,2,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,2,2,2,2,2,1]
,[1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1]
,[0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0]
,[0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0]
,[0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0]
,[1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1]
,[1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1]
,[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1]
,[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1]
,[1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,1]
,[1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1]
,[1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1]
,[1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1]
,[1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1]
,[1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1]
,[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
,[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

		self.startX, self.startY = 1,1;

		self.fps = 10
		self.fpsClock = pygame.time.Clock()

		self.gridSize = (30,30)
		self.screenSize = ( (len(self.map) * self.gridSize[0]), (len(self.map[0]) * self.gridSize[1]) )


		self.screen = pygame.display.set_mode( self.screenSize, 0, 32)
		
		self.surf = pygame.Surface(self.screen.get_size()).convert()

		self.clock = pygame.time.Clock()

		pygame.key.set_repeat(1,40)

		self.surf.fill((0,0,0))

		self.screen.blit(self.surf, (0,0))

		self.frameCnt = 0

		self.pac = pac(self.startX, self.startY)


	def timeGrid(self, x,y):
		return (x * self.gridSize[0], y * self.gridSize[1])

	def drawObj(self, ob):
		avatar = pygame.image.load(ob.img[ob.d])
		avatar = pygame.transform.scale(avatar, self.gridSize)
		r = avatar.get_rect(topleft = ( self.timeGrid( ob.x, ob.y ) ))
		self.surf.blit(avatar, r)

	def drawRec(self, x, y, color):
		r = pygame.Rect(self.timeGrid(x, y), self.gridSize)
		pygame.draw.rect(self.surf, color, r)

	def drawImg(self, x, y, fileName):
		avatar = pygame.image.load(fileName)
		avatar = pygame.transform.scale(avatar, self.gridSize)
		r = avatar.get_rect( topleft = self.timeGrid(x,y) )
		self.surf.blit(avatar,r)
	def drawMap(self):
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if(self.map[i][j] == 1):
					self.drawRec(i,j,(0,0,255))
				elif(self.map[i][j] == 2):
					self.drawImg(i,j,"point.png")

	def drawAll(self):
		self.surf.fill((0,0,0))


		# self.drawMap()
		self.drawMap()
		self.drawObj(self.pac)

		# for ghost in self.ghosts:
		# 	self.draw(self.ghost)
		self.screen.blit(self.surf, (0,0))

		
		
		pygame.display.flip()
		pygame.display.update()
		self.fpsClock.tick(self.fps)
		self.frameCnt += 1


class moveSelector:


	def getMove(self, g):
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if(event.key == pygame.K_UP):
					g.pac.move(0,-1,g.map,1)
				elif(event.key == pygame.K_DOWN):
					g.pac.move(0,1,g.map,3)
				elif(event.key == pygame.K_RIGHT):
					g.pac.move(1,0,g.map,0)
				elif(event.key == pygame.K_LEFT):
					g.pac.move(-1,0,g.map,2)
