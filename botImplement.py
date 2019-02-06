import time 
import selPractice   as hehe

pTime = time.time()

username = "hahayeahbot"
password = "123123123JK"
tryTime  = 10
subjects  = ["nastyfeminism"]
message  = "Hi there.\nThis is just a quick reminder that though political accounts are valuable, they also frequently generalize and exaggerate to further enflame their followers. This causes beliefs on all sides to flare, leading to further divisiveness and further entrapping people in their political bubbles. Keep this in mind when scrolling, and perhaps take a moment to check accounts of the opposite position - if not to simply see their views on things. It probably won’t change your mind, but it will help you step outside of your political bubble and see things through somebody else’s eyes."
headless = True
dateDict = {}

dateDict = hehe.comment(username, password, tryTime, subject, message, headless, dateDict)

while True:
	cTime = time.time()
	if (cTime - pTime) % (60*5) == 0 :
		for subject in subjects:
			dateDict = hehe.comment(username, password, tryTime, subject, message, headless, dateDict)