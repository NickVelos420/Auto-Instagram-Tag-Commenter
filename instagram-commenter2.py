# check if the code works 
# everything is suppose to be working correctly but i don't know

import pyautogui as pya
import pyperclip
import string
import random
from time import sleep

commentInput = pya.locateOnScreen('comment.png', confidence=0.8)

locations = {
  "inputX": commentInput[0] + 100,
  "inputY": commentInput[1] + 30
}

fileManage = {
  "allUsersRead": open("users-written.txt", "r").read(),
  "allUsersWrite": open("users-written.txt", "w"),
  "currentUserRead": open("current-tags.txt", "r").read(),
  "currentUsersWrite": open("current-tags.txt", "w"),
  "currentUsersDelete": open("current-tags.txt", "r+").truncate(0)
}


timesToGoDown = 1
firstTime = True
filesContent = {}

# def copyInput():
#   # moves the mouse to the comment input
#   pya.click(locations["inputX"], locations["inputY"])
#   # highlights everything
#   pya.hotkey("ctrl", "a")
#   # copies everything
#   pya.hotkey("ctrl", "c")
#   fileManage["allUsersWrite"].write(pyperclip.paste())
#   fileManage["currentUsersWrite"].write(pyperclip.paste())
#   if firstTime == True:
#     return
#   else:
#     filesContent["allUsers"] = fileManage["allUsersRead"].split()
#     filesContent["currentUsers"] = fileManage["currentUsersRead"].split()
#     for i in filesContent["allUsers"]:
#       for j in filesContent["currentUsers"]:
#         if j == i:
#           pya.click(locations["inputX"], locations["inputY"])          
#           pya.hotkey("ctrl", "a")
#           pya.press("delete")
#           fileManage["currentUsersDelete"]
#           return

# def checkIfCantComment(fileName):
#   checksForError = pya.locateOnScreen(fileName, confidence=0.85)
#   if checksForError != None:
#     sleep(4 * 60)
#   else: 
#     return

def bot(): 
  global timesToGoDown 

  for i in range(2):
    if i > 0:
      firstTime = False
    # clicks the input
    pya.click(locations["inputX"], locations["inputY"])
    for j in range(3):
      # writes a random letter
      pya.typewrite("@"+random.choice(string.ascii_letters))
      # waits for the suggestions to load
      sleep(0.95)
      # presses the down button so the users are random
      pya.press("down", presses=timesToGoDown)
      # presses enter so it writes the whole name
      pya.press("enter")
    # pya.click(locations["inputX"], locations["inputY"])
    # copyInput()
    # checkIfCantComment("error.png")
    # pya.click(locations["inputX"], locations["inputY"])
    # pya.press("enter")
    # checks if an error  
    # checkIfCantComment("error.png")
    # timesToGoDown += 1
    
      
if commentInput != None:
  bot()