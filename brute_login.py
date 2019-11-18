import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://172.31.1.6:8090/httpclient.html"
driver = webdriver.Firefox()
print("Opening login page !")
time.sleep(3)
driver.get(url)
roll = ["101603312","101615041","101615049","placement"]
password = ["sheron","shinchan12","5049","cilp@19"]
i = 0

while i<len(roll):
	time.sleep(2)
	r = roll[i]
	p = password[i]
	t1 = driver.find_element_by_id("username")
	t2 = driver.find_element_by_id("password")
	t1.send_keys(r)
	t2.send_keys(p)
	t2.send_keys(Keys.RETURN)
	time.sleep(3)
	try:
		is_in = driver.find_element_by_id("signin-caption")
		ass = "You are signed in as {}".format(r)
		time.sleep(3)
		if is_in.get_attribute('innerHTML') == ass: 
			st = "Logged in for {}".format(r)
			print (st)
			break
		else:
			st = "Login failed for : {}".format(r)
			print (st)
			driver.refresh()
			i += 1	
	except:
		st = "Login failed for : {}".format(r)
		print (st)
		driver.refresh()
		i += 1





