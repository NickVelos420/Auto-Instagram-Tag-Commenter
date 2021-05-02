import cv2
import numpy as np
import pyautogui as pya
from time import sleep

commentInput = pya.locateOnScreen('images/comment.png', confidence=0.8)

# the center x and y value of the comment input 
commentLocation = pya.center(commentInput)

def checkIfCantComment(template, small):
  global commentLocation
  img1 = cv2.imread(template)
  img2 = cv2.imread(small)

  img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  res = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)
  if np.any(res > .83):
      print("error found")
      sleep(1 * 60)
      pya.click(commentLocation)
      pya.hotkey("ctrl", "a")
      pya.press("delete")
  else:
    print ("Not found")

