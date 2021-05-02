import cv2
import numpy as np
from time import sleep

def checkIfCantComment(template, small):
  img1 = cv2.imread(template)
  img2 = cv2.imread(small)

  img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  res = cv2.matchTemplate(img1_gray, img2_gray, cv2.TM_CCOEFF_NORMED)
  if np.any(res > .9):
      print("error found")
      sleep(4)
  else:
    return "Not found"

