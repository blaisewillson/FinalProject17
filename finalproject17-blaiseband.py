import numpy
import curses
import random
import sys
import time

# make sure to use screen.addstr print doesn't work with curses

map1 = numpy.array([['#','#','#','#','#','#','#','#'],
   	 	            ['#','.','.','.','#','.','.','#'],
   	 	            ['#','.','@','.','.','.','.','#'],
   	 	            ['#','.','.','.','#','.','.','#'],
   	 	            ['#','#','.','#','#','#','.','#'],
   	 	            ['#','.','.','.','.','#','.','#'],
   	 	            ['#','$','.','.','.','#','s','#'],
   	 	            ['#','#','#','#','#','#','#','#']])
playerX = 2
playerY = 2
monsterX = 6
monsterY = 6
potion = 1
health = 20
healthmax = 20
coninv = False
gold = 100
charactermon = 's'
monsterlvl = 1
wait = 0

def endgame():
    screen.clear()
    screen.addstr(0,0,'you have lost')
    time.sleep(10)
    sys.exit()


def fight(turn):
    global monsterX
    global monsterY
    global playerX
    global playerY
    global monsterlvl
    global health
    global gold
    global wait
    monster = 'snake'
    monsterhp = monsterlvl * 10

    if monsterX == playerX + 1 and monsterY == playerY or monsterX == playerX and monsterY == playerY -1 or monsterY == playerY + 1 and monsterX == playerX or monsterY == playerY - 1 and monsterX == playerX:
        if turn == 'player':
            screen.clear()
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
            screen.addstr(0, 10, 'health:')
            screen.addstr(0, 17, '%s'%(health))
            screen.addstr(0, 20, '| It is a level %s %s with %s health.'%(monsterlvl, monster, monsterhp))
            screen.addstr(0, 0, 'gold:')
            screen.addstr(0, 5, '%s'%(gold))
            screen.getch()

        while monsterhp > 0:
            screen.clear()
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
            if turn == 'monster':
                damage = random.randint(monsterlvl*5, monsterlvl*7)
                health = health - damage
                screen.addstr(0, 20, '| In Battle | The %s has hit you for %s damage!'%(monster, damage))
                screen.addstr(1, 20, '            | The %s has %s health'%(monster, monsterhp))
                if health <=0:
                    endgame()
                turn = 'player'
            elif turn == 'player':
                monsterhp = monsterhp - 5
                screen.addstr(0, 20, '| In Battle | You have hit the monster for 5 damage!')
                screen.addstr(1, 20, '            | The %s has %s health'%(monster, monsterhp))
                turn = 'monster'
            screen.addstr(0, 10, 'health:')
            screen.addstr(0, 17, '%s'%(health))
            screen.addstr(0, 0, 'gold:')
            screen.addstr(0, 5, '%s'%(gold))
            char = screen.getch()
            if char == 105:
                while coninv == False:
                    coninv = inventory()
                coninv = False
        screen.addstr(0, 20, 'You have defeated the %s'%(monster))
        screen.addstr(1, 20, 'You have recieved %s'%(monsterlvl*1.5))
        gold = gold * 1.5
        nothing = screen.getch
        wait = 1

def monsterMove():
    global charactermon
    global map1
    global monsterX
    global monsterY
    global wait
    if wait == 1:
        map1[monsterY][monsterX] = '.'
        if map1[monsterY][monsterX + 1] != '#':
            monsterX = monsterX + 1
        elif map1[monsterY][monsterX - 1] != '#':
            monsterX = monsterX - 1
        elif map1[monsterY + 1][monsterX] != '#':
            monsterY = monsterY + 1
        elif map1[monsterY - 1][monsterX] != '#':
            monsterY = monsterY - 1
        wait = 0
        return 0
    suc = 0
    while suc == 0:
        rand = random.randint(0, 3)
        if rand == 0 and map1[monsterY][monsterX + 1] != '#':
            suc = 1
            map1[monsterY][monsterX + 1] = charactermon
            map1[monsterY][monsterX] = '.'
            monsterX = monsterX + 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
        elif rand == 1 and map1[monsterY][monsterX - 1] != '#':
            suc = 1
            map1[monsterY][monsterX - 1] = charactermon
            map1[monsterY][monsterX] = '.'
            monsterX = monsterX - 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
        elif rand == 2 and map1[monsterY - 1][monsterX] != '#':
            suc = 1
            map1[monsterY - 1][monsterX] = charactermon
            map1[monsterY][monsterX] = '.'
            monsterY = monsterY - 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
        elif rand == 2 and map1[monsterY + 1][monsterX] != '#':
            suc = 1
            map1[monsterY + 1][monsterX] = charactermon
            map1[monsterY][monsterX] = '.'
            monsterY = monsterY + 1
            screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))

def buy():
    global map1
    global playerX
    global playerY
    global gold
    global potion
    amount = 48
    while amount == 48:
        screen.clear()
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 6, '%s'%(gold))
        screen.addstr(0, 10, '| Store | e:exit')
        screen.addstr(1, 0, 'Press the number next to the item you want to buy')
        screen.addstr(2, 0, '1. potion: 50 gold')
        itemchoice = screen.getch()
        if itemchoice == 101:
            return 0
        screen.clear()
        screen.addstr(1, 0, 'How many?')
        amount = screen.getch()
        if itemchoice == 49 and gold >= 50 * (amount - 48) and amount != 48:
        	potion = potion + (amount - 48)
        	gold = gold - 50 * (amount - 48)

def store(direction):
    global map1
    global playerX
    global playerY
    if map1[playerY - 1][playerX] == '$' and direction == 'up':
        buy()
        return 1
    elif map1[playerY + 1][playerX] == '$' and direction == 'down':
        buy()
        return 1
    elif map1[playerY][playerX + 1] == '$' and direction == 'right':
        buy()
        return 1
    elif map1[playerY][playerX - 1] == '$' and direction == 'left':
        buy()
        return 1
    return 2

def move(char):
    global map1
    global playerX
    global playerY
    if char == curses.KEY_RIGHT and map1[playerY][playerX + 1] != '#':
        end = store('right')
        if end == 1:
            end = 2
            return 0
        map1[playerY][playerX + 1] = '@'
        map1[playerY][playerX] = '.'
        playerX = playerX + 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
    elif char == curses.KEY_LEFT and map1[playerY][playerX - 1] != '#':
        end = store('left')
        if end == 1:
            end = 2
            return 0
        map1[playerY][playerX - 1] = '@'
        map1[playerY][playerX] = '.'
        playerX = playerX - 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
    elif char == curses.KEY_UP and map1[playerY - 1][playerX] != '#':
        end = store('up')
        if end == 1:
            end = 2
            return 0
        map1[playerY - 1][playerX] = '@'
        map1[playerY][playerX] = '.'
        playerY = playerY - 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
    elif char == curses.KEY_DOWN and map1[playerY + 1][playerX] != '#':
        end = store('down')
        if end == 1:
            end = 2
            return 0
        map1[playerY + 1][playerX] = '@'
        map1[playerY][playerX] = '.'
        playerY = playerY + 1
        fight('player')
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
    monsterMove()
    fight('monster')
def inventory():
    global potion
    global health
    screen.clear()
    screen.addstr(0, 0, 'gold:')
    screen.addstr(0, 5, '%s'%(gold))
    screen.addstr(0, 10, '| Inventory | e:exit')
    screen.addstr(1, 0, 'Press the number next to the item you want to use')
    screen.addstr(2, 0, '1. potions: %s'%(potion))
    itemchoice = screen.getch()
    if itemchoice == 101:
        return True
    elif itemchoice == 49 and potion != 0:
        if health + 10 >= healthmax and health != healthmax:
            health = healthmax
            potion = potion - 1
        elif health + 10 < healthmax:
            health = health + 10
            potion = potion - 1
        elif health == healthmax:
            return False
        return True
    else:
        return False

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

screen.addstr(0, 0, 'gold:')
screen.addstr(0, 5, '%s'%(gold))
screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))

try:
    while True:
        screen.clear()
        screen.addstr(0, 10, 'health:')
        screen.addstr(0, 17, '%s'%(health))
        screen.addstr(0, 20, '| Commands: i:inventory, h:help')
        screen.addstr(0, 0, 'gold:')
        screen.addstr(0, 5, '%s'%(gold))
        screen.addstr(1, 0, '\n'.join(''.join(str(cell) for cell in row) for row in map1))
        char = screen.getch()
        move(char)
        if char == 105:
            while coninv == False:
                coninv = inventory()
        coninv = False
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
