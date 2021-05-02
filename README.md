# THE BOT FULLY WORKS. BUT THERE ARE SOME THINGS THAT I WANT TO MAKE SOME SLIGHT CHANGES AND ADD SOME FEATURES.

## This bot can help you with commenting on giveaways.

#### The bot will not work if you haven't downloaded the modules that I'm using. To download it you'll need to have python and pip installed

<table>
  <caption>The Modules</caption>
  <tr>
    <th>
      name
    </th>
    <th>
      command
    </th>
  </tr>
  <tr>
    <td>pyautogui</td>
    <td>pip install pyautogui</td>
  </tr>
  <tr>
    <td>numpy</td>
    <td>pip install numpy</td>
  </tr>
  <tr>
    <td>cv2</td>
    <td>pip install opencv-python</td>
  </tr>
</table>

#### That should do it.

### If you are still getting an error you're probably using the dark theme of instagram or the input placeholder does not appear. To fix the first error (the dark theme) you should just take a screenshot of the input and it must have the emoji button in it just like the comment.png file, now when you have taken the screenshot you put it in the folder of the python script and replace the followings line first parameter

###### the line to replace:

```py
commentInput = pya.locateOnScreen('comment.png', confidence=0.8)
```

<br />

### If you're still getting an error it's probably a problem with instagrams input placeholder to fix this just restart the page and click on the image until the placeholder text shows "Add a comment". Also the input shouldn't have text in it.

<br />
<br />

#### To change the amount of tags you have in a comment you just have to change the number in the following for loop:

```py
for j in range(3):
```
