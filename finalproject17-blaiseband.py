import numpy
import curses
import random
import sys


# make sure to use screen.addstr print doesn't work with curses

map1 = numpy.array([['#','#','#','#','#','#','#','#'],
   	 	            ['#','.','.','.','#','.','.','#'],
   	 	            ['#','.','@','.','.','.','.','#'],
   	 	            ['#','.','.','.','#','.','.','#'],
   	 	            ['#','#','.','#','#','#','.','#'],
   	 	            ['#','.','.','.','.','#','.','#'],
   	 	            ['#','$','.','.','.','#','s','#'],
   	 	            ['#','#','#','#','#','#','#','#']])

currentmap = map1
coninv = False
wait = 0

class Monster():
	monster = 'snake'       
	monsterX = 6
	monsterY = 6
	charactermon = 's'
	monsterlvl = 1

class Player():
	playerX = 2
	playerY = 2
	consumables = {'potion': {'amount': 1, 'cost': 50}, 'better potion': {'amount': 0, 'cost': 100}, 'full heal': {'amount': 0, 'cost': 200}}
	equipable = {'basic sword':{'has': True, 'dmg': 1, 'weight': 0, 'equiped': True},'broadsword':{'has': False, 'dmg': 3, 'weight': -1, 'equiped': False},'shortsword':{'has': False, 'dmg': 2, 'weight': 1, 'equiped': False}, 'sheild':{'has': False, 'defence': 5}, 'big sheild':{'has': False, 'defence': 10}},
	health = 20
	healthmax = 20
	gold = 100
	
	#def __init__(self, name):
		#self.name = name
		
	#def characterStat(self)
			

def playerset():
	player = Player()
	
#	player.characterStat()

def titlescreen():
    screen.addstr(0, 3, ' ____  _        _    ___ ____  _____ ____    _    _   _ ____  ')
    screen.addstr(1, 3, '| __ )| |      / \  |_ _/ ___|| ____| __ )  / \  | \ | |  _ \ ')
    screen.addstr(2, 3, '|  _ \| |     / _ \  | |\___ \|  _| |  _ \ / _ \ |  \| | | | |')
    screen.addstr(3, 3, '| |_) | |___ / ___ \ | | ___) | |___| |_) / ___ \| |\  | |_| |')
    screen.addstr(4, 3, '|____/|_____/_/   \_\___|____/|_____|____/_/   \_\_| \_|____/ ')
    screen.addstr(6, 3, '                   Press any key to start                     ')
    start = screen.getch()
    if start == -2:
        return 0

def fight(turn):
    #global Monster.monsterX
    #global Monster.monsterY
    #global Player.playerX
    #global Player.playerY
    #global Monster.monsterlvl
    #global Player.health
    #global Player.healthmax
    #global Player.gold
    global wait
    #global Monster.monster
    Monster.monsterhp = Monster.monsterlvl * 10

    if Monster.monsterX == Player.playerX + 1 and Monster.monsterY == Player.playerY or Monster.monsterX == Player.playerX and Monster.monsterY == Player.playerY -1 or Monster.monsterY == Player.playerY + 1 and Monster.monsterX == Player.playerX or Monster.monsterY == Player.playerY - 1 and Monster.monsterX == Player.playerX:
        screen.clear()
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        screen.addstr(0, 10, 'health:')
        screen.addstr(0, 17, '%s/%s'%(Player.health, Player.healthmax))
        screen.addstr(0, 26, '| It is a level %s %s with %s health.'%(Monster.monsterlvl, Monster.monster, Monster.monsterhp))
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 5, '%s'%(Player.gold))
        screen.getch()

        while Monster.monsterhp > 0:
            screen.clear()
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
            if turn == 'monster':
                damage = random.randint((Monster.monsterlvl)*5, (Monster.monsterlvl)*7)
                Player.health = Player.health - damage
                screen.addstr(0, 26, '| In Battle | The %s has hit you for %s damage!'%(Monster.monster, damage))
                screen.addstr(1, 26, '            | The %s has %s health'%(Monster.monster, Monster.monsterhp))
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
                Monster.monsterhp = Monster.monsterhp - 5
                screen.addstr(0, 26, '| In Battle | You have hit the monster for 5 damage!')
                screen.addstr(1, 26, '            | The %s has %s health'%(Monster.monster, Monster.monsterhp))
                turn = 'monster'
            screen.addstr(0, 10, 'health:')
            screen.addstr(0, 17, '%s/%s'%(Player.health, Player.healthmax))
            screen.addstr(0, 0, 'gold:')
            screen.addstr(0, 5, '%s'%(Player.gold))
            coninv = False
            char = screen.getch()
            if char == 105:
                while coninv == False:
                    coninv = inventory()
                coninv = False
        Player.healthmax = Player.healthmax + 5
        Player.gold = Player.gold + Monster.monsterlvl * 5
        Monster.monsterlvl = Monster.monsterlvl + 1
        Player.health = Player.healthmax
        screen.clear()
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        screen.addstr(0, 10, 'health:')
        screen.addstr(0, 17, '%s/%s'%(Player.health, Player.healthmax))
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 5, '%s'%(Player.gold))
        screen.addstr(0, 26, '| You have defeated the %s'%(Monster.monster))
        screen.addstr(1, 26, '| You have recieved %s gold'%(Monster.monsterlvl*5))
        nothing = screen.getch()
        wait = 1

def monsterMove():
    #global Monster.charactermon
    global currentmap
    #global Monster.monsterX
    #global Monster.monsterY
    global wait
    if wait == 1:
        currentmap[Monster.monsterY][Monster.monsterX] = '.'
        if currentmap[Monster.monsterY][Monster.monsterX + 1] != '#':
            Monster.monsterX = Monster.monsterX + 1
        elif currentmap[Monster.monsterY][Monster.monsterX - 1] != '#':
            Monster.monsterX = Monster.monsterX - 1
        elif currentmap[Monster.monsterY + 1][Monster.monsterX] != '#':
            Monster.monsterY = Monster.monsterY + 1
        elif currentmap[Monster.monsterY - 1][Monster.monsterX] != '#':
            Monster.monsterY = Monster.monsterY - 1
        wait = 0
        return 0
    suc = 0
    while suc == 0:
        rand = random.randint(0, 3)
        if rand == 0 and currentmap[Monster.monsterY][Monster.monsterX + 1] != '#':
            suc = 1
            currentmap[Monster.monsterY][Monster.monsterX + 1] = Monster.charactermon
            currentmap[Monster.monsterY][Monster.monsterX] = '.'
            Monster.monsterX = Monster.monsterX + 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        elif rand == 1 and currentmap[Monster.monsterY][Monster.monsterX - 1] != '#':
            suc = 1
            currentmap[Monster.monsterY][Monster.monsterX - 1] = Monster.charactermon
            currentmap[Monster.monsterY][Monster.monsterX] = '.'
            Monster.monsterX = Monster.monsterX - 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        elif rand == 2 and currentmap[Monster.monsterY - 1][Monster.monsterX] != '#':
            suc = 1
            currentmap[Monster.monsterY - 1][Monster.monsterX] = Monster.charactermon
            currentmap[Monster.monsterY][Monster.monsterX] = '.'
            Monster.monsterY = Monster.monsterY - 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        elif rand == 2 and currentmap[Monster.monsterY + 1][Monster.monsterX] != '#':
            suc = 1
            currentmap[Monster.monsterY + 1][Monster.monsterX] = Monster.charactermon
            currentmap[Monster.monsterY][Monster.monsterX] = '.'
            Monster.monsterY = Monster.monsterY + 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))

def buy():
    #global Player.gold
    #global Player.consumables['potion']['amount']
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
    #global Player.playerX
    #global Player.playerY
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
    #global Player.playerX
    #global Player.playerY
    if char == curses.KEY_RIGHT and currentmap[Player.playerY][Player.playerX + 1] != '#':
        end = store('right')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX + 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX + 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
    elif char == curses.KEY_LEFT and currentmap[Player.playerY][Player.playerX - 1] != '#':
        end = store('left')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY][Player.playerX - 1] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerX = Player.playerX - 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
    elif char == curses.KEY_UP and currentmap[Player.playerY - 1][Player.playerX] != '#':
        end = store('up')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY - 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY - 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
    elif char == curses.KEY_DOWN and currentmap[Player.playerY + 1][Player.playerX] != '#':
        end = store('down')
        if end == 1:
            end = 2
            return 0
        currentmap[Player.playerY + 1][Player.playerX] = '@'
        currentmap[Player.playerY][Player.playerX] = '.'
        Player.playerY = Player.playerY + 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
    monsterMove()
    fight('monster')

def inventory():
    #global Player.consumables['potion']['amount']
    #global Player.health
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

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=20, cols=68))

screen = curses.initscr()

curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.curs_set(0)

titlescreen()
playerset()

try:
    while True:
        screen.clear()
        screen.addstr(0, 10, 'health:')
        screen.addstr(0, 17, '%s/%s'%(Player.health, Player.healthmax))
        screen.addstr(0, 26, '| Commands: i:inventory, h:help')
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 5, '%s'%(Player.gold))
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in currentmap))
        char = screen.getch()
        move(char)
        if char == 105:
            while coninv == False:
                coninv = inventory()
        coninv = False
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
