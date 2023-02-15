from datetime import datetime 
import datetime
from astral import LocationInfo
from astral.sun import sun
from astral.geocoder import database, lookup
import gspread

def timeline_1():
	info = lookup('Hanoi', database()) # print out Hanoi infomation
	city = LocationInfo('Hanoi', 'Viet Nam', 'Asia/Saigon', '21.083', '105.917')	
	c_data = sun(city.observer)
	# display +00:00 timezone => need add more 7 hours to +07:00 time zone
	sunrise = str(c_data['sunrise'])[11:16].split(':')
	sunrise = [int(x) for x in sunrise]
	sunrise[0] += 7 - 24 

	sunset = str(c_data['sunset'])[11:16].split(":")
	sunset = list(map(int, sunset))
	sunset[0] += 7
	print(sunrise)
	print(sunset)

def timeline_2():
	city = LocationInfo('Hanoi', 'Viet Nam', 'Asia/Saigon', '21.083', '105.917')	
	c_data = sun(city.observer)
	
	sunrise = str(c_data['sunrise'])[11:16].split(':')
	sunset = str(c_data['sunset'])[11:16].split(':')

	sunrise = list(map(int, sunrise))
	sunset = list(map(int, sunset))

	# display +00:00 timezone => need add more 7 hours to +07:00 time zone
	sunrise[0] += 7 - 24
	sunset[0] += 7
	# Hanoi's dusk time later than Hue
	sunset[1] = abs(sunset[1] - 25)

	# assign time sunset vs sunrise
	now = datetime.datetime.now()
	sunrise = datetime.datetime(now.year, now.month, now.day, sunrise[0], sunrise[1])
	sunset = datetime.datetime(now.year, now.month, now.day, sunset[0], sunset[1])

	return sunrise, sunset


if __name__ == '__main__':
	# timeline_1()

	# Getting current date and time
	pass


