from selenium import webdriver
from selenium.common.exceptions 		import TimeoutException
from selenium.webdriver.support.ui 		import WebDriverWait 
#from selenium.webdriver.support 		import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys 	import Keys
import time 


def logIn(driver, username, password, tryTime):
	
	#go to google page
	driver.get("https://www.instagram.com/accounts/login/?sourceurce=auth_switcher")

	
	#gets the input elements 
	val = False
	s   = time.time()
	while val == False:
		try:
			usernameInput = driver.find_element_by_xpath("//input[@name='username']")
			passwordInput = driver.find_element_by_xpath("//input[@name='password']")
			val           = True
			usernameInput.send_keys(username)
			passwordInput.send_keys(password)

			#submit the form
			passwordInput.submit()
			time.sleep(2)
		
		except:
			f = time.time()
			if f - s >= 30:
				break

#MUST LOG IN TO INSTA FIRST
def comment(username, password, driver, tryTime, subject, message, headless, dateDict):
	
	if headless == False:
		val = False
		while val == False:
			try:
				thing = driver.find_element_by_xpath("//div[@class='mt3GC']/button[1]")
				val = True
			except:
				print("fucking preferences")

		thing.click()
	
	#find users's home page
	val = False
	s   = time.time()
	while val == False:
		try:
			searchBar = driver.find_element_by_xpath("//div[@class='MWDvN ']/div[2]/input")
			val = True
		except:
			f = time.time()
			print('searchBar Issue')
			if f - s >= 30:
				break
	
	'''searchBar = driver.find_element_by_xpath("//div[@class='MWDvN ']/div[2]/input")
	time.sleep(tryTime)'''
	searchBar.send_keys(subject)
	
	#clicks on user result
	val = False
	s	= time.time()
	while val == False:
		try:
			res  = driver.find_element_by_xpath("//div[@class='z556c']")
			name = str(res.find_element_by_xpath("//div[@class='uyeeR']/span").text)
			print("the name i see is {}".format(name))
			
			if name.lower() == subject.lower():
				val = True
				print('User found')
				res.click()
			else:
				print("it should be {}".format(subject))
				this_is_an_intentional_error
		except:
			f = time.time()
			print("couldn't find user result")
			if f - s >= 30:
				break

	#Image shit is down here boiiiiiiiiiiiiiiiiiiiiiii - - - - - - - - - - - - - - - - - - -
	val = False
	s 	= time.time()
	time.sleep(3)
	while val == False:
		try:
			img = driver.find_elements_by_class_name("_bz0w")[0] #ISSUE IS HERE BOYO
			img.click()
			img.click()
			val = True
		except:
			f = time.time()
			print("couldn't get image")

			if f - s >= 30:
				break
				
	dOut = dateGet(driver)
	if dateCheck(dateDict, dOut, subject) == True:
		print("photo found")
	else:
		print('No new photo')
		return dateDict

	
	#comment on image
	val = False
	s 	= time.time()
	while val == False:
		try:
			commentBox = driver.find_element_by_xpath("//span[@class='_15y0l']/button[1]")
			val = True
		except:
			f = time.time()
			print("Can't find comment button")
			if f - s >= 30:
				break

	commentBox.click()
	
	val = False
	s 	= time.time()
	while val == False:
		try:
			commentForm = driver.find_element_by_xpath("//form[@class='X7cDz']/textarea")
			val = True
		except:	
			f = time.time()
			print("can't find comment input area")
			if f - s >= 30:
				break
	
	print('sending message')
	
	commentForm.send_keys(message[:len(message)])	

	#commentForm.send_keys(Keys.RETURN)
	commentForm.submit()
	print('submitted?')
	

	driver.quit()

	print("ended")
	return dateDict

def followerList(username, password, driver, tryTime, headless):
	
	# if options.headless == False:
	# 	val = False
	# 	while val == False:
	# 		try:
	# 			thing = driver.find_element_by_xpath("//div[@class='mt3GC']/button[1]")
	# 			val = True
	# 		except:
	# 			print("fucking preferences")

	# 	thing.click()

	#go to profile
	driver.get("https://www.instagram.com/{}/".format(username))

	#go to followers list
	fPath     = ("//a[@href='/{}/followers/']".format(username))
	followers = driver.find_element_by_xpath(fPath)
	followers.click()
	#time.sleep(tryTime*3)

	#get number of followers
	val = False
	while val == False:
		try:
			numF   = int(driver.find_element_by_xpath(fPath + "/span").get_attribute("title"))
			val = True
			print("numF is {}".format(numF))
		except:
			print("can't find how many followers you have")	

	#iterates over list of followers until (number of accounts) == numF
	val = False
	while val == False:
		try:
			fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
			val = True
		except:
			print("can't seem to find followers list")
	
	for i in range(3):
		driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + (arguments[0].offsetHeight /5);', fBody)
	time.sleep(tryTime)

	#Holy shit I need to comment here
	counter = 0
	numO    = 0
	while True:
		numC    = len(driver.find_elements_by_xpath("//div[@class='PZuss']/li"))
		if numC <= numF:	
			
			print(len(driver.find_elements_by_xpath("//div[@class='PZuss']/li")))
			driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + (arguments[0].offsetHeight);', fBody)
			counter == counter + 1
			if numO != numC:
				counter = 0
			else:
				if counter % 1000 == 0:
					driver.refresh()
					followerList(username, password, driver, tryTime, headless)
					return True

			numO = numC
			
			if len(driver.find_elements_by_xpath("//div[@class='PZuss']/li")) == numF:
				fElList  = driver.find_elements_by_xpath("//div[@class='PZuss']/li/div[1]/div[2]/div[1]")
				break
		
		elif numC >= numF:
			break

	fList    = []

	for el in fElList:
		fList.append(el.text)

	print("fElList len is {}".format(len(fElList)))
	print("numC is {}".format(numC))

	print(fList)
	print("ended")
	driver.quit()
	return True
	
def dateGet(driver): #must be on specific image to call

	val = False
	s 	= time.time()
	while val == False:
		try:
			timeTag  = driver.find_element_by_xpath("//a[@class='c-Yi7']/time")
			val = True
		
		except:
			f = time.time()
			print('yo when was this posted tho')
			if f - s >= 30:
				break				

	dT = str(timeTag.get_attribute("datetime"))
	
	t        = dT[-13:-1]
	hour 	 = int(t[:2])
	minute   = int(t[3:5])
	second   = int(t[6:8])

	d        = dT[:10]
	year     = int(d[:4])
	month    = int(d[5:7])
	day   	 = int(d[8:])

	dOut 	 = [year, month, day, hour, minute, second]
	
	print(d,t)
	print(" Hour {}\n Minute {}\n Second {}\n".format(hour, minute, second))
	print(dOut)
	return dOut

def dateCheck(dateDict, dOut, subject):
	if len(dateDict) == 0:
		dateDict[subject] = dOut
		return True
	else:
		for i in range(len(dOut)):
			if dOut[i] <= dateDict[subject][i]:
				return False
			elif dOut[i] > dateDict[subject][i]:
				dateDict[subject] = dOut
				return True
			else:
				pass
		return False


if __name__ == "__main__":

	username = "hahayeahbot"
	password = "123123123JK"
	tryTime  = 1
	subject  = "nastyfeminism"
	message  = "beep boop"
	headless = False
	dateDict = {}	
	
	#create driver instance and log in
	options = Options()  
	options.headless = False
	driver = webdriver.Firefox(options = options)

	logIn(driver, username, password, tryTime)

	comment(username, password, driver, tryTime, subject, message, headless, dateDict)
	print("\n\n\n")
	
