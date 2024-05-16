import pygame
from pygame import mixer
import time
pygame.init()

start = True

gameState = 'notWin'

seconds = time.time()

widthx = 448
widthy = 496+32

screen = pygame.display.set_mode((widthx,widthy))

running = True

cheatcode = ""
cheatCodestate = 'notActivated'
changeApply = False

def applyCheatCode():
    global changeApply,cheatCodestate,cheatcode
    if cheatcode == '971045457':
        cheatCodestate = 'Activated'
        changeApply = True
        cheatcode = ''
    elif cheatcode == '575410497':
        changeApply = False
        cheatCodestate = 'Activated'
        cheatcode = ''
    elif len(cheatcode) > 15:
        cheatcode = ''
        cheatCodestate = 'Activated'
    else:
        pass

def Activated():
    global cheatCodestate
    if cheatCodestate == 'Activated':
        mixer.music.load('blipSelect.wav')
        mixer.music.play()
        cheatCodestate = 'notActivated'


class Maze():
    def __init__(self):
        self.width = widthx//28
        self.images = {
            '0' : pygame.transform.scale(pygame.image.load('0.png'),(widthx//28,widthx//28)),
            '0 1' : pygame.transform.scale(pygame.image.load('1.png'),(widthx//28,widthx//28)),
            '0 2' : pygame.transform.scale(pygame.image.load('2.png'),(widthx//28,widthx//28)),
            '0 3' : pygame.transform.scale(pygame.image.load('3.png'),(widthx//28,widthx//28)),
            '0 4' : pygame.transform.scale(pygame.image.load('4.png'),(widthx//28,widthx//28)),
            '0 2 3' : pygame.transform.scale(pygame.image.load('5.png'),(widthx//28,widthx//28)),
            '0 2 4' : pygame.transform.scale(pygame.image.load('6.png'),(widthx//28,widthx//28)),
            '0 1 2 3' : pygame.transform.scale(pygame.image.load('7.png'),(widthx//28,widthx//28)),
            '0 1 2 3 4' : pygame.transform.scale(pygame.image.load('1 2 3 4.png'),(widthx//28,widthx//28)),
            '0 1 3 4' : pygame.transform.scale(pygame.image.load('8.png'),(widthx//28,widthx//28)),
            '0 2 3 4' : pygame.transform.scale(pygame.image.load('9.png'),(widthx//28,widthx//28)),
            '0 1 2' : pygame.transform.scale(pygame.image.load('1 2.png'),(widthx//28,widthx//28)),
            '0 1 3' : pygame.transform.scale(pygame.image.load('1 4.png'),(widthx//28,widthx//28)),
            '0 1 4' : pygame.transform.scale(pygame.image.load('1 5.png'),(widthx//28,widthx//28)),
            '0 3 4' : pygame.transform.flip(pygame.transform.scale(pygame.image.load('1 5.png'),(widthx//28,widthx//28)),True,False),
            '0 1 2 4' : pygame.transform.scale(pygame.image.load('1 7.png'),(widthx//28,widthx//28)),
            'normalbutton' : pygame.transform.scale(pygame.image.load('powerbutton.png'),(self.width,self.width)),
            'powerbutton' : pygame.transform.scale(pygame.image.load('powerbutton2.png'),(self.width,self.width)),
            'pipe' : pygame.transform.scale(pygame.image.load('pipe.png'),(self.width,self.width)),
        }
        self.blinking = 'Now'
        self.maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,4,4,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,2,0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,2,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.setmaze = self.maze

    def checkingWin(self):
        global gameState
        sum = 0
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 0:
                    sum += 1
        
        if sum == 0:
            gameState = 'Lost'
        
    def displayingMaze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 1:
                    tilesum = '0'
                    if j - 1 >= 0:
                        if self.maze[i][j - 1] == 1:
                            tilesum += ' 1'
                    if i - 1 >= 0:
                        if self.maze[i - 1][j] == 1:
                            tilesum += ' 2'
                    if j + 1 < len(self.maze[i]):
                        if self.maze[i][j + 1] == 1:
                            tilesum += ' 3'
                    if i + 1 < len(self.maze):
                        if self.maze[i + 1][j] == 1:
                            tilesum += ' 4'
                    screen.blit(self.images[tilesum],(j*self.width,i*self.width))
                if self.maze[i][j] == 0:
                    screen.blit(self.images['normalbutton'],(j*self.width,i*self.width))
                if self.maze[i][j] == 3:
                    if self.blinking == 'Now':
                        screen.blit(self.images['powerbutton'],(j*(self.width),i*(self.width)))
                if self.maze[i][j] == 4:
                    screen.blit(self.images['pipe'],(j*(self.width),i*(self.width)))

window = Maze()

class Pacman():
    def __init__(self):
        self.width = widthx//28
        self.x = 16*14
        self.setx = 16*14
        self.sety = 16*23
        self.lives = 3
        self.lives = 3
        self.y = 16*23
        self.eating = False
        self.radius = 8
        self.dir = 'stop'
        self.newdir = 'stop'
        self.pacman1 = pygame.transform.scale(pygame.image.load('pacman1.png'),(widthx//28,widthx//28))
        self.pacman2 = pygame.transform.scale(pygame.image.load('pacman2.png'),(widthx//28,widthx//28))
        self.pacman3 = pygame.transform.scale(pygame.image.load('pacman3.png'),(widthx//28,widthx//28))

        self.pacman11 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman1.png'),(widthx//28,widthx//28)),90)
        self.pacman21 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman2.png'),(widthx//28,widthx//28)),90)
        self.pacman31 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman3.png'),(widthx//28,widthx//28)),90)

        self.pacman12 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman1.png'),(widthx//28,widthx//28)),180)
        self.pacman22 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman2.png'),(widthx//28,widthx//28)),180)
        self.pacman32 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman3.png'),(widthx//28,widthx//28)),180)

        self.pacman13 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman1.png'),(widthx//28,widthx//28)),270)
        self.pacman23 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman2.png'),(widthx//28,widthx//28)),270)
        self.pacman33 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('pacman3.png'),(widthx//28,widthx//28)),270)
        self.score = 0
        self.checkdir = 'right'
        self.pacmanList1 = [self.pacman1,self.pacman2,self.pacman3]
        self.pacmanList2 = [self.pacman11,self.pacman21,self.pacman31]
        self.pacmanList3 = [self.pacman12,self.pacman22,self.pacman32]
        self.pacmanList4 = [self.pacman13,self.pacman23,self.pacman33]
        self.pacmanList = self.pacmanList1

        self.index = 0
        self.pacman = self.pacmanList[self.index]

    def displayingLives(self):
        for i in range(self.lives):
            screen.blit(self.pacman1,(i*16+10,widthy-25))

    def displayingPacman(self):
        self.pacman = self.pacmanList[self.index]
        screen.blit(self.pacman,(self.x,self.y))

    def animatingPacman(self):
        if self.dir != 'stop':
            if self.index < len(self.pacmanList) - 1:
                self.index += 1
            else:
                self.index = 0
        else:
            self.index = 0
    

    def settingDir(self):
        if self.newdir == 'right':
            if self.x//window.width + 1 < len(window.maze[self.y//window.width]):
                if window.maze[self.y//window.width][self.x//window.width + 1] != 1:
                    self.dir = 'right'
                    self.newdir = 'stop'
        if self.newdir == 'left':
            if self.x//window.width - 1 > 0:
                if window.maze[self.y//window.width][self.x//window.width - 1] != 1:
                    self.dir = 'left'
                    self.newdir = 'stop'

        if self.newdir == 'down':
            if self.y//window.width + 1 < len(window.maze):
                if window.maze[self.y//window.width + 1][self.x//window.width] != 1 and window.maze[self.y//window.width + 1][self.x//window.width] != 4:
                    self.dir = 'down'
                    self.newdir = 'stop'

        if self.newdir == 'up':
            if self.y//window.width - 1 > 0:
                if window.maze[self.y//window.width - 1][self.x//window.width] != 1 and window.maze[self.y//window.width - 1][self.x//window.width] != 4:
                    self.dir = 'up'
                    self.newdir = 'stop'


    def movingPacman(self):
        if self.dir == 'right':
            self.pacmanList = self.pacmanList1
            if (self.x//window.width) + 1 <= len(window.maze[self.y//window.width]):
                if window.maze[self.y//self.width][(self.x//self.width) + 1] != 1:
                    self.x += window.width
                else:
                    self.dir = 'stop'
        if self.dir == 'left':
            self.pacmanList = self.pacmanList3
            if window.maze[self.y//window.width][self.x//window.width - 1] != 1:
                self.x -= window.width
            else:
                self.dir = 'stop'
        if self.dir == 'up':
            self.pacmanList = self.pacmanList2
            if window.maze[self.y//window.width - 1][self.x//window.width] != 1 and window.maze[self.y//window.width - 1][self.x//window.width] != 4:
                self.y -= window.width
            else:
                self.dir = 'stop'
        if self.dir == 'down':
            self.pacmanList = self.pacmanList4
            if window.maze[self.y//window.width + 1][self.x//window.width] != 1 and window.maze[self.y//window.width + 1][self.x//window.width] != 4:
                self.y += window.width
            else:
                self.dir = 'stop'

    def eatingDots(self,ghost1state,ghost2state,ghost3state,ghost4state):
        global seconds
        y = self.y//window.width
        x = self.x//window.width
        if window.maze[y][x] == 0:
            window.maze[y][x] = 2
            self.score += 50
        if window.maze[y][x] == 3:
            window.maze[y][x] = 2
            ghost1state = 'frightened'
            ghost2state = 'frightened'
            ghost3state = 'frightened'
            ghost4state = 'frightened'
            seconds = time.time()
            self.score += 100
        return ghost1state,ghost2state,ghost3state,ghost4state
    
    def displayingScore(self):
        font = pygame.font.Font('Emulogic-zrEw.ttf',16)
        font_render = font.render('Score: ' + str(self.score),True,'white')
        screen.blit(font_render,(240,widthy-25))

    def teleportation(self):
        if self.x <= 0:
            self.x = 432
        elif self.x + self.width == 448:
            self.x = 0

pacman = Pacman()
movingpacman = pygame.USEREVENT + 0
pygame.time.set_timer(movingpacman,85)

class Ghosts():
    def __init__(self,sprite1,sprite2,sprite3,sprite4,sprite5,sprite6,sprite7,sprite8,sprite9,sprite10,sprite11):
        self.sprite1 = pygame.transform.scale(pygame.image.load(sprite1),(widthx//28,widthx//28))
        self.sprite2 = pygame.transform.scale(pygame.image.load(sprite2),(widthx//28,widthx//28))
        self.sprite3 = pygame.transform.scale(pygame.image.load(sprite3),(widthx//28,widthx//28))
        self.sprite4 = pygame.transform.scale(pygame.image.load(sprite4),(widthx//28,widthx//28))
        self.sprite5 = pygame.transform.scale(pygame.image.load(sprite5),(widthx//28,widthx//28))
        self.sprite6 = pygame.transform.scale(pygame.image.load(sprite6),(widthx//28,widthx//28))
        self.sprite7 = pygame.transform.scale(pygame.image.load(sprite7),(widthx//28,widthx//28))
        self.sprite8 = pygame.transform.scale(pygame.image.load(sprite8),(widthx//28,widthx//28))
        self.sprite9 = pygame.transform.scale(pygame.image.load(sprite9),(widthx//28,widthx//28))
        self.sprite10 = pygame.transform.scale(pygame.image.load(sprite10),(widthx//28,widthx//28))
        self.sprite11 = pygame.transform.scale(pygame.image.load(sprite11),(widthx//28,widthx//28))
        self.chaseSprite = [self.sprite9,self.sprite8,self.sprite7,self.sprite6,self.sprite5,self.sprite4,self.sprite3,self.sprite2,self.sprite1]
        self.frightSprite = [self.sprite10,self.sprite11]
        self.index = 0
        self.spriteList = self.chaseSprite
        self.sprite = self.spriteList[self.index]
        self.x = 16
        self.setx = self.x
        self.y = 16
        self.width = 16
        self.sety = self.y
        self.index2 = 0
        self.name = ''
        self.state = 'chasing'
        self.dir = 'stop'
        self.directions = ['right','up','down','left']

    def teleportation(self):
        if self.x <= 0:
            self.x = 432
        elif self.x + self.width == 448:
            self.x = 0

    def scatter(self):
        # similar to chase but they target and revolve around a certain block to let the pacman escape
        target = [self.setx//16,self.sety//16]

        distance = 0
        candir = self.dir
        x = self.x//16
        y = self.y//16

        if x - 1 >= 0:
            if window.maze[y][x-1] != 1:
                distx = 0
                disty = 0
                if target[0] > x-1: 
                    distx = target[0] - (x-1)
                if target[0] < x-1:
                    distx = (x-1) - target[0]
                if target[1] > y:
                    disty = target[1] - y
                if target[1] < y:
                    disty = y - target[1]

                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if self.dir != 'left':
                        candir = 'left'

        if x + 1 < len(window.maze[0]):
            if window.maze[y][x+1] != 1:
                distx = 0
                disty = 0
                if target[0] > x+1: 
                    distx = target[0] - (x+1)
                if target[0] < x+1:
                    distx = (x+1) - target[0]
                if target[1] > y:
                    disty = target[1] - y
                if target[1] < y:
                    disty = y - target[1]

                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if self.dir != 'right':
                        candir = 'right'

        if y + 1 < len(window.maze):
            if window.maze[y+1][x] != 1:
                distx = 0
                disty = 0
                if target[0] > x: 
                    distx = target[0] - (x)
                if target[0] < x:
                    distx = (x) - target[0]
                if target[1] > y+1:
                    disty = target[1] - (y+1)
                if target[1] < y+1:
                    disty = (y+1) - target[1]

                newDistance = distx**2 + disty**2

                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if candir != 'down':
                        candir = 'down'
        if y - 1 >= 0:
            if window.maze[y-1][x] != 1:
                distx = 0
                disty = 0
                if target[0] > x: 
                    distx = target[0] - (x)
                if target[0] < x:
                    distx = (x) - target[0]
                if target[1] > y - 1:
                    disty = target[1] - (y-1)
                if target[1] < y-1:
                    disty = (y-1) - target[1]
                
                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if self.dir != 'up':
                        candir = 'up'


        if self.dir == 'right':
            if candir != 'left':
                 self.dir = candir
        elif self.dir == 'left':
            if candir != 'right':
                self.dir = candir
        elif self.dir =='up':
            if candir != 'down':
                self.dir = candir
        elif self.dir == 'down':
            if candir != 'up':
                self.dir = candir
        else:
            self.dir = candir


    def chasing(self):
        target = [pacman.x//16,pacman.y//16]
        if self.name == 'pinky':
            if pacman.checkdir == 'left':
                if pacman.x//16 - 4 > 0:
                    target = [pacman.x//16 - 4,pacman.y//16]
            if pacman.checkdir == 'right':
                if pacman.x//16 + 4 < len(window.maze[0]):
                    target = [pacman.x//16 + 4,pacman.y//16]
            if pacman.checkdir == 'up':
                if pacman.y//16 - 4 > 0:
                    target = [pacman.x//16,pacman.y//16 - 4]
            if pacman.checkdir == 'down':
                if pacman.y//16 + 4 < len(window.maze):
                    target = [pacman.x//16,pacman.y//16 + 4]
                    
        distance = 0
        candir = self.dir
        x = self.x//16
        y = self.y//16

        if x - 1 >= 0:
            if window.maze[y][x-1] != 1:
                distx = 0
                disty = 0
                if target[0] > x-1: 
                    distx = target[0] - (x-1)
                if target[0] < x-1:
                    distx = (x-1) - target[0]
                if target[1] > y:
                    disty = target[1] - y
                if target[1] < y:
                    disty = y - target[1]

                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if candir != 'left':
                        candir = 'left'

        if x + 1 < len(window.maze[0]):
            if window.maze[y][x+1] != 1:
                distx = 0
                disty = 0
                if target[0] > x+1: 
                    distx = target[0] - (x+1)
                if target[0] < x+1:
                    distx = (x+1) - target[0]
                if target[1] > y:
                    disty = target[1] - y
                if target[1] < y:
                    disty = y - target[1]

                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if candir != 'right':
                        candir = 'right'

        if y - 1 >= 0:
            if window.maze[y-1][x] != 1:
                distx = 0
                disty = 0
                if target[0] > x: 
                    distx = target[0] - (x)
                if target[0] < x:
                    distx = (x) - target[0]
                if target[1] > y - 1:
                    disty = target[1] - (y-1)
                if target[1] < y-1:
                    disty = (y-1) - target[1]
                
                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if candir != 'up':
                        candir = 'up'

        if y + 1 < len(window.maze):
            if window.maze[y+1][x] != 1:
                distx = 0
                disty = 0
                if target[0] > x: 
                    distx = target[0] - (x)
                if target[0] < x:
                    distx = (x) - target[0]
                if target[1] > y+1:
                    disty = target[1] - (y+1)
                if target[1] < y+1:
                    disty = (y+1) - target[1]

                newDistance = distx**2 + disty**2
                if distance == 0 or newDistance < distance:
                    distance = newDistance
                    if candir != 'down':
                        candir = 'down'

        if self.dir == 'right':
            if candir != 'left':
                 self.dir = candir
        elif self.dir == 'left':
            if candir != 'right':
                self.dir = candir
        elif self.dir =='up':
            if candir != 'down':
                self.dir = candir
        elif self.dir == 'down':
            if candir != 'up':
                self.dir = candir
        else:
            self.dir = candir


    def displayingGhost(self):
        if self.state == 'chasing':
            self.sprite = self.chaseSprite[self.index]
        if self.state == 'frightened':
            self.sprite = self.frightSprite[self.index2]

        screen.blit(self.sprite,(self.x,self.y))

    def animatingSprite(self):
        if self.state != 'frightened':
            self.index += 1
            if self.index > len(self.chaseSprite) - 1:
                self.index = 0
        if self.state == 'frightened':
            self.index2 += 1
            if self.index2 > len(self.frightSprite) - 1:
                self.index2 = 0

    def resettingState(self):
        global seconds
        if self.state == 'frightened':
            currentTime = time.time()
            if int(currentTime) - int(seconds) > 5:
                self.state = 'chasing'
                self.spriteList = self.chaseSprite
                self.index = 0
        else:
            pass
            
    def movingGhost(self):
        if self.dir == 'right':
            self.x += widthx//28
        if self.dir == 'left':
            self.x -= widthx//28
        if self.dir == 'up':
            self.y -= widthx//28
        if self.dir == 'down':
            self.y += widthx//28
    
    def colliding(self):
        global gameState
        x = self.x//window.width
        y = self.y//window.width
        if self.dir == 'up':
            if y - 1 >= 0:
                if window.maze[y - 1][x] == 1:
                    self.dir = 'stop'
        if self.dir == 'down':
            if y + 1 < len(window.maze):
                if window.maze[y + 1][x] == 1:
                    self.dir = 'stop'
        if self.dir == 'right':
            if x + 1 < len(window.maze[0]):
                if window.maze[y][x+1] == 1:
                    self.dir = 'stop'
        if self.dir == 'left':
            if x - 1 >= 0:
                if window.maze[y][x - 1] == 1:
                    self.dir = 'stop'

    def collidingPlayer(self):
        global pacmanx,pacmany,gameState
        x = self.x//window.width
        y = self.y//window.width
        pacmanx = pacman.x//window.width
        pacmany = pacman.y//window.width
        if pacman.lives == 0:
                gameState = 'Lost'
        # this is basically the collision of the ghosts with pacman.
        if x == pacmanx and y == pacmany:
            if self.state != 'frightened':
                if pacman.lives > 0:
                    pacman.x = pacman.setx
                    pacman.y = pacman.sety
                    pacman.dir = 'stop'
                    pacman.pacmanList = pacman.pacmanList1
                    pacman.index = 0
                    return True
                
        if x == pacmanx and y == pacmany:
            if self.state == 'frightened':
                self.x = self.setx
                self.y = self.sety
                pacman.score += 200
                self.state = 'chasing'
            
        return False
            

blinky = Ghosts('ghost1.png','ghost2.png','ghost3.png','ghost4.png','ghost5.png','ghost6.png','ghost7.png','ghost8.png','ghost9.png','fright (1).png','fright (2).png')

inky = Ghosts('cyan1.png','cyan2.png','cyan3.png','cyan4.png','cyan5.png','cyan1.png','cyan2.png','cyan3.png','cyan4.png','fright (1).png','fright (2).png')

pinky = Ghosts('pinky1 (1).png','pinky1 (2).png','pinky1 (3).png','pinky1 (4).png','pinky1 (5).png','pinky1 (1).png','pinky1 (2).png','pinky1 (3).png','pinky1 (4).png','fright (1).png','fright (2).png')

clyde = Ghosts('clyde1 (1).png','clyde1 (2).png','clyde1 (3).png','clyde1 (4).png','clyde1 (5).png','clyde1 (6).png','clyde1 (7).png','clyde1 (1).png','clyde1 (2).png','fright (1).png','fright (2).png')

inky.x = 16*26
inky.setx = inky.x

clyde.x = 16*26
clyde.setx = clyde.x

clyde.y = 16*29
clyde.sety = clyde.y

pinky.y = 16*29
pinky.sety = pinky.y

blinky.name = 'blinky'
inky.name = 'inky'
pinky.name = 'pinky'
clyde.name = 'clyde'

def changetool():
    global canChange
    x = pygame.mouse.get_pos()[0]//16
    y = pygame.mouse.get_pos()[1]//16
    if y > 0 and y < len(window.maze) and x > 0 and x < len(window.maze[0]):
        if window.maze[y][x] == 0 or window.maze[y][x] == 2:
            window.maze[y][x] = 1
        elif window.maze[y][x] == 1:
            window.maze[y][x] = 0
        else:
            pass

def Lost():
    global gameState
    if gameState == 'Lost':
        font = pygame.font.Font('Emulogic-zrEw.ttf',8)
        font_render = font.render('Game over',True,'red')
        screen.blit(font_render,(190,370))

eating = pygame.USEREVENT + 1
pygame.time.set_timer(eating,1000)

animatingGhost = pygame.USEREVENT + 2
pygame.time.set_timer(animatingGhost,200)

blinkingDots = pygame.USEREVENT + 3
pygame.time.set_timer(blinkingDots,300)

movingGhosts = pygame.USEREVENT + 4
pygame.time.set_timer(movingGhosts,125)

changingState = pygame.USEREVENT + 5
pygame.time.set_timer(changingState,10000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == movingGhosts:
            if gameState != 'Lost':
                blinky.teleportation()
                pinky.teleportation()
                clyde.teleportation()
                inky.teleportation()
                blinky.movingGhost()
                pinky.movingGhost()
                clyde.movingGhost()
                inky.movingGhost()
        if event.type == movingpacman:
            if start == True:
                if gameState != 'Lost':
                    if blinky.state == 'scatter':
                        blinky.scatter()
                    if pinky.state == 'scatter':
                        pinky.scatter()
                    if inky.state == 'scatter':
                        inky.scatter()
                    if clyde.state == 'scatter':
                        clyde.scatter()
                    if blinky.state != 'scatter':
                        blinky.chasing()
                    if pinky.state != 'scatter':
                        pinky.chasing()
                    if inky.state != 'scatter':
                        inky.chasing()
                    if clyde.state != 'scatter':
                        clyde.chasing()
                    pacman.movingPacman()
                    pacman.teleportation()
                    pacman.animatingPacman()
        if event.type == blinkingDots:
            if window.blinking == 'Now':
                window.blinking = 'NotNow'
            elif window.blinking == 'NotNow':
                window.blinking = 'Now'
        if event.type == changingState:
            if blinky.state == 'chasing':
                blinky.state = 'scatter'
            elif blinky.state == 'scatter':
                blinky.state = 'chasing'
            else:
                pass
            if pinky.state == 'chasing':
                pinky.state = 'scatter'
            elif pinky.state == 'scatter':
                pinky.state = 'chasing'
            else:
                pass
            if inky.state == 'chasing':
                inky.state = 'scatter'
            elif inky.state == 'scatter':
                inky.state = 'chasing'
            else:
                pass
            if clyde.state == 'chasing':
                clyde.state = 'scatter'
            elif clyde.state == 'scatter':
                clyde.state = 'chasing'
            else:
                pass
        if event.type == animatingGhost:
            if gameState != 'Lost':
                blinky.animatingSprite()
                pinky.animatingSprite()
                inky.animatingSprite()
                clyde.animatingSprite()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if changeApply:
                changetool()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameState != 'notWin':
                    pacman.lives = 3 
                    pacman.score = 0
                    blinky.x = blinky.setx
                    blinky.y = blinky.sety
                    pinky.x = pinky.setx
                    pinky.y = pinky.sety
                    inky.x = inky.setx
                    inky.y = inky.sety
                    clyde.x = clyde.setx
                    clyde.y = clyde.sety
                    pacman.x = pacman.setx
                    pacman.y = pacman.sety
                    gameState = 'notWin'
                    window.maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,4,4,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,2,0,0,0,0,1,2,2,2,2,2,2,1,0,0,0,0,2,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,2,2,2,2],
                [2,2,2,2,2,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,2,2,2,2,2],
                [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
                [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
                [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                [1,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
            cheatcode += str(event.key)
            if event.key == pygame.K_w:
                pacman.newdir = 'up'
                pacman.checkdir = 'up'
            if event.key == pygame.K_a:
                pacman.newdir = 'left'
                pacman.checkdir = 'left'
            if event.key == pygame.K_s:
                pacman.newdir = 'down'
                pacman.checkdir = 'down'
            if event.key == pygame.K_d:
                pacman.newdir = 'right'
                pacman.checkdir = 'right'

    screen.fill('black')
    if start == True:
        window.displayingMaze()
        if gameState != 'Lost':
            if blinky.collidingPlayer():
                pacman.lives -= 1
                blinky.x = blinky.setx
                blinky.y = blinky.sety
                pinky.x = pinky.setx
                pinky.y = pinky.sety
                clyde.x = clyde.setx
                clyde.y = clyde.sety
                inky.x = inky.setx
                inky.y = inky.sety
            if pinky.collidingPlayer():
                pacman.lives -= 1
                blinky.x = blinky.setx
                blinky.y = blinky.sety
                pinky.x = pinky.setx
                pinky.y = pinky.sety
                clyde.x = clyde.setx
                clyde.y = clyde.sety
                inky.x = inky.setx
                inky.y = inky.sety
            if clyde.collidingPlayer():
                pacman.lives -= 1
                blinky.x = blinky.setx
                blinky.y = blinky.sety
                pinky.x = pinky.setx
                pinky.y = pinky.sety
                clyde.x = clyde.setx
                clyde.y = clyde.sety
                inky.x = inky.setx
                inky.y = inky.sety
            if inky.collidingPlayer():
                pacman.lives -= 1
                blinky.x = blinky.setx
                blinky.y = blinky.sety
                pinky.x = pinky.setx
                pinky.y = pinky.sety
                clyde.x = clyde.setx
                clyde.y = clyde.sety
                inky.x = inky.setx
                inky.y = inky.sety
            pacman.displayingPacman()
            blinky.displayingGhost()
            inky.displayingGhost()
            pinky.displayingGhost()
            clyde.displayingGhost()
        window.checkingWin()
        pacman.displayingScore()
        pacman.displayingLives()
        blinky.state,pinky.state,inky.state,clyde.state = pacman.eatingDots(blinky.state,pinky.state,inky.state,clyde.state)
        blinky.colliding()
        pinky.colliding()
        clyde.colliding()
        inky.colliding()
        blinky.resettingState()
        pinky.resettingState()
        inky.resettingState()
        clyde.resettingState()
        Lost()
        applyCheatCode()
        Activated()
        pacman.settingDir()
    pygame.display.update()
