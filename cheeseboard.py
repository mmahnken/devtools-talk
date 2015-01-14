import requests
from BeautifulSoup import BeautifulSoup
import datetime


extra = ''
weekday = datetime.datetime.now().strftime("%A")
if weekday == 'Monday':
	weekday = 'Tuesday'
	extra = 'For tomorrow,'

blob = requests.get('http://www.cheeseboardcollective.coop/pizza')
soup = BeautifulSoup(blob.text)

section = soup.findAll(['h4', 'p'])

def pizza():
	for item in section:
		if item.text[0:2] == weekday[0:2]:
			phrase = "%s's Cheeseboard\n%s" % (item.text, section[section.index(item)+1].text)		
			print phrase
			return

pizza()
