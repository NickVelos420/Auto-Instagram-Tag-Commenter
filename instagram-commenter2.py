import pyautogui as pya
import string
import random
from functions.checkforError import checkIfCantComment
from time import sleep

commentInput = pya.locateOnScreen('images/comment.png', confidence=0.8)

# the center x and y value of the comment input 
commentLocation = pya.center(commentInput)

timesToGoDown = 1

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
    # this sleep is here because the error takes some ms to pop up
    sleep(1)
    # takes a screenshot of the screen to see if the error.png file is contained within it
    # the region will be different for you
    pya.screenshot('images/screen.png')
    # checks if instagram blocked you from commenting  
    checkIfCantComment("images/screen.png", "images/error.png")
    timesToGoDown += 1
    # this line is needed because when you post a comment it takes some time to load so it's based on your internet and it doesn't have to be that high you can change it
    sleep(3)
    
      
if commentInput != None:
  bot()