from selenium  							import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import commentBot   					as bot

pTime 	 = time.time() 	#starting time

interv	 = 5 #minutes

username = "politicalreminderbot"
password = "123123123JK"
tryTime  = 10
subjects = ["nastyfeminism", "republican.s", "republicanparty", "localdemocrazy", "occupydemocrats"]
headless = False										#changes script processes (doesn't actually now lol)
message  = "."#open("message.txt").read()
dateDict = {}
duration = 3 #days

for sub in subjects:
	dateDict[sub] = {}
	

#create driver instance and log in
options 		 = Options()
options.headless = headless							#changes driver processes
driver 			 = webdriver.Firefox(options = options)

bot.logIn(driver, username, password, tryTime)

for subject in subjects:
	dateDict = bot.comment(username, password, driver, tryTime, subject, message, headless, dateDict)
	driver.get("https://www.instagram.com/")

cTime = time.time()
while cTime - pTime <= 60*60*60*24*duration:
	try:
		cTime = time.time()
		if (cTime - pTime) % (60*interv) == 0:
			for subject in subjects:
				dateDict = bot.comment(username, password, driver, tryTime, subject, message, headless, dateDict)
				driver.get("https://www.instagram.com/")
	except:
		driver.quit()
