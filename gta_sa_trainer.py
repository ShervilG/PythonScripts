import pyautogui as cheat
import keyboard 
import time

#activate the trainer
while True:
	if keyboard.read_key() == "f1":
		time.sleep(1.5)
		while True:
			if keyboard.read_key() == "f2":
				bot.typewrite("hesoyam")
			if keyboard.read_key() == "f3":
				bot.typewrite("fullclip")
			if keyboard.read_key() == "f4":
				bot.typewrite("aezakmi")
			if keyboard.read_key() == "f1":
				exit()
