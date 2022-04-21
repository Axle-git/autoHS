#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import L
import time
import pyautogui
import XY
pyautogui.PAUSE = .2
import random

 # + random.randint(-25,25)
 # a function to wiggle the clicks to be harder to detect as a bot

def playCards():

    X = XY.HAND_LEFT # play cards on active spot 75%, first bench 25%
    i = 0 
    while i < 501:
        pyautogui.click(X[0]+i + random.randint(-25,25),X[1] + random.randint(-25,25)) # click card
        
        pyautogui.click(XY.BOARD_LEFT[0] + random.randint(0,920) + random.randint(-25,25) ,XY.BOARD_RIGHT[1] + random.randint(-25,25)) # click board

        i += 100 # shift right

    return

def attack(): # attacks face only

    for i in range(7):
        pyautogui.click(XY.BOARD_LEFT[0] + i*131 + random.randint(-25,25), XY.BOARD_LEFT[1] + random.randint(-25,25)) # board length / 7 minion slots
        pyautogui.click(XY.ENEMY_HERO[0] + random.randint(-25,25), XY.ENEMY_HERO[1] + random.randint(-25,25)) # face

    pyautogui.click(XY.HP[0] + random.randint(-25,25), XY.HP[1] + random.randint(-25,25)) # use hero power, probably hunter's

    return

def Done():
    pyautogui.click(XY.CONFIRM[0] + random.randint(-25,25), XY.CONFIRM[1] + random.randint(-25,25))
    pyautogui.click(XY.END_TURN[0] + random.randint(-25,25), XY.END_TURN[1] + random.randint(-25,25))

    return

def autoBattle():

    print("\n")

    while not pyautogui.locateOnScreen('Play.png', confidence = .8): # wait for play to be available
        print("Waiting for Play button",end = '\r')
        pass
    pyautogui.click(1400 + random.randint(-25,25), 880 + random.randint(-25,25)) # click Play!

    # wait for initializer
    while not pyautogui.locateOnScreen('initializer.png', confidence = .8): # wait for match
        print("Waiting for initializer",end = '\r')
        pass

    pyautogui.click(XY.CONFIRM[0] + random.randint(-25,25), XY.CONFIRM[1] + random.randint(-25,25))

    print("Beginning Battle")

    i = 0
    while True: # main game loop

        playCards()
        attack()
        if not i % 3:
            Done()

        i += 1
        if i % 5:
            if pyautogui.locateOnScreen('Play.png', confidence = .8):
                return 1


def main():

    time.sleep(2) # time to stop between games

    startTime = time.time()


    battles = 0

    while autoBattle():
        battles += 1
        print("Battle #" + str(battles) + " Complete                 ")
        print("Total hours elapsed: " + str((time.time()-startTime)/3600))

    print("\nDone\n")

    print("Ran for a total of " + str((time.time()-startTime)/3600) + " hours.")
    print("Fought a total of " + str(battles) + "battles.")

    return 0

if __name__ == "__main__":
    main()