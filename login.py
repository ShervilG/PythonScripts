from tkinter import *
import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

#global stuff
options = Options()
options.add_argument("--headless")
flag = 0
url = "https://172.31.1.6:8090/httpclient.html"
driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\Program Files (x86)\\geckodriver.exe")
driver.get(url)
name = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")	
bb = driver.find_element_by_id("loginbutton")

top = Tk()
top.title("Coz sophos is too mainstream !")
btext = tk.StringVar()
top.geometry("330x150")
t1 = Entry(top,bd = 2,width = 40)
t1.place(x=40,y=0)
t2 = Entry(top,bd = 2,width = 40)
t2.place(x=40,y=40)
def login():
	global flag,btext,driver,name,password,bb,t1,t2
	if (t1.get()!="" and t2.get()!= ""):
		r = str(t1.get()).strip()
		p = str(t2.get()).strip()
		if flag==0:
			name.send_keys(r)
			password.send_keys(p)
			password.send_keys(Keys.RETURN)
			try:
				is_in = driver.find_element_by_id("signin-caption")
				ass = "You are signed in as {}".format(r)
				time.sleep(3)
				if is_in.get_attribute('innerHTML') == ass: 
					st = "Log-out !"
					btext.set(st)
					flag = 1
				else:
					name.send_keys("")
					password.send_keys("")
					st = "Login failed !"
					btext.set(st)	
			except:
				print("lol !")
		else:
			bb.click()
			time.sleep(3)
			name.send_keys("")
			password.send_keys("")
			btext.set("Login !")
			flag = 0
b = Button(top,bd = 2,width = 20,textvariable = btext,command = login).place(x=80,y=80)
btext.set("Login !")

top.mainloop()
driver.quit()