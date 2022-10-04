#!/usr/bin/env sh
#!/system/bin/sh

# shell=""
shell="adb shell"
tap="${shell} input touchscreen tap"
swipe="${shell} input touchscreen swipe"
text="${shell} input text"
key="${shell} input keyevent"

# checkNotification() {
# 	# if true 
# 	while [[ true ]]; do
# 		#statements
# 		$text 1000
# 		sleep 0.5
# 		$tap x y	
# 		sleep 0.5
# 		$text C2 || L2
# 		sleep 0.5
# 		$tap x y
# 		sleep 5
# 		if [[ win ]]; then
# 			wait for notification;
# 		fi 
# 	done


# 	$text 2000
# 	$text 4000
# 	$text 8000
# 	$text 16000
# 	$text 33000
# 	$text 68000
# }
# estimate time: 25s
moveCash() {
	# click more cash move
	$tap 170 1216
	sleep 1

	# input cash
	$text ${1}00
	# sleep 0.25

	# input message
	$tap 360 435
	# sleep 0.25
	$text ${2}
	# sleep 0.25

	# click chuyen tien
	$tap 360 680
	sleep 9
	# click xac nhan
	$tap 360 1225
	sleep 1
	# # click skip
	# $tap 360 760
	# sleep 0.5

	# input password: 6s
	$tap 135 866
	$tap 135 985
	$tap 135 1100
	$tap 360 980
	$tap 590 866
	$tap 590 980

	# xem kq
	sleep 10
	$tap 360 750
}

moveCash 1 C2

# Check momo bill's number % 2 == 0 or not

# if win -> start over with 1000 and the same code
# if lose -> start double * previous money and the same code


# if lost more than 133.000 stop the script and notify

# check if the number closer to 140 or not each 5 min
# if amount of number left is >140 stop the script and notify