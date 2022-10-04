#! python3
import datetime, time

now = datetime.datetime.now()
date_born = datetime.datetime(2000, 6, 25, 0, 0, 0)

now.year, now.month, now.day, now.hour, now.minute, now.second
datetime.datetime.fromtimestamp(time.time())

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
# (11, 36548, 0)
delta.total_seconds()
# 986948.0
str(delta)
# '11 days, 10:09:08'

# ------------------------------------------------------------
# pausing program
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
	time.sleep(1)
	# The time.sleep(1) call will pause your Python program so that the
	# computer doesn’t waste CPU processing cycles simply checking the time
	# over and over. 

# ------------------------------------------------------------
# convert datetime datatype -> string
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')
# '04:29 PM'
oct21st.strftime("%B of '%y")
# "October of '15"

# ------------------------------------------------------------
#convert string -> datetimetype
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
# datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
# datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of '%y")
# datetime.datetime(2015, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")
# datetime.datetime(2063, 11, 1, 0, 0)
