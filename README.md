# This bot can help you with commenting on giveaways.

#### The bot will not work if you haven't downloaded the modules that I'm using. To download them you need to have python and pip installed

<table>
  <caption>The Modules</caption>
  <tr>
    <td>pyautogui</td>
    <td>pip install pyautogui</td>
  </tr>
  <tr>
    <td>pyperclip</td>
    <td>pip install pyperclip</td>
  </tr>
</table>
#### That should do it.

### If you are getting an error you're probably using the dark theme of instagram or the input placeholder does not appear. To fix the first error (the dark theme) you should just take a screenshot of the input and it must have the emoji button in it just like the comment.png file, now when you have taken the screenshot you put it in the folder of the python script and replace the seventh line with the name of the screenshot you just took. Now if this error pops up again

error:

```
"inputX": commentInput[0] + 100,
TypeError: 'NoneType' object is not subscriptable
```

### it's probably a problem with instagrams input placeholder to fix this just restart the page and click on the image until the placeholder text shows "Add a comment". Also the input shouldn't have text in it.
