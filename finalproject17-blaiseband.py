import numpy
import curses
import random
import sys


# make sure to use screen.addstr print doesn't work with curses

floor1 = numpy.array([
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','#','.','.','#','#','#','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','@','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','.','.','.','.','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','>','.','.','#','.','.','#','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','#','#','#','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','.','.','.','.','#','#','#','#','#','#','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','#','.','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','.','#','.','.','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','$','.','.','.','#','s','#','#','#','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.','|','#','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']])

currentmap = floor1
coninv = False
wait = 0
floor = 'floor 1'

class Monster(object):
	
	def __init__(self):
		self.monster = 'snake'       
		self.monsterX = 6
		self.monsterY = 6
		self.charactermon = 's'
		self.monsterlvl = 1
		self.monsterhp = self.monsterlvl * 10
	
	def monsterMove(self):
		global currentmap
		global wait
		suc = 0
		if wait == 0:
			while suc == 0:
				rand = random.randint(0, 3)
				if rand == 0 and currentmap[self.monsterY][self.monsterX + 1] != '#':
					suc = 1
					currentmap[self.monsterY][self.monsterX + 1] = self.charactermon
					currentmap[self.monsterY][self.monsterX] = '.'
					self.monsterX = self.monsterX + 1
					drawmap()
				elif rand == 1 and currentmap[self.monsterY][self.monsterX - 1] != '#':
					suc = 1
					currentmap[self.monsterY][self.monsterX - 1] = self.charactermon
					currentmap[self.monsterY][self.monsterX] = '.'
					self.monsterX = self.monsterX - 1
					drawmap()
				elif rand == 2 and currentmap[self.monsterY - 1][self.monsterX] != '#':
					suc = 1
					currentmap[self.monsterY - 1][self.monsterX] = self.charactermon
					currentmap[self.monsterY][self.monsterX] = '.'
					self.monsterY = self.monsterY - 1
					drawmap()
				elif rand == 2 and currentmap[self.monsterY + 1][self.monsterX] != '#':
					suc = 1
					currentmap[self.monsterY + 1][self.monsterX] = self.charactermon
					currentmap[self.monsterY][self.monsterX] = '.'
					self.monsterY = self.monsterY + 1
					drawmap()
		elif wait >= 1:
			currentmap[self.monsterY][self.monsterX] = '.'
			if currentmap[self.monsterY][self.monsterX + 1] != '#':
				self.monsterX = self.monsterX + 1
			elif currentmap[self.monsterY][self.monsterX - 1] != '#':
				self.monsterX = self.monsterX - 1
			elif currentmap[self.monsterY + 1][self.monsterX] != '#':
				self.monsterY = self.monsterY + 1
			elif currentmap[self.monsterY - 1][self.monsterX] != '#':
				self.monsterY = self.monsterY - 1
			wait = wait - 1

	def fight(self, turn):
		global wait

		if self.monsterX == Player.playerX + 1 and self.monsterY == Player.playerY or self.monsterX == Player.playerX and self.monsterY == Player.playerY -1 or self.monsterY == Player.playerY + 1 and self.monsterX == Player.playerX or self.monsterY == Player.playerY and self.monsterX == Player.playerX - 1:
			screen.clear()
			drawmap()
			dispinv()
			disptop()
			screen.addstr(5, 20, '**It is a level %s %s with %s health.**'%(self.monsterlvl, self.monster, self.monsterhp))
			screen.getch()

			while self.monsterhp > 0:
				screen.clear()
				dispinv()
				drawmap()
				if turn == 'monster':
					damage = random.randint((self.monsterlvl)*1, (self.monsterlvl)*1)
					Player.health = Player.health - damage
					disptop()
					screen.addstr(5, 9, '**The %s has hit you for %s damage! The %s has %s health**'%(self.monster, damage, self.monster, self.monsterhp))
					if Player.health <= 0:
						screen.clear()
						screen.addstr(0, 0,  '                 ______')
						screen.addstr(1, 0,  '           _____/      \\_____')
						screen.addstr(2, 0,  '          |  _     ___   _   ||')
						screen.addstr(3, 0,  '          | | \     |   | \  ||')
						screen.addstr(4, 0,  '          | |  |    |   |  | ||')
						screen.addstr(5, 0,  '          | |_/     |   |_/  ||')
						screen.addstr(6, 0,  '          | | \     |   |    ||')
						screen.addstr(7, 0,  '          | |  \    |   |    ||')
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
					self.monsterhp = self.monsterhp - 5
					screen.addstr(5, 7, '**You have hit the %s for 5 damage! The %s has %s health.**'%(self.monster, self.monster, self.monsterhp))
					turn = 'monster'
				disptop()
				coninv = False
				char = screen.getch()
				if char == 105:
					while coninv == False:
						coninv = inventory()
					coninv = False			
			Player.lvl = Player.lvl + 1
			Player.healthmax = Player.healthmax + 5
			Player.gold = Player.gold + self.monsterlvl * 5
			self.monsterlvl = self.monsterlvl + 1
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
	playerX = 2
	playerY = 2
	consumables = {'potion': {'amount': 1, 'cost': 50}, 'better potion': {'amount': 0, 'cost': 100}, 'full heal': {'amount': 0, 'cost': 200}}
	equipable = {'basic sword':{'has': True, 'dmg': 1, 'equiped': True},'broadsword':{'has': False, 'dmg': 3, 'equiped': False},'shortsword':{'has': False, 'dmg': 2, 'equiped': False}, 'sheild':{'has': False, 'defence': 5, 'equiped': False}, 'big sheild':{'has': False, 'defence': 10, 'equiped': False}},
	health = 20
	healthmax = 20
	gold = 100
	lvl = 1
	
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
		screen.addstr(4, 32, '----------------')
	elif floor == 'floor 1':
		screen.addstr(3, 32, 'Dungeon  Floor 1')
		screen.addstr(4, 32, '----------------')
	elif floor == 'floor 2':
		screen.addstr(3, 32, 'Dungeon  Floor 2')
		screen.addstr(4, 32, '----------------')
	elif floor == 'floor 3':
		screen.addstr(3, 32, 'Dungeon  Floor 3')
		screen.addstr(4, 32, '----------------')
	elif floor == 'floor 4':
		screen.addstr(3, 32, 'Dungeon  Floor 4')
		screen.addstr(4, 32, '----------------')
	elif floor == 'final floor':
		screen.addstr(3, 32, '  Final  Floor  ')
		screen.addstr(4, 32, '----------------')
	elif floor == 'boss room':
		screen.addstr(3, 32, '   Boss  Room   ')
		screen.addstr(4, 32, '----------------')
	screen.addstr(0, 5, '++++++++++++++++++')
	screen.addstr(1, 5, '+ HEALTH:%s /%s  '%(Player.health, Player.healthmax))
	screen.addstr(1, 22, '+')
	screen.addstr(2, 5, '++++++++++++++++++')
	screen.addstr(0, 32, '++++++++++++++++')
	screen.addstr(1, 32, '+   GOLD:%s   '%(Player.gold))
	screen.addstr(1, 47, '+')
	screen.addstr(2, 32, '++++++++++++++++')
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

def buy():
    amount = 0
    while amount >= 0:
        screen.clear()
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 6, '%s'%(Player.gold))
        screen.addstr(0, 10, '| Store | e:exit')
        screen.addstr(1, 0, 'Press the number next to the item you want to buy')
        screen.addstr(2, 0, '1. potion: 50 gold')
        itemchoice = screen.getch()
        if itemchoice == 101:
            return 0
        screen.clear()
        screen.addstr(1, 0, 'How many?')
        curses.curs_set(1)
        curses.echo()
        amount = int(screen.getstr())
        if itemchoice == 49 and Player.gold >= 50 * amount:
        	Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] + amount
        	Player.gold = Player.gold - (Player.consumables['potion']['cost'] * amount)	
        curses.curs_set(0)
        curses.noecho()

def store(direction):
    global currentmap
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
    return 2

def move(char):
    global currentmap
    if char == curses.KEY_RIGHT and currentmap[Player.playerY][Player.playerX + 1] != '#':
        end = store('right')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX + 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX + 1
        if wait == 0:
        	monster1.fight('player')
        drawmap()
    elif char == curses.KEY_LEFT and currentmap[Player.playerY][Player.playerX - 1] != '#':
        end = store('left')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX - 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX - 1
        if wait == 0:
        	monster1.fight('player')
        drawmap()
    elif char == curses.KEY_UP and currentmap[Player.playerY - 1][Player.playerX] != '#':
        end = store('up')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY - 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY - 1
        if wait == 0:
        	monster1.fight('player')
        drawmap()
    elif char == curses.KEY_DOWN and currentmap[Player.playerY + 1][Player.playerX] != '#':
        end = store('down')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY + 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY + 1
        if wait == 0:
        	monster1.fight('player')
        drawmap()
    monster1.monsterMove()
    monster1.fight('monster')

def inventory():
    screen.clear()
    screen.addstr(0, 0, 'gold:')
    screen.addstr(0, 5, '%s'%(Player.gold))
    screen.addstr(0, 17, '%s/%s'%(Player.health, Player.healthmax))
    screen.addstr(0, 26, '| Inventory | e:exit')
    screen.addstr(1, 0, 'Press the number next to the item you want to use')
    screen.addstr(2, 0, '1. potions: %s'%(Player.consumables['potion']['amount']))
    itemchoice = screen.getch()
    if itemchoice == 101:
        return True
    elif itemchoice == 49 and Player.consumables['potion']['amount'] != 0:
        if Player.health + 10 >= Player.healthmax and Player.health != Player.healthmax:
            Player.health = Player.healthmax
            Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] - 1
        elif Player.health + 10 < Player.healthmax:
            Player.health = Player.health + 10
            Player.consumables['potion']['amount'] = Player.consumables['potion']['amount'] - 1
        elif Player.health == Player.healthmax:
            return False
        return True
    else:
        return False

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=80))

screen = curses.initscr()

curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

titlescreen()
playerset()

monster1 = Monster()

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
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
