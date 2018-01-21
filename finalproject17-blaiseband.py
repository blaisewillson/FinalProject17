import numpy
import curses
import random
import sys


# make sure to use screen.addstr print doesn't work with curses

floor1 = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','>','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','^','.','.','#','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

floor2 = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','^','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','$','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','>','.','.','.','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

floor3 = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','#','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','>','#','.','.','^','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

floor4 = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','#','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','>','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','^','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

finalfloor = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','#','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','^','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','>','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

bossroom = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','^','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])


village = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','P','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','>','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','@','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','#'],
['#','$','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','.','.','.','.','.','.','.','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])


currentmap = village
coninv = False
conjourn = False
wait = 0
floor = 'village'

def won():
	screen.clear()
	screen.addstr(0, 0, 'u won')
	won1 = screen.getch()
	sys.exit()

class Monster(object):
	
	def __init__(self ,boss):
		global currentmap
		global floor
		
		if boss == False:
			self.monsters = {'rat': {'char': 'r', 'dmg1': 1, 'dmg2': 2}, 'goblin': {'char': 'g', 'dmg1': 1, 'dmg2': 3}, 'wizard': {'char': 'w', 'dmg1': 3, 'dmg2': 6}, 'orgre': {'char': 'O', 'dmg1': 2, 'dmg2': 4}, 'cyclops': {'char': 'C', 'dmg1': 3, 'dmg2': 5}}		
			self.monsterchoice = random.randint(0,4)
			if self.monsterchoice == 0:
				self.monster = 'rat' 
			if self.monsterchoice == 1:
				self.monster = 'goblin'
			if self.monsterchoice == 2:
				self.monster = 'wizard'
			if self.monsterchoice == 3:
				self.monster = 'orgre'
			if self.monsterchoice == 4:
				self.monster = 'cyclops'	   			   			   			   			      
			self.monsterX = 0
			self.monsterY = 0
			while currentmap[self.monsterY][self.monsterX] != '.': 
				self.monsterX = random.randint(1, 77)
				self.monsterY = random.randint(1, 6)						
			if floor != 'village':
				currentmap[self.monsterY][self.monsterX] = self.monsters[self.monster]['char']
			self.charactermon = self.monsters[self.monster]['char']
			if floor == 'village':
				self.monsterlvl = 0
			elif floor == 'floor 1':
				self.monsterlvl = 1
			elif floor == 'floor 2':
				self.monsterlvl = 3
			elif floor == 'floor 3':
				self.monsterlvl = 6
			elif floor == 'floor 4':
				self.monsterlvl = 9
			elif floor == 'final floor':
				self.monsterlvl = 12	
			self.monsterhp = self.monsterlvl * 10
			self.basedmg1 = self.monsters[self.monster]['dmg1']
			self.basedmg2 = self.monsters[self.monster]['dmg2']
			self.boss = False
		elif boss == True:
			self.monster = 'King of Rats'
			self.monsterX = 0
			self.monsterY = 0
			while currentmap[self.monsterY][self.monsterX] != '.': 
				self.monsterX = random.randint(1, 77)
				self.monsterY = random.randint(1, 6)
			self.monsterlvl = 1
			self.monsterhp = 150
			self.basedmg1 = 30
			self.basedmg2 = 60
			self.charactermon = 'M'
			self.boss = True
	
	def monsterMove(self):
		global currentmap
		global wait
		if floor != 'village' and self.monsterhp > 0:
			suc = 0
			if wait == 0:
				while suc == 0:
					rand = random.randint(0, 3)
					if rand == 0 and currentmap[self.monsterY][self.monsterX + 1] != '#' and currentmap[self.monsterY][self.monsterX + 1] != '>' and currentmap[self.monsterY][self.monsterX + 1] != '^' and currentmap[self.monsterY][self.monsterX + 1] != '$':
						suc = 1
						currentmap[self.monsterY][self.monsterX + 1] = self.charactermon
						currentmap[self.monsterY][self.monsterX] = '.'
						self.monsterX = self.monsterX + 1
						drawmap()
					elif rand == 1 and currentmap[self.monsterY][self.monsterX - 1] != '#' and currentmap[self.monsterY][self.monsterX - 1] != '>' and currentmap[self.monsterY][self.monsterX - 1] != '^' and currentmap[self.monsterY][self.monsterX - 1] != '$':
						suc = 1
						currentmap[self.monsterY][self.monsterX - 1] = self.charactermon
						currentmap[self.monsterY][self.monsterX] = '.'
						self.monsterX = self.monsterX - 1
						drawmap()
					elif rand == 2 and currentmap[self.monsterY - 1][self.monsterX] != '#' and currentmap[self.monsterY - 1][self.monsterX] != '>' and currentmap[self.monsterY - 1][self.monsterX] != '^' and currentmap[self.monsterY - 1][self.monsterX] != '$':
						suc = 1
						currentmap[self.monsterY - 1][self.monsterX] = self.charactermon
						currentmap[self.monsterY][self.monsterX] = '.'
						self.monsterY = self.monsterY - 1
						drawmap()
					elif rand == 2 and currentmap[self.monsterY + 1][self.monsterX] != '#' and currentmap[self.monsterY + 1][self.monsterX] != '>' and currentmap[self.monsterY + 1][self.monsterX] != '^' and currentmap[self.monsterY + 1][self.monsterX] != '$':
						suc = 1
						currentmap[self.monsterY + 1][self.monsterX] = self.charactermon
						currentmap[self.monsterY][self.monsterX] = '.'
						self.monsterY = self.monsterY + 1
						drawmap()
			elif wait == 4:
				currentmap[self.monsterY][self.monsterX] = '.'
				self.monsterX = 0
				self.monsterY = 0
				while currentmap[self.monsterY][self.monsterX] != '.': 
					self.monsterX = random.randint(1, 77)
					self.monsterY = random.randint(1, 6)
			
			if wait > 0:	
				wait = wait - 1

	def fight(self, turn):
		global wait
		
		if floor != 'village' and self.monsterhp > 0:
			if self.monsterX == Player.playerX + 1 and self.monsterY == Player.playerY or self.monsterX == Player.playerX and self.monsterY == Player.playerY -1 or self.monsterY == Player.playerY + 1 and self.monsterX == Player.playerX or self.monsterY == Player.playerY and self.monsterX == Player.playerX - 1:
				screen.clear()
				drawmap()
				dispinv()
				disptop()
				if self.boss == False:
					screen.addstr(5, 20, '**It is a level %s %s with %s health.**'%(self.monsterlvl, self.monster, self.monsterhp))
				elif self.boss == True:
					screen.addstr(5, 20, '**It is the King of Rats!  It has 150 health.')
				screen.getch()
	
				while self.monsterhp > 0:
					screen.clear()
					dispinv()
					drawmap()
					if turn == 'monster':
						damage = random.randint(self.monsterlvl + self.basedmg1 +(self.monsterlvl/2), self.monsterlvl + self.basedmg2 + (self.monsterlvl/2))
						Player.health = Player.health - damage
						disptop()
						screen.addstr(5, 0, '**The %s has hit you for %s damage! The %s has %s health**'%(self.monster, damage, self.monster, self.monsterhp))
						if Player.health <= 0:
							screen.clear()
							screen.addstr(0, 0,  '                 ______')
							screen.addstr(1, 0,  '           _____/      \\_____')
							screen.addstr(2, 0,  '          |  _     ___   _   ||')
							screen.addstr(3, 0,  '          | | \     |   | \  ||')
							screen.addstr(4, 0,  '          | |  |    |   |  | ||')
							screen.addstr(5, 0,  '          | |_/     |   |_/  ||')
							screen.addstr(6, 0,  '          | | \     |   |    ||    LVL: %s'%(Player.lvl))
							screen.addstr(7, 0,  '          | |  \    |   |    ||    GOLD: %s'%(Player.gold))
							screen.addstr(8, 0,  '          | |   \. _|_. | .  ||')
							screen.addstr(9, 0,  '          |                  ||')
							screen.addstr(10, 0, '          |                  ||')
							screen.addstr(11, 0, '  *       | *   **    * **   |**      **')
							screen.addstr(12, 0, '   \))..\,,/.,(//,,..,,\||(,,.,\\,.((//')
							quit = screen.getch()
							if quit != -122:
								sys.exit()
						turn = 'player'
					elif turn == 'player':
						self.monsterhp = self.monsterhp - Player.attack
						if self.monsterhp > 0:
							screen.addstr(5, 0, '**You have hit the %s for %s damage! The %s has %s health.**'%(self.monster, Player.attack, self.monster, self.monsterhp))
						elif self.monsterhp <= 0:
							screen.addstr(5, 0, '**You have hit the %s for %s damage! The %s has 0 health.**'%(self.monster, Player.attack, self.monster))		
						turn = 'monster'
					disptop()
					coninv = False
					char = screen.getch()
					if char == 105:
						while coninv == False:
							coninv = inventory()
						coninv = False			
				if floor == 'boss room':
					won()
				
				if Player.lvl < 100:
					Player.lvl = Player.lvl + 1
					Player.attack = Player.attack + 1
					Player.defence = Player.defence +1
				Player.healthmax = Player.healthmax + 5 + Player.defence
				Player.gold = Player.gold + self.monsterlvl * 5
				self.monsterlvl = self.monsterlvl + 1
				if floor != 'boss room':
					self.monsterhp = self.monsterlvl * 10	
				Player.health = Player.healthmax
				screen.clear()
				drawmap()
				dispinv()
				disptop()
				screen.addstr(5, 13, '**You have defeated the %s! You have recieved %s gold'%(self.monster, (self.monsterlvl-1)*5))
				nothing = screen.getch()
				wait = 4
				self.monsterMove()


class Player():
	playerX = 77
	playerY = 3
	consumables = {'potion': {'amount': 1, 'cost': 50}, 'better potion': {'amount': 0, 'cost': 100}, 'full heal': {'amount': 0, 'cost': 200}}
	equipable = {'basic sword': {'has': True, 'dmg': 1, 'equiped': 'equiped'}, 'broadsword': {'has': False, 'dmg': 3, 'equiped': 'unequiped'}, 'shield':{'has': False, 'defence': 5, 'equiped': 'unequiped'}, 'big shield': {'has': False, 'defence': 10, 'equiped': 'unequiped'}}
	health = 20
	healthmax = 20
	gold = 100
	lvl = 1
	attack = 6
	defence = 0
	name = 'nothing'
	
	
	#def __init__(self, name):
		#self.name = name
		
	#def characterStat(self)
			

def playerset():
	player = Player()
	
#	player.characterStat()

def titlescreen():
    screen.addstr(0, 9,  ' ____  _        _    ___ ____  _____ ____    _    _   _ ____  ')
    screen.addstr(1, 9,  '| __ )| |      / \  |_ _/ ___|| ____| __ )  / \  | \ | |  _ \ ')
    screen.addstr(2, 9,  '|  _ \| |     / _ \  | |\___ \|  _| |  _ \ / _ \ |  \| | | | |')
    screen.addstr(3, 9,  '| |_) | |___ / ___ \ | | ___) | |___| |_) / ___ \| |\  | |_| |')
    screen.addstr(4, 9,  '|____/|_____/_/   \_\___|____/|_____|____/_/   \_\_| \_|____/ ')
    screen.addstr(7, 9,  '                      By: Blaise Willson                      ')
    screen.addstr(10, 9, '                    Press any key to start                    ')
    screen.addstr(11, 3, '           /\                                                 /\ ')
    screen.addstr(12, 3, ' _         )( ______________________   ______________________ )(         _ ')     
    screen.addstr(13, 3, '(_)|||||||(**)______________________> <______________________(**)|||||||(_)')
    screen.addstr(14, 3, '           )(                                                 )(')
    screen.addstr(15, 3, '           \/                                                 \/ ')
    start = screen.getch()
    if start == -2:
        return 0

def dispinv():
    screen.addstr(15, 5, '+++++++++++++')
    screen.addstr(16, 5, '+ INVENTORY +')
    screen.addstr(17, 5, '+++++++++++++')
    screen.addstr(18, 5, '  -press i-  ')
    screen.addstr(15, 60, '+++++++++++++')
    screen.addstr(16, 60, '+  JOURNAL  +')
    screen.addstr(17, 60, '+++++++++++++')
    screen.addstr(18, 60, '  -press j-  ')
    
def disptop():
	if floor == 'village':
		screen.addstr(3, 32, '      Town      ')
		screen.addstr(4, 31, '------------------')
	elif floor == 'floor 1':
		screen.addstr(3, 32, 'Dungeon  Floor 1')
		screen.addstr(4, 31, '------------------')
	elif floor == 'floor 2':
		screen.addstr(3, 32, 'Dungeon  Floor 2')
		screen.addstr(4, 31, '------------------')
	elif floor == 'floor 3':
		screen.addstr(3, 32, 'Dungeon  Floor 3')
		screen.addstr(4, 31, '------------------')
	elif floor == 'floor 4':
		screen.addstr(3, 32, 'Dungeon  Floor 4')
		screen.addstr(4, 31, '------------------')
	elif floor == 'final floor':
		screen.addstr(3, 32, '  Final  Floor  ')
		screen.addstr(4, 31, '------------------')
	elif floor == 'boss room':
		screen.addstr(3, 32, '   Boss  Room   ')
		screen.addstr(4, 31, '------------------')
	screen.addstr(0, 5, '++++++++++++++++++')
	screen.addstr(1, 5, '+ HEALTH:%s /%s  '%(Player.health, Player.healthmax))
	screen.addstr(1, 22, '+')
	screen.addstr(2, 5, '++++++++++++++++++')
	screen.addstr(0, 32, '++++++++++++++++')
	screen.addstr(1, 32, '+   GOLD:%s   '%(Player.gold))
	screen.addstr(1, 47, '+')
	screen.addstr(2, 32, '++++++++++++++++')
	screen.addstr(3, 11, 'ATK:%s'%(Player.attack))
	screen.addstr(3, 64, 'DEF:%s'%(Player.defence))
	if Player.lvl < 10:
		screen.addstr(0, 57, '++++++++++++++++++')
		screen.addstr(1, 57, '+      LVL:%s     +'%(Player.lvl))
		screen.addstr(2, 57, '++++++++++++++++++')
	else:
		screen.addstr(0, 57, '++++++++++++++++++')
		screen.addstr(1, 57, '+     LVL:%s     +'%(Player.lvl))
		screen.addstr(2, 57, '++++++++++++++++++')
    
def drawmap():
	screen.addstr(6, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
	
def movedown():
	global currentmap
	global floor
	global village
	global floor1
	global floor2
	global floor3
	global floor4
	global finalfloor
	global bossroom
	global monster1
	global monster2
	global monster3
	global monster4
	global monster5
	global boosmonster
	
	if floor == 'village':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		floor = 'floor 1'
		currentmap = floor1
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		drawmap()
	elif floor == 'floor 1':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		floor = 'floor 2'
		currentmap = floor2
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		drawmap()
	elif floor == 'floor 2':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		floor = 'floor 3'
		currentmap = floor3
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		monster3 = Monster(False)
		drawmap()
	elif floor == 'floor 3':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		floor = 'floor 4'
		currentmap = floor4
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		monster3 = Monster(False)
		monster4 = Monster(False)
		drawmap()
	elif floor == 'floor 4':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		del monster4
		floor = 'final floor'
		currentmap = finalfloor
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		monster3 = Monster(False)
		monster4 = Monster(False)
		monster5 = Monster(False)
		drawmap()
	elif floor == 'final floor':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		del monster4
		del monster5
		floor = 'boss room'
		currentmap = bossroom
		currentmap[Player.playerY][Player.playerX] = '@'
		bossmonster = Monster(True)
		drawmap()		
		
def moveup():
	global currentmap
	global floor
	global village
	global floor1
	global floor2
	global floor3
	global floor4
	global finalfloor
	global bossroom
	global monster1
	global monster2
	global monster3
	global monster4
	global monster5
	global bossmonster

	if floor == 'floor 1':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		floor = 'village'
		currentmap = village
		currentmap[Player.playerY][Player.playerX] = '@'
		drawmap()
	elif floor == 'floor 2':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		floor = 'floor 1'
		currentmap = floor1
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		drawmap()      
	elif floor == 'floor 3':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		floor = 'floor 2'
		currentmap = floor2
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		drawmap()	
	elif floor == 'floor 4':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		del monster4
		floor = 'floor 3'
		currentmap = floor3
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		monster3 = Monster(False)
		drawmap()
	elif floor == 'final floor':
		currentmap[monster1.monsterY][monster1.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del monster1
		del monster2
		del monster3
		del monster4
		del monster5
		floor = 'floor 4'
		currentmap = floor4
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		monster2 = Monster(False)
		monster3 = Monster(False)
		monster4 = Monster(False)
		drawmap()
	elif floor == 'boss room' and bossmonster.monsterhp <= 0:
		currentmap[bossmonster.monsterY][bossmonster.monsterX] = '.'
		currentmap[Player.playerY][Player.playerX] = '.'
		del bossmonster
		floor = 'final floor'
		currentmap = village
		currentmap[Player.playerY][Player.playerX] = '@'
		monster1 = Monster(False)
		drawmap()						

def buy():
	screen.clear()
	drawmap()
	disptop()
	screen.addstr(14, 33, '   Store   ')
	screen.addstr(15, 33, '-----------')
	screen.addstr(16, 31, 'press e to exit')
	screen.addstr(17, 30, 'press space to buy')
	screen.addstr(18, 27, 'use arrow keys to select')	
	screen.addstr(14, 5, '  Inventory:  ')
	screen.addstr(15, 4, '--------------')
	screen.addstr(16, 2, '1. potions: %s'%(Player.consumables['potion']['amount']))
	screen.addstr(17, 2, '2. better potions: %s'%(Player.consumables['better potion']['amount']))	
	screen.addstr(18, 2, '3. full heals: %s'%(Player.consumables['full heal']['amount']))
	screen.addstr(14, 62, 'Buy:')
	screen.addstr(15, 61, '------')
	screen.addstr(16, 59, '1. potion:$%s'%(Player.consumables['potion']['cost']))
	screen.addstr(17, 59, '2. better potion:$%s'%(Player.consumables['better potion']['cost']))
	screen.addstr(18, 59, '3. full heal:$%s'%(Player.consumables['full heal']['cost']))
	
	screen.move(16, 70)
	curses.curs_set(1)
	cursermove = 1	
	while cursermove != 101:
		cursermove = screen.getch()
		
		if cursermove == curses.KEY_DOWN and screen.getyx() == (16, 70):
			screen.move(17, 77) 
		elif cursermove == curses.KEY_DOWN and screen.getyx() == (17, 77):
			screen.move(18, 73)
		elif cursermove == curses.KEY_UP and screen.getyx() == (18, 73):
			screen.move(17, 77)
		elif cursermove == curses.KEY_UP and screen.getyx() == (17, 77):
			screen.move(16, 70)
		elif cursermove == 32 and Player.gold >= Player.consumables['potion']['cost'] and screen.getyx() == (16, 70):
			Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] +1
			Player.gold = Player.gold - Player.consumables['potion']['cost']
			disptop()
			screen.addstr(16, 2, '1. potions: %s'%(Player.consumables['potion']['amount']))
			screen.move(16, 70)
		elif cursermove == 32 and Player.gold >= Player.consumables['better potion']['cost'] and screen.getyx() == (17, 77):
			Player.consumables['better potion']['amount'] = Player.consumables['better potion']['amount'] +1
			Player.gold = Player.gold - Player.consumables['better potion']['cost']
			disptop()
			screen.addstr(17, 2, '2. better potions: %s'%(Player.consumables['better potion']['amount']))
			screen.move(17, 77)
		elif cursermove == 32 and Player.gold >= Player.consumables['full heal']['cost'] and screen.getyx() == (18, 73):
			Player.consumables['full heal']['amount'] = Player.consumables['full heal']['amount'] +1
			Player.gold = Player.gold - Player.consumables['full heal']['cost']
			disptop()
			screen.addstr(18, 2, '3. full heal: %s'%(Player.consumables['full heal']['amount']))
			screen.move(18, 73)						
	curses.curs_set(0)

def elder():
	global journal
	
	screen.clear()
	disptop()
	dispinv()
	drawmap()
	screen.addstr(5, 5, 'Hello traveler! You must be here for the dugeon.')
	screen.getch()
	screen.addstr(5, 5, 'What might your name be:                        ')
	curses.echo()
	curses.curs_set(1)
	screen.move(5, 29)
	Player.name = screen.getstr() 
	curses.curs_set(0)
	curses.noecho()
	screen.addstr(5, 5, 'Hello %s. I am the town elder.'%(Player.name))
	screen.getch()
	screen.addstr(5, 5, 'Ah! I see you have a journal.                      ')
	screen.getch()
	screen.addstr(5, 5, 'May I take a look.             ')
	screen.getch()
	screen.addstr(5, 5, 'I have added everything you might need to know to it.')
	screen.getch()
	screen.addstr(5, 5, 'Good luck! The dungeon is just West of here.          ')
	screen.getch()
	journal = True

def check(direction):
    global currentmap
    global floor
    global village
    global floor1
    global monster1
    
    if currentmap[Player.playerY - 1][Player.playerX] == '$' and direction == 'up':
        buy()
        return 1
    elif currentmap[Player.playerY + 1][Player.playerX] == '$' and direction == 'down':
        buy()
        return 1
    elif currentmap[Player.playerY][Player.playerX + 1] == '$' and direction == 'right':
        buy()
        return 1
    elif currentmap[Player.playerY][Player.playerX - 1] == '$' and direction == 'left':
        buy()
        return 1
    elif currentmap[Player.playerY - 1][Player.playerX] == '>' and direction == 'up':
        movedown()
        return 1
    elif currentmap[Player.playerY + 1][Player.playerX] == '>' and direction == 'down':    
        movedown()
        return 1
    elif currentmap[Player.playerY][Player.playerX + 1] == '>' and direction == 'right':
        movedown()
        return 1
    elif currentmap[Player.playerY][Player.playerX - 1] == '>' and direction == 'left':
        movedown()
        return 1 
    elif currentmap[Player.playerY - 1][Player.playerX] == '^' and direction == 'up':  		
        moveup()
        return 1
    elif currentmap[Player.playerY + 1][Player.playerX] == '^' and direction == 'down':
        moveup()
        return 1
    elif currentmap[Player.playerY][Player.playerX + 1] == '^' and direction == 'right':
        moveup()
        return 1
    elif currentmap[Player.playerY][Player.playerX - 1] == '^' and direction == 'left':
        moveup()
        return 1
    elif currentmap[Player.playerY - 1][Player.playerX] == 'P' and direction == 'up':  		
        elder()
        return 1
    elif currentmap[Player.playerY + 1][Player.playerX] == 'P' and direction == 'down':
        elder()
        return 1
    elif currentmap[Player.playerY][Player.playerX + 1] == 'P' and direction == 'right':
        elder()
        return 1
    elif currentmap[Player.playerY][Player.playerX - 1] == 'P' and direction == 'left':
        elder()
        return 1                                                
    return 2

def fightlist():
	if floor == 'floor 1':
		monster1.fight('player')
	elif floor == 'floor 2':
		monster1.fight('player')
		monster2.fight('player')
	elif floor == 'floor 3':
		monster1.fight('player')
		monster2.fight('player')
		monster3.fight('player')
	elif floor == 'floor 4':
		monster1.fight('player')
		monster2.fight('player')
		monster3.fight('player')
		monster4.fight('player')
	elif floor == 'floor 5':
		monster1.fight('player')
		monster2.fight('player')
		monster3.fight('player')
		monster4.fight('player')
		monster5.fight('player')		
	elif floor ==  'boss room':
		bossmonster.fight('player')

def move(char):
    global currentmap
    global floor
    if char == curses.KEY_RIGHT and currentmap[Player.playerY][Player.playerX + 1] != '#':
        end = check('right')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX + 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX + 1
        if wait == 0:
        	fightlist()
        drawmap()
    elif char == curses.KEY_LEFT and currentmap[Player.playerY][Player.playerX - 1] != '#':
        end = check('left')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX - 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX - 1
        if wait == 0:
        	fightlist()
        drawmap()
    elif char == curses.KEY_UP and currentmap[Player.playerY - 1][Player.playerX] != '#':
        end = check('up')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY - 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY - 1
        if wait == 0:
        	fightlist()
        drawmap()
    elif char == curses.KEY_DOWN and currentmap[Player.playerY + 1][Player.playerX] != '#':
        end = check('down')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY + 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY + 1
        if wait == 0:
        	fightlist()
        drawmap()
    if floor == 'floor 1':
		monster1.monsterMove()
    elif floor == 'floor 2':
		monster1.monsterMove()
		monster2.monsterMove()
    elif floor == 'floor 3':
		monster1.monsterMove()
		monster2.monsterMove()
		monster3.monsterMove()
    elif floor == 'floor 4':
		monster1.monsterMove()
		monster2.monsterMove()
		monster3.monsterMove()
		monster4.monsterMove()
    elif floor == 'floor 5':
		monster1.monsterMove()
		monster2.monsterMove()
		monster3.monsterMove()
		monster4.monsterMove()
		monster5.monsterMove()		
    elif floor ==  'boss room':
		bossmonster.move()        		
    fightlist()

def Journal():
	global journal
	
	screen.clear()
	drawmap()
	disptop()
	exit = -1
	while exit != 101:
		if journal == False:
			screen.addstr(14, 34, 'Journal         press e to exit')
			screen.addstr(15, 33, '---------')
			screen.addstr(16, 0, 'There is nothing written.')
		elif journal == True:
			screen.addstr(14, 34, 'Journal         press e to exit')
			screen.addstr(15, 33, '---------')		
			screen.addstr(16, 0, 'The Dungeon is a terrible place. It is filled with rats(r), goblins(g) and more!')
			screen.addstr(17, 0, 'To descend into the dungeon walk up to the staircases that look like this: >')
			screen.addstr(18, 0, 'To ascend up through the dungeon walk up to the staircase that look like this: ^')
			screen.addstr(19, 0, 'In order to fight the monsters walk next to them.')
		exit = screen.getch()
    
def inventory():
	screen.clear()
	drawmap()
	disptop()
	screen.addstr(14, 34, 'Inventory')
	screen.addstr(15, 33, '-----------')
	screen.addstr(16, 31, 'press e to exit')
	screen.addstr(17, 27, 'press space to use/equip')
	screen.addstr(18, 27, 'use arrow keys to select')
	screen.addstr(14, 5, 'Consumables:')
	screen.addstr(15, 4, '--------------')
	screen.addstr(14, 58, 'Weapons / Shields:')
	screen.addstr(15, 57, '--------------------')
	screen.addstr(16, 2, '1. potions: %s'%(Player.consumables['potion']['amount']))
	screen.addstr(17, 2, '2. better potions: %s'%(Player.consumables['better potion']['amount']))	
	screen.addstr(18, 2, '3. full heals: %s'%(Player.consumables['full heal']['amount']))
	screen.addstr(16, 54, '1. basic sword: %s'%(Player.equipable['basic sword']['equiped']))
	if Player.equipable['broadsword']['has'] == True:
		screen.addstr(17, 54, '2. broadsword: %s'%(Player.equipable['broadsword']['equiped']))
	elif Player.equipable['broadsword']['has'] == False:	
		screen.addstr(17, 54, '2. broadsword: Dont have')
		
	if Player.equipable['shield']['has'] == True:
		screen.addstr(18, 54, '3. shield: %s'%(Player.equipable['shield']['equiped']))
	elif Player.equipable['shield']['has'] == False:	
		screen.addstr(18, 54, '3. shield: Dont have')
		
	if Player.equipable['big shield']['has'] == True:
		screen.addstr(19, 54, '4. big shield: %s'%(Player.equipable['big shield']['equiped']))
	elif Player.equipable['big shield']['has'] == False:	
		screen.addstr(19, 54, '4. big shield: Dont have')			
	
	curses.curs_set(1)
	screen.move(16, 14)
	cursermove = 1
	while cursermove != 101:
		cursermove = screen.getch()
		if cursermove == curses.KEY_DOWN and screen.getyx() == (16, 14):
			screen.move(17, 21) 
		elif cursermove == curses.KEY_DOWN and screen.getyx() == (17, 21):
			screen.move(18, 17)
		elif cursermove == curses.KEY_UP and screen.getyx() == (18, 17):
			screen.move(17, 21)
		elif cursermove == curses.KEY_UP and screen.getyx() == (17, 21):
			screen.move(16, 14)
		elif cursermove == curses.KEY_DOWN and screen.getyx() == (16, 70):
			screen.move(17, 69) 
		elif cursermove == curses.KEY_DOWN and screen.getyx() == (17, 69):
			screen.move(18, 65)
		elif cursermove == curses.KEY_DOWN and screen.getyx() == (18, 65):
			screen.move(19, 69)
		elif cursermove == curses.KEY_UP and screen.getyx() == (19, 69):
			screen.move(18, 65)
		elif cursermove == curses.KEY_UP and screen.getyx() == (18, 65):
			screen.move(17, 69) 
		elif cursermove == curses.KEY_UP and screen.getyx() == (17, 69):
			screen.move(16, 70)
		elif cursermove == curses.KEY_RIGHT:
			screen.move(16, 70)
		elif cursermove == curses.KEY_LEFT:
			screen.move(16, 14)	
#where it starts to check for enters	
		elif cursermove == 32 and screen.getyx() == (16, 14) and Player.consumables['potion']['amount'] > 0: # potion
			if Player.health + 20 >= Player.healthmax and Player.health != Player.healthmax :
				Player.health = Player.healthmax
				Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] - 1
				screen.addstr(16, 2, '1. potions: %s'%(Player.consumables['potion']['amount']))
				disptop()
				screen.move(16, 14)				
			elif Player.health + 20 < Player.healthmax:
				Player.health = Player.health + 20
				Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] - 1
				screen.addstr(16, 2, '1. potions: %s'%(Player.consumables['potion']['amount']))
				disptop()
				screen.move(16, 14)
		elif cursermove == 32 and screen.getyx() == (17, 21) and Player.consumables['better potion']['amount'] > 0: # better potion
			if Player.health + 50 >= Player.healthmax and Player.health != Player.healthmax :
				Player.health = Player.healthmax
				Player.consumables['better potion']['amount'] = Player.consumables['better potion']['amount'] - 1
				screen.addstr(17, 2, '2. better potions: %s'%(Player.consumables['better potion']['amount']))
				disptop()
				screen.move(17, 21)
			elif Player.health + 50 < Player.healthmax:
				Player.health = Player.health + 50
				Player.consumables['better potion']['amount'] = Player.consumables['better potion']['amount'] - 1
				screen.addstr(17, 2, '2. better potions: %s'%(Player.consumables['better potion']['amount']))
				disptop()
				screen.move(17, 21)			
		elif cursermove == 32 and screen.getyx() == (18, 17) and Player.consumables['full heal']['amount'] > 0: # full heal
			Player.health = Player.healthmax
			Player.consumables['full heal']['amount'] = Player.consumables['full heal']['amount'] - 1	
			screen.addstr(18, 2, '3. full heals: %s'%(Player.consumables['full heal']['amount']))
			disptop()
			screen.move(18, 17)		
		elif cursermove == 32 and screen.getyx() == (16, 70) and Player.equipable['basic sword']['equiped'] == 'equiped': # basic sword - equiped
			Player.equipable['basic sword']['equiped'] = 'unequiped'
			Player.attack = Player.attack - Player.equipable['basic sword']['dmg']
			screen.addstr(16, 54, '1. basic sword: %s'%(Player.equipable['basic sword']['equiped']))
			disptop()
			screen.move(16, 70)
		elif cursermove == 32 and screen.getyx() == (16, 70) and Player.equipable['basic sword']['equiped'] == 'unequiped': # basic sword - unequiped
			Player.equipable['basic sword']['equiped'] = 'equiped'
			Player.attack = Player.attack + Player.equipable['basic sword']['dmg']
			screen.addstr(16, 54, '1. basic sword: %s  '%(Player.equipable['basic sword']['equiped']))
			disptop()
			screen.move(16, 70)			
		elif cursermove == 32 and screen.getyx() == (17, 69) and Player.equipable['broadsword']['equiped'] == 'equiped' and Player.equipable['broadsword']['has'] == True: # broad sword - equiped
			Player.equipable['broadsword']['equiped'] = 'unequiped'
			Player.attack = Player.attack - Player.equipable['broadsword']['dmg']
			screen.addstr(17, 54, '2. broadsword: %s'%(Player.equipable['broadsword']['equiped']))
			disptop()
			screen.move(16, 70)		
		elif cursermove == 32 and screen.getyx() == (17, 69) and Player.equipable['broadsword']['equiped'] == 'unequiped' and Player.equipable['broadsword']['has'] == True: # broad sword - unequiped
			Player.equipable['broadsword']['equiped'] = 'equiped'
			Player.attack = Player.attack + Player.equipable['broadsword']['dmg']	
			screen.addstr(17, 54, '2. broadsword: %s  '%(Player.equipable['broadsword']['equiped']))
			disptop()
			screen.move(16, 70)						
		elif cursermove == 32 and screen.getyx() == (18, 65) and Player.equipable['shield']['equiped'] == 'equiped' and Player.equipable['shield']['has'] == True: # shield - equiped
			Player.equipable['shield']['equiped'] = 'unequiped'
			Player.healthmax = Player.defence - Player.equipable['shield']['defence']
			screen.addstr(18, 54, '3. shield: %s'%(Player.equipable['shield']['equiped']))
			disptop()
			screen.move(18, 65)
		elif cursermove == 32 and screen.getyx() == (18, 65) and Player.equipable['shield']['equiped'] == 'unequiped' and Player.equipable['shield']['has'] == True: # shield - unequiped
			Player.equipable['shield']['equiped'] = 'equiped'
			Player.healthmax = Player.defence + Player.equipable['shield']['defence']
			screen.addstr(18, 54, '3. shield: %s  '%(Player.equipable['shield']['equiped']))
			disptop()
			screen.move(18, 65)						
		elif cursermove == 32 and screen.getyx() == (19, 69) and Player.equipable['big shield']['equiped'] == 'equiped' and Player.equipable['big shield']['has'] == True: # big shield - equiped
			Player.equipable['big shield']['equiped'] = 'unequiped'
			Player.healthmax = Player.defence - Player.equipable['big shield']['defence']	
			screen.addstr(19, 54, '4. big shield: %s'%(Player.equipable['big shield']['equiped']))
			disptop()
			screen.move(19, 69)			
		elif cursermove == 32 and screen.getyx() == (19, 69) and Player.equipable['big shield']['equiped'] == 'unequiped' and Player.equipable['big shield']['has'] == True: # big shield - unequiped
			Player.equipable['big shield']['equiped'] = 'equiped'
			Player.healthmax = Player.defence + Player.equipable['big shield']['defence']
			screen.addstr(19, 54, '4. big shield: %s  '%(Player.equipable['big shield']['equiped']))
			disptop()
			screen.move(19, 69)
	curses.curs_set(0)							

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=80))

screen = curses.initscr()

curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

titlescreen()
playerset()

bossmonster = Monster(True)
monster1 = Monster(False)
monster2 = Monster(False)
monster3 = Monster(False)
monster4 = Monster(False)
monster5 = Monster(False)
journal = False


try:
    while True:
        screen.clear()
        disptop()
        dispinv()
        drawmap()
        char = screen.getch()
        move(char)
        if char == 105:
            while coninv == False:
                coninv = inventory()
        coninv = False
        if char == 106:
        	while conjourn == False:
        		conjourn = Journal()
        conjourn = False	
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
