import pyautogui as bot
import time 

time.sleep(2)
time.sleep(2)
while True:
    	if bot.pixel(35,232) == (75, 219, 106):
    		bot.click()
    		bot.sleep(2)