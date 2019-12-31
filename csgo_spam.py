import keyboard
import pyautogui as bot
import random
import time

lis = ["Im a hacker !","Lol Noobs !","Cant touch dis :P","Hopeless is walling !!!!","Just aimware.exe !!!!"]

while True:
	if keyboard.read_key() == 'f1':
		exit()
	if keyboard.read_key() == 'y':
		ind = random.randint(0,len(lis)-1)
		bot.typewrite(lis[ind])
		bot.press('return')