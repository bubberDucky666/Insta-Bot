from selenium  							import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import commentBot   					as bot

pTime 	 = time.time() 	#starting time

interv	 = 5 #minutes

username = "politicalreminderbot"
password = "123123123JK"
tryTime  = 10
subjects = ["nastyfeminism", "quality._.equality"]
headless = False										#changes script processes
dateDict = {}
message  = open("message.txt").read()

#create driver instance and log in
options = Options()
options.headless = headless							#changes driver processes
driver = webdriver.Firefox(options = options)

bot.logIn(driver, username, password, tryTime)

while True:

	cTime = time.time()
	if (cTime - pTime) % (60*interv) == 0 :
		for subject in subjects:
			dateDict = bot.comment(username, password, driver, tryTime, subject, message, headless, dateDict)
