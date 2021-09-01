from astral import LocationInfo
from astral.sun import sun
from astral.geocoder import database, lookup
from icecream import ic

def timeline():
	info = lookup('Hanoi', database()) # print out Hanoi infomation
	# city = LocationInfo(name, region, timezone, latitude, longtitude)
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
	# print('dawn: ' + str(c_data["dawn"]))
	# print('dusk: ' + str(c_data["dusk"]))


if __name__ == '__main__':
	timeline()
