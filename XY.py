# Constants and function to easily find coordinates (X,Y)

import pyautogui
import time

END_TURN = (1600,490)
CONFIRM = (960,860)
HAND_LEFT = (700,1000)
HAND_RIGHT = (1200,1000)
HP = (1140,830)
ENEMY_HERO = (960,200)
BOARD_LEFT = (480,600)
BOARD_RIGHT = (1400,600)
ENEMY_BOARD_MID = (960,410)

PAUSE = (1880,1060)
CONCEDE = (960,390)

def find_XY():

    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + " "
        print(positionStr, end='\r')

# find_XY()

