import pygame
from pygame.locals import *

import sys
import time
import random


import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,20)


class pac:
	def __init__( self, _x, _y ):
		self.x = _x
		self.y = _y
		self.img = []
		for i in range(4):
			self.img.append("./pacman" + str(i) + ".png")
		self.d = 0

	def move(self, dx, dy, m, dd):
		self.d = dd
		if( m[self.x + dx][self.y + dy] == 1):
			return
		self.x += dx
		self.y += dy

	def backMove(self, g):
		dx, dy = 0,0
		if(self.d == 0):
			dx,dy = (1,0)
		elif(self.d == 1):
			dx,dy = (0,-1)
		elif(self.d == 2):
			dx,dy = (-1,0)
		elif(self.d == 3):
			dx,dy = (0,1)
		dx,dy = -dx,-dy
		if(g.map[self.x + dx][self.y + dy] == 1):
			return (self.x, self.y)
		else:
			return (self.x + dx, self.y + dy)

class ghostBFS:
	def __init__(self, _x, _y, imgPrefix = "ghost1_"):
		self.x = _x
		self.y = _y
		self.img = []
		for i in range(4):
			self.img.append( imgPrefix + str(i) + ".png")
		self.d = 0
	def backMove(self, g):
		dx, dy = 0,0
		if(self.d == 0):
			dx,dy = (1,0)
		elif(self.d == 1):
			dx,dy = (0,-1)
		elif(self.d == 2):
			dx,dy = (-1,0)
		elif(self.d == 3):
			dx,dy = (0,1)
		dx,dy = -dx,-dy
		if(g.map[self.x + dx][self.y + dy] == 1):
			return (self.x, self.y)
		else:
			return (self.x + dx, self.y + dy)

	def move(self, dx, dy, m, dd):
		self.d = dd
		if( m[self.x + dx][self.y + dy] == 1):
			return
		self.x += dx
		self.y += dy
	def getMove(self, g):
		dizzyRate = 30
		r = random.randint(1,100)
		if(r<=dizzyRate):
			return random.randint(0,3)
		q = []
		qPtr = 0
		dis = []
		for i in range( len(g.map) ):
			dis.append([])
			for j in range(len(g.map[0])):
				dis[i].append(10000)
		dis[g.pac.x][g.pac.y] = 0
		q.append((g.pac.x, g.pac.y))
		while(qPtr < len(q)):
			nowX,nowY = q[qPtr]
			qPtr += 1
			for i in range(4):
				dx, dy = 0,0
				if(i == 0):
					dx,dy = (1,0)
				elif(i == 1):
					dx,dy = (0,-1)
				elif(i == 2):
					dx,dy = (-1,0)
				elif(i == 3):
					dx,dy = (0,1)
				if( g.map[nowX+dx][nowY+dy] != 1 and dis[nowX + dx][nowY + dy] > dis[nowX][nowY]+1 ):
					dis[nowX+dx][nowY + dy] = dis[nowX][nowY] + 1
					q.append( (nowX+dx,nowY+dy))

		for i in range(4):
			dx, dy = 0,0
			if(i == 0):
				dx,dy = (1,0)
			elif(i == 1):
				dx,dy = (0,-1)
			elif(i == 2):
				dx,dy = (-1,0)
			elif(i == 3):
				dx,dy = (0,1)
			if( dis[self.x + dx][self.y + dy] + 1 == dis[self.x][self.y]):
				return i


class ghostRandom:
	def __init__(self, _x, _y, imgPrefix = "ghost1_"):
		self.x = _x
		self.y = _y
		self.img = []
		for i in range(4):
			self.img.append( imgPrefix + str(i) + ".png")
		self.d = 0
	def backMove(self, g):
		dx, dy = 0,0
		if(self.d == 0):
			dx,dy = (1,0)
		elif(self.d == 1):
			dx,dy = (0,-1)
		elif(self.d == 2):
			dx,dy = (-1,0)
		elif(self.d == 3):
			dx,dy = (0,1)
		dx,dy = -dx,-dy
		if(g.map[self.x + dx][self.y + dy] == 1):
			return (self.x, self.y)
		else:
			return (self.x + dx, self.y + dy)

	def move(self, dx, dy, m, dd):
		self.d = dd
		if( m[self.x + dx][self.y + dy] == 1):
			return
		self.x += dx
		self.y += dy
	def getMove(self, g):

		disX = g.pac.x - self.x
		disY = g.pac.y - self.y

		prob = [50,30,15,5]
		# prob = [25,25,25,25]
		arr = []
		if( abs(disY) > abs(disX) ):
			if(disY > 0):
				arr.append(3)
				if(disX > 0):
					arr.append(0)
					arr.append(2)
				else:
					arr.append(2)
					arr.append(0)
				arr.append(1)
			else:
				arr.append(1)
				if(disX > 0):
					arr.append(0)
					arr.append(2)
				else:
					arr.append(2)
					arr.append(0)
				arr.append(3)
		else:
			if(disX > 0):
				arr.append(0)
				if(disY > 0):
					arr.append(3)
					arr.append(1)
				else:
					arr.append(1)
					arr.append(3)
				arr.append(2)
			else:
				arr.append(2)
				if(disY > 0):
					arr.append(3)
					arr.append(1)
				else:
					arr.append(1)
					arr.append(3)
				arr.append(0)

		lim = 0
		dd = [ (1,0), (0,-1), (-1,0), (0,1)]
		for i in range(4):
			j = arr[i]
			if( g.map[self.x + dd[j][0]][self.y + dd[j][1]] != 1 ):
				lim += prob[i]
		r = random.randint(1,lim)
		tmp = 0
		for i in range(4):	
			j = arr[i]
			if( g.map[self.x + dd[j][0]][self.y + dd[j][1]] != 1 ):	
				tmp += prob[i]
				if(tmp >= r):
					return j
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

		self.clearPoints = 0
		for i in range( len(self.map) ):
			for j in range( len(self.map[0]) ):
				if(self.map[i][j] == 2):
					self.clearPoints += 1

		self.startX, self.startY = 17,14;
		self.ghostStartX = [15,15] #two ghosts
		self.ghostStartY = [11,16]

		# self.ghostStartX = [15] #one ghost
		# self.ghostStartY = [11]


		self.fps = 10
		self.fpsClock = pygame.time.Clock()

		self.gridSize = (30,30)
		self.screenSize = ( (len(self.map) * self.gridSize[0]) + 300, (len(self.map[0]) * self.gridSize[1]) )


		self.screen = pygame.display.set_mode( self.screenSize, 0, 32)
		
		self.surf = pygame.Surface(self.screen.get_size()).convert()

		self.clock = pygame.time.Clock()

		pygame.key.set_repeat(1,40)

		self.surf.fill((0,0,0))

		self.screen.blit(self.surf, (0,0))

		self.frameCnt = 0

		self.points = 0

		self.pac = pac(self.startX, self.startY)
		self.ghosts = []
		for i in range(len(self.ghostStartX)):
			self.ghosts.append(ghostBFS(self.ghostStartX[i], self.ghostStartY[i]))


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

	def checkEatPoint(self):
		# print("yo ",self.pac.x, self.pac.y, self.map[self.pac.x][self.pac.y])
		if(self.map[self.pac.x][self.pac.y] == 2):
			self.points += 1
			self.map[self.pac.x][self.pac.y] = 0
			# print("+1!",self.points)

	def checkGhost(self):
		for ghost in self.ghosts:
			if(ghost.x == self.pac.x and ghost.y == self.pac.y):
				return 1
			if(ghost.backMove(self) == (self.pac.x, self.pac.y) and self.pac.backMove(self) == (ghost.x, ghost.y)):
				return 1
		return 0

	def drawAll(self):
		self.surf.fill((0,0,0))


		# self.drawMap()
		self.drawMap()
		self.drawObj(self.pac)

		for ghost in self.ghosts:
			self.drawObj(ghost)

		self.checkEatPoint()
		if(self.checkGhost()):
			return 0

		if(self.points == self.clearPoints):
			return 2

		font = pygame.font.Font(None, 50)
		text1= font.render( str(self.points), 10, (255,255,255))
		text2 = font.render( str(self.frameCnt//10) + "." + str(self.frameCnt%10), 10, (255,255,255))		

		textpos1 = text1.get_rect()
		textpos2 = text2.get_rect()
		textpos1.centerx = (len(self.map) * self.gridSize[0]) + 100
		textpos1.centery = 200
		textpos2.centerx = (len(self.map) * self.gridSize[0]) + 100
		textpos2.centery = 500
		self.surf.blit(text1, textpos1)
		self.surf.blit(text2, textpos2)

		self.screen.blit(self.surf, (0,0))

		pygame.display.flip()
		pygame.display.update()
		self.fpsClock.tick(self.fps)
		self.frameCnt += 1
		return 1

class moveSelector:


	def getMove(self, g):
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if(event.key == pygame.K_UP):
					return 1
				elif(event.key == pygame.K_DOWN):
					return 3
				elif(event.key == pygame.K_RIGHT):
					return 0
				elif(event.key == pygame.K_LEFT):
					return 2
		return -1