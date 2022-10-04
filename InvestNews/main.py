#!/usr/bin/env python3
import vietstock
import schedule
import time

# schedule.every().monday.tuesday.wednesday.thursday.friday.at(
#     "06:01").do(vietstock.enter_news())
# schedule.every().monday.tuesday.wednesday.thursday.friday.at(
#     "08:01").do(vietstock.filter(3))

# while 1:
#     schedule.run_pending()
#     time.sleep(1)

vietstock.check_time()
