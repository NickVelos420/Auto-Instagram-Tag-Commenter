import pyautogui as pya
import string
import random
import keyboard as kb
from time import sleep

commentInput = pya.locateOnScreen('comment.png', confidence=0.8)

# the center x and y value of the comment input 
commentLocation = pya.center(commentInput)

timesToGoDown = 1

# The instagram algorithm stopes you from commenting after a bit so we have to if it has blocked us
# when it stopes you it pops up a message so we this function just searches the sreen for that after 
# it hit the enter button

def checkIfCantComment():
  checksForError = pya.locateOnScreen("error.png", confidence=0.5)
  if checksForError != None:
    sleep(4 * 60)
  else: 
    return

def bot(): 
  global timesToGoDown 
  while True:
    # clicks the input
    pya.click(commentLocation)
    for j in range(3):
      # writes a random letter
      pya.typewrite("@"+random.choice(string.ascii_letters))
      # waits for the suggestions to load
      sleep(1.5)
      # presses the down button so the users are random
      pya.press("down", presses=timesToGoDown)
      # presses enter so it writes the whole name
      pya.press("enter")
    pya.click(commentLocation)
    pya.press("enter")
    # checks if instagram blocked you from commenting  
    checkIfCantComment()
    timesToGoDown += 1
    # this line is needed because when you post a comment it takes some time to load so it's based on your internet and it doesn't have to be that high you can change it
    sleep(3)
    
      
if commentInput != None:
  bot()