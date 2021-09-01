import time 

now = time.time()
# The time() function returns the number of seconds passed since epoch.
# For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
print(now)

print(time.ctime(now)) # -> Fri Mar 26 20:02:19 2021

# stopwatch.py - A simple stopwatch program.

# Display the program's instructions.
print('''Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.
Press Ctrl-C to quit.''')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
# TODO: Start tracking the lap times.

# Start tracking the lap times.
try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
		lapNum += 1
		lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
	# Handle the Ctrl-C exception to keep its error message from displaying.
	print('\nDone.')












