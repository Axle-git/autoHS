#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import L
import time
import pyautogui
import XY
pyautogui.PAUSE = .2
import random
from pyautogui import click
from pyautogui import locateOnScreen
from random import randint

# Menagerie Build

# currently no Demons nor Pirates to keep down on time
# most prefered at top
Prefered = ["Lightfang.png",    # *****
            "DONG.png",         # all ******
            "Poison_Loc.png",   # murloc *****
            "Hydra.png",        # beast ****
            "Div_Ele.png",      # elemental ***
            "Menag_Hulk.png",   # *****
            "Div_Reb_Drag.png", # dragon ***
            "Deflecto.png",     # mech ***
            "Div_Gem.png",           # quilboar ***
            "Menag_Jug.png",    # **
            "Menag_Cup.png"     # ****
            ]

# only things worth freezing for
FreezeFor = ["Lightfang.png",
             "DONG.png"
             ]


def getStarted(): # make sure the bot doesn't simply roll continuous for the first couple plays

    time.sleep(5)
    while not locateOnScreen("Bob.png", confidence = .9):

        turnTime = time.time()

        print("Getting Started...                    ", end = '\r') # status

    time.sleep(20)
    click(XY.ENEMY_MINION) # first minion
    click(XY.HAND_LEFT)
    time.sleep(3)

    playCards()

    print("Waiting for turn 2...         ", end = '\r')
    time.sleep(50) # turn 2, 1 minion

    Level(2)

    print("Waiting for turn 3...         ", end = '\r')
    time.sleep(60) # turn 3, 2 minions

    click(XY.BOARD_MID)# sell lvl 1 minion for 2 lvl 2
    time.sleep(1)
    click(XY.BOB)
    time.sleep(4)

    click(XY.ENEMY_MINION[0] + 30,XY.ENEMY_MINION[1]) # first minion
    time.sleep(1)
    click(XY.HAND_LEFT)
    time.sleep(4)

    click(XY.ENEMY_MINION[0],XY.ENEMY_MINION[1]) # second minion
    time.sleep(1)
    click(XY.HAND_LEFT)
    time.sleep(4)

    playCards()

    print("Waiting for turn 4...         ", end = '\r')
    time.sleep(50) # turn 4, 4 minions

    click(XY.ENEMY_MINION[0] + 30,XY.ENEMY_MINION[1]) # first minion
    click(XY.HAND_LEFT)
    time.sleep(4)

    click(XY.ENEMY_MINION[0],XY.ENEMY_MINION[1]) # second minion
    click(XY.HAND_LEFT)
    time.sleep(4)

    playCards()

    print("Waiting for turn 5...         ", end = '\r')
    time.sleep(50) # turn 5

    # return control to autoBG

    return

def findPrefered(): # returns prefered in shop

    for i in Prefered:
        print("Looking for " + i + "            ", end = '\r')
        curr = locateOnScreen(i, confidence = .6)
        if curr and curr[1]  < 500:
            return locateOnScreen(i, confidence = .6)

    return

def Freeze():
    
    for i in FreezeFor:
        curr = locateOnScreen(i, confidence = .6)
        if curr and curr[1]  < 500:
            click(XY.FREEZE)

    return


def Level(turns):

    print("Leveling...           ", end = '\r')

    if turns in [2,5,7,8,11,12,13,14,15]: # in case turn counter gets off still try to level later on
        click(XY.LEVEL[0] + randint(-13,13), XY.LEVEL[1] + randint(-13,13))
        click(100, 500 + randint(-13,13))
    return


def buyCards():

    print("Buying Cards...               ", end = '\r')     

    for i in range(3): # do 3 times
        # time.sleep(5) # delay for animations
        curr = findPrefered()
        if curr:
            click(curr) # buy card
            time.sleep(1)
            click(XY.HAND_LEFT)
        else:
            click(XY.ROLL[0] + randint(-13,13), XY.ROLL[1] + randint(-13,13))
            time.sleep(4) # delay for animations
    return


def moveCards(): # make sure proper cards are sold
    
    print("Moving Cards...               ", end = '\r')

    for i in reversed(Prefered): # basically a bubble sort
        for j in range(2): # do twice for consistancy and in case two are on board
            curr = locateOnScreen(i,confidence = .6)
            if curr:
                if (curr[1] > 500) and (not i == "Menag_Jug.png" and not i == "Menag_Cup.png"):
                    click(locateOnScreen(i,confidence = .6))
                    click(100 + randint(-13,13),500 + randint(-13,13)) # iT JUST WORKS IDK
                    time.sleep(1)
    return


def playCards():

    startTime = time.time()

    counter = 0
    while not locateOnScreen("Empty_Hand.png", confidence = .8):

        print("Playing Cards...                ", end = '\r')
        click(XY.HAND_LEFT[0] + randint(-13,13) + 250, XY.HAND_LEFT[1] + randint(-13,13))
        click(XY.BOARD_MID[0] + randint(-13,13),XY.BOARD_MID[1] + randint(-13,13))
        # click(100 + randint(-13,13),500 + randint(-13,13)) # click off to side to deselect any cards

        if not counter % 8:
            sellCard()

        if time.time() - startTime > 20: # 20 seconds max
            break

        counter += 1

    return

def sellCard(): # sell leftmost card if 7 cards available

    print("Selling Card...              ", end = '\r' )

    time.sleep(1)
    click(XY.BOARD_LEFT[0] + randint(-13,13) - 20,XY.BOARD_LEFT[1] + randint(-13,13))
    time.sleep(1)
    click(XY.BOB)

    return


def autoBG():

    while not locateOnScreen('Play.png', confidence = .8) and not locateOnScreen('Alt_Play.png', confidence = .8): # wait for play to be available
        print("Waiting for Play button",end = '\r')
        
    # time.sleep(30)
    click(1400 + randint(-13,13), 880 + randint(-13,13)) # click Play!

        # wait for initializer
    startTime = time.time()
    while not locateOnScreen('initializer_BG.png', confidence = .8): # wait for match
        print("Waiting for initializer " + str(round(time.time() - startTime,1)) + str(" seconds         "),end = '\r')
        
        if locateOnScreen("Okay.png", confidence = .8):
            click(XY.OKAY)
            return 2 # new exit code
        
        if time.time() - startTime > 120: # two minutes to reset
            click(XY.CANCEL)
            click(XY.CANCEL) # cancel and try again
            startTime = time.time()

            time.sleep(5)
            click(1400 + randint(-13,13), 880 + randint(-13,13)) # click Play!

    click(XY.HERO_SLOT_2[0] + randint(-13,13),XY.HERO_SLOT_2[1] + randint(-13,13))

    click(XY.CONFIRM[0] + randint(-13,13), XY.CONFIRM[1] + randint(-13,13))

    print("Beginning Battle                            ")

    turns = 5 # offset by getStarted

    getStarted() # fill board before takeover
    print("Entering AutoBattler           ", end = '\r')

    while True: # main game loop

        while not locateOnScreen("Bob.png", confidence = .9):

            print("Waiting for turn                    ", end = '\r') # status

            time.sleep(5)
            # click around middle to cover edge cases
            click(1000 + randint(-200,200),500 + randint(-13,13)) # click middle of screen
            if locateOnScreen('Play.png', confidence = .8) and not locateOnScreen('Alt_Play.png', confidence = .8):
                return 1 

        Level(turns)

        turnTime = time.time()

        while time.time() - turnTime < 60: # do for 40 seconds

            if locateOnScreen("Battle_Phase.png",confidence = .8): # check if battle phase is active
                break

            time.sleep(1) # delay
            buyCards()

            time.sleep(1)
            moveCards()

            time.sleep(1) # delay
            playCards()

            time.sleep(1) # delay
            moveCards()

            Freeze()

        # while not locateOnScreen("Battle_Phase.png", confidence = .8):
        #     print("Waiting for Battle Phase...            ", end = '\r')

        #     time.sleep(5)
        #     click(1000 + randint(-13,13),500 + randint(-13,13)) # click middle of screen
        #     if locateOnScreen("Play.png"):
        #         return 1             

        turns += 1




    return 1



def main():

    time.sleep(2) # time to stop between games

    startTime = time.time()


    battles = 0

    while True:
        if autoBG() == 1: # other exit codes indicate an incomplete / non-started game
            battles += 1
        print("\nBattle #" + str(battles) + " Complete                 ")
        print("Total hours elapsed: " + str(round((time.time()-startTime)/3600,2)) + "\n")

    print("\nDone\n")

    print("Ran for a total of " + str((time.time()-startTime)/3600) + " hours.")
    print("Fought a total of " + str(battles) + "battles.")

    return 0

if __name__ == "__main__":
    main()
