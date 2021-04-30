# THE BOT IS STILL IN PRODUCTION AND I DON'T KNOW IF IT WORKS PROPERLY

## This bot can help you with commenting on giveaways.

#### The bot will not work if you haven't downloaded the module that I'm using. To download it you'll need to have python and pip installed

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
</table>

#### That should do it.

### If you are still getting an error you're probably using the dark theme of instagram or the input placeholder does not appear. To fix the first error (the dark theme) you should just take a screenshot of the input and it must have the emoji button in it just like the comment.png file, now when you have taken the screenshot you put it in the folder of the python script and replace the followings line first parameter

###### the line to replace:

```py
commentInput = pya.locateOnScreen('comment.png', confidence=0.8)
```

### with the name of the screenshot you just took. Now if this error pops up again

###### error:

```
"inputX": commentInput[0] + 100,
TypeError: 'NoneType' object is not subscriptable
```

### it's probably a problem with instagrams input placeholder to fix this just restart the page and click on the image until the placeholder text shows "Add a comment". Also the input shouldn't have text in it.

<br />
<br />

#### To stop the script from running just press the escape key until you see that the script has stopped. If you want to chat the key that stopes the script you can just change the "esc" in the following line

```py
while kb.is_pressed("esc") == False
```

<br />

#### To change the amount of tags you have in a comment you just have to change the number in the following for loop:

```py
for j in range(3):
```
