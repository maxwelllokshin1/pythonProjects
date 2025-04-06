import pyautogui


x,y = 1578, 987

pyautogui.moveTo(x,y, duration=1)

while pyautogui.pixel(x,y) != (255, 255, 0):
    print(pyautogui.pixel(x,y))
    pyautogui.click()