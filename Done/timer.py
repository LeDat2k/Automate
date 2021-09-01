import time, sys, datetime, subprocess
import winsound
import ctypes  # An included library with Python install.   
import threading
# find the second before the time
def secondBefore(h, m, s):
	s-=1
	if s<0:
		s=59
		m-=1
		if m<0:
			m=59
			h-=1
			if h<0:
				return 0, 0, 0

	return h, m, s

# make a countdown digital clock
def clockCountdown(h, m, s):
	while h!=0 or m!=0 or s!=0:
		h, m, s = secondBefore(h, m, s)
		sys.stdout.write('\r{}:{}:{}    '.format(h, m, s))
		time.sleep(1)
			
# open Dialog when timer done
def notify():
	winsound.PlaySound('*', winsound.SND_ALIAS)
	# subprocess.Popen(['start', 'alarm.wav'], shell=True)

	# dialog
	text = 'Timer count down done!'
	title = 'Dialog'
	style = 1
	ctypes.windll.user32.MessageBoxW(0, text, title, style)

def countdown(hours, minutes, seconds):
	delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
	
	time.sleep(delta.total_seconds())

	notify()

def timeHasSet():
	while True:
		print('''1. 5 min''')
		print('''2. 25 min''')
		option = input()
		if option == '1':
			countdown(0, 5, 0)
			break
		elif option =='2':
			countdown(0, 25, 0)
			break
		else:
			print('Wrong input! \n Enter again!')

def setTime():
	while True:
		print("Set timer! ( h:m:s || m:s || s )")

		time = str(input())
		time = time.split(':')	
		time = [int(x) for x in time]

		is_InputWrong = False
		for t in time:
			if t<0 or t>60:
				is_InputWrong = True
				break
		if is_InputWrong:
			print('Input must less than 60 and greater than 0! Input again!')
			continue
		
		if len(time)==3:
			# countdown(time[0], time[1], time[2])
			clockCountdown(time[0], time[1], time[2])
			notify()
			break
		elif len(time)==2:
			# countdown(0, time[0], time[1]) 
			clockCountdown(0, time[0], time[1])
			notify()
			break
		elif len(time)==1:
			# countdown(0, 0, time[0])
			clockCountdown(0, 0, time[0])
			notify()
			break
		else:
			print('Wrong input! \n Enter again!')


def main():
	while True:
		print('''**** Timer ****
		1.Set old timer
		2.Set your new timer
		q.Quit	''')
		ch = input()

		if ch == '1':
			timeHasSet()
		elif ch == '2':
			setTime()
		elif ch == 'q':
			print('Quit')
			break
		else:
			print('Wrong input!\nEnter again!')
try:
	main()
except KeyboardInterrupt:
	print()



		
	
	





