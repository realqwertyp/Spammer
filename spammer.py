import pyautogui, time

time.sleep(10) ##starts 5 seconds after running

spamText = open("spam.txt", "r") ##spam.txt is the text you are using to spam

for line in spamText:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
