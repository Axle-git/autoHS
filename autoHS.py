#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import L
import time
import pyautogui
import XY
pyautogui.PAUSE = .2
import random

 # + random.randint(-13,13)
 # a function to wiggle the clicks to be harder to detect as a bot

def playCards():

    X = XY.HAND_LEFT
    for counter in range(2): # try to play the cards twice
        i = 0 
        while i < 501: # left to right then right to left
            pyautogui.click(X[0]+i + random.randint(-13,13),X[1] + random.randint(-13,13)) # click card
            
            pyautogui.click(XY.BOARD_LEFT[0] + random.randint(0,920) + random.randint(-13,13) ,XY.BOARD_RIGHT[1] + random.randint(-13,13)) # click board

            i += 100 # shift right

    return

def attack(): # attacks face only

    for i in range(7):
        # not using any except center minion rn, just seeing if it is productive
        if i == 3 or i == 2 or i == 4: # use central minions to attack central minions, artbitrary
            pyautogui.click(XY.BOARD_LEFT[0] + i*131 + 30 + random.randint(-13,13), XY.BOARD_LEFT[1] + random.randint(-13,13)) # +100 on the X because we want to hit both even and odd amount of minions
            for j in range(7):
                pyautogui.click(XY.BOARD_LEFT[0] + j*131 + random.randint(-13,13), XY.ENEMY_MINION[1] + random.randint(-13,13))
            pyautogui.click(XY.ENEMY_HERO[0] + random.randint(-13,13), XY.ENEMY_HERO[1] + random.randint(-13,13)) # face

        else:
            pyautogui.click(XY.BOARD_LEFT[0] + i*131 + random.randint(-13,13), XY.BOARD_LEFT[1] + random.randint(-13,13)) # board length / 7 minion slots
            pyautogui.click(XY.ENEMY_HERO[0] + random.randint(-13,13), XY.ENEMY_HERO[1] + random.randint(-13,13)) # face

    pyautogui.click(XY.HP[0] + random.randint(-13,13), XY.HP[1] + random.randint(-13,13)) # use hero power, probably hunter's

    pyautogui.click(XY.HERO) # attack face w/ hero (weapon)
    pyautogui.click(XY.ENEMY_HERO)

    return

def Done():
    pyautogui.click(XY.CONFIRM[0] + random.randint(-13,13), XY.CONFIRM[1] + random.randint(-13,13))
    pyautogui.click(XY.END_TURN[0] + random.randint(-13,13), XY.END_TURN[1] + random.randint(-13,13))

    return

def autoBattle():

    while not pyautogui.locateOnScreen('Play.png', confidence = .8): # wait for play to be available
        print("Waiting for Play button",end = '\r')
        pass
    pyautogui.click(1400 + random.randint(-13,13), 880 + random.randint(-13,13)) # click Play!

    # wait for initializer
    startTime = time.time()
    while not pyautogui.locateOnScreen('initializer.png', confidence = .8): # wait for match
        print("Waiting for initializer " + str(round(time.time() - startTime,1)) + str(" seconds         "),end = '\r')
        if time.time() - startTime > 120: # two minutes to reset
            pyautogui.click(XY.CANCEL)
            pyautogui.click(XY.CANCEL) # cancel and try again
            startTime = time.time()

            time.sleep(.1)
            pyautogui.click(1400 + random.randint(-13,13), 880 + random.randint(-13,13)) # click Play!

    pyautogui.click(XY.CONFIRM[0] + random.randint(-13,13), XY.CONFIRM[1] + random.randint(-13,13))

    print("Beginning Battle                            ")

    i = 0

    while True: # main game loop

        print("Turn #%d                    " % (i+1))

        turnTime = time.time()

        while not pyautogui.locateOnScreen("EndTurn.png", confidence = .8):
            
            print("Waiting for turn          ", end = '\r') # status
            
            # pyautogui.click(1000,500) # click middle of screen
            if pyautogui.locateOnScreen("Green_End_Turn.png", confidence = .8):
                Done()
                break
            if pyautogui.locateOnScreen('Play.png', confidence = .8) or pyautogui.locateOnScreen('Okay.png', confidence = .8):
                return 1

        print("Playing Cards                ", end = '\r')
        playCards()
        
        print("Attacking                    ", end = '\r')
        attack()

        print("Ending Turn                  ", end = '\r')
        if pyautogui.locateOnScreen("Green_End_Turn.png", confidence = .8):
            Done()
        else:
            
            if time.time() - turnTime > 60: # 60 seconds max per turn
                Done()


        i += 1
        if i % 5:
            if pyautogui.locateOnScreen('Play.png', confidence = .8) or pyautogui.locateOnScreen('Okay.png', confidence = .8):
                # pyautogui.click(XY.OKAY)
                return 1


def main():

    time.sleep(2) # time to stop between games

    startTime = time.time()


    battles = 0

    while autoBattle():
        battles += 1
        print("\nBattle #" + str(battles) + " Complete                 ")
        print("Total hours elapsed: " + str((time.time()-startTime)/3600) + "\n")

    print("\nDone\n")

    print("Ran for a total of " + str((time.time()-startTime)/3600) + " hours.")
    print("Fought a total of " + str(battles) + "battles.")

    return 0

if __name__ == "__main__":
    main()