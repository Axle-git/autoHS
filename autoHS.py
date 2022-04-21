#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import L
import time
import pyautogui
import XY
pyautogui.PAUSE = .2
import random





def playCards():

    X = XY.HAND_LEFT # play cards on active spot 75%, first bench 25%
    i = 0 
    while i < 501:
        pyautogui.click(X[0]+i,X[1]) # click card
        
        pyautogui.click(XY.BOARD_LEFT[0] + random.randint(0,920),XY.BOARD_RIGHT[1]) # click board
        # pyautogui.click(75,430) # click off to side to ready cards

        i += 100 # shift right

    return

def attack(): # attacks face only
    pyautogui.click(75,430) # click off to side to ready attack

    for i in range(7):
        pyautogui.click(XY.BOARD_LEFT[0] + i*131, XY.BOARD_LEFT[1]) # board length / 7 minion slots
        pyautogui.click(XY.ENEMY_HERO) # face

    pyautogui.click(XY.HP) # use hero power, probably hunter's

    pyautogui.click(75,430) # click off to side to ready for next action

    return

def Done():
    pyautogui.click(XY.CONFIRM)
    pyautogui.click(XY.END_TURN)

    return

def autoBattle():

    while not pyautogui.locateOnScreen('Play.png', confidence = .8): # wait for play to be available
        print("Waiting for Play button",end = ' ')
        pass
    pyautogui.click(1400,880) # click Play!

    # wait for initializer
    while not pyautogui.locateOnScreen('initializer.png', confidence = .8): # wait for match
        print("Waiting for initializer",end = '\r')
        pass

    pyautogui.click(XY.CONFIRM)

    print("\nBeginning Battle\n")

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