import datetime, time, webbrowser, sys
import itertools
import threading

def checkMail(url, timeline, duration):
    # secToNow = setNowTime()
    now = datetime.datetime.now()
    timeStart = []
    timeEnd = []
    for i in range(len(timeline)):
        timeStart.append(datetime.datetime(now.year, now.month, now.day, timeline[i][0], timeline[i][1], timeline[i][2]))
        timeEnd.append(datetime.datetime(now.year, now.month, now.day, timeline[i][0], timeline[i][1]+duration, timeline[i][2]))

    for i in range(len(timeStart)):
        if i==len(timeStart)-1:
            if now>=timeStart[i] and now<timeEnd[i]:
                webbrowser.open(url)
                t_sleep = (timeStart[0] - timeEnd[i]).total_seconds() 
                time.sleep(t_sleep)
                break

        if now>=timeStart[i] and now<timeEnd[i]:
            webbrowser.open(url)
            t_sleep = (timeStart[i+1] - timeEnd[i]).total_seconds() 
            time.sleep(t_sleep)

try:
    url = 'https://mail.google.com/mail/u/0/h/1p1nogfydjb1p/?zy=e&f=1'
    # timeline should not: thoi diem chuyen sang tieng moi vd 7:45, hay 8:50 -> hard to code
    timeline = [
        (7, 0, 0),
        (13, 10, 0),
        (19, 30, 0),
    ]
    durationTime = 15 # in 15 mins
    
    # th = threading.Thread(target=runningStatus)
    # th.start()

    while True:
        print('Running\n') 
        checkMail(url, timeline, durationTime)
except KeyboardInterrupt:
    sys.stdout.write('\r!!! Done !!!')
    is_done = True
    time.sleep(0.5)
