#!/usr/bin/env python3
import itertools
import threading
import time
import sys

is_done = False
#here is the animation
def animate():
	# itertools.cycle -> infinity loop cycle 
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if is_done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    # \r : write new đè lên old  
    sys.stdout.write('\rDone!     ')

try:
	is_done = False
	# still run function() when time.sleep() active
	# t = threading.Thread(target=animate(is_done))
	# t.start()

	while True:
		animate()
except KeyboardInterrupt:
	#long process here
	is_done = True
	print('Done')
