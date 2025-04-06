import pyautogui

x, y = 1755, 570

pyautogui.moveTo(x,y, duration=.001) # move to icon
pyautogui.click()
while pyautogui.pixel(x,y) != (75, 219, 106):
    pass
pyautogui.click()