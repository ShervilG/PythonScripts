import pyautogui as bot
import time
import keyboard

times = 50

string = ":-)"
time.sleep(3)

for i in range(1,times+1):
	#if keyboard.read_key() == 'f1':
		#:-)break
	x = string*i
	bot.typewrite(x)
	bot.press('enter')
	time.sleep(0.6)