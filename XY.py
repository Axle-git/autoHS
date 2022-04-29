# Constants and function to easily find coordinates (X,Y)
# Valid for 1920x1080 screens

import pyautogui
import time


####    HS    ####
END_TURN = (1600,490)
HAND_LEFT = (700,1030)
HAND_RIGHT = (1200,1030)
HERO = (960,820)
ENEMY_HERO = (960,200)
ENEMY_MINION = (960,420)
BOARD_LEFT = (550,600)
BOARD_RIGHT = (1400,600)
ENEMY_BOARD_MID = (960,410)
ALT_PLAY = (1130,830)
OKAY = (960,640)
####    ####


####    BGs    ####
PLAY_BG = (1450,850)
HERO_SLOT_2 = (840,525)
MID_MINION_BG = (960,400)
LEVEL = (800,200)
BOARD_MID = (1000,600)
BOARD_RIGHT = (1430,600)
ROLL = (1120,210)
BOB = (960,160)
FREEZE = (1240,175)
####    ####


####    General    ####
HP = (1140,830)
PAUSE = (1880,1060)
CONFIRM = (960,860)
CONCEDE = (960,390)
CANCEL = (970,920)
####    ####

def find_XY():

    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + " "
        print(positionStr, end='\r')

# find_XY()

