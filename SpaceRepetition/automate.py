#!/usr/bin/env python3

import schedule
import time
import repetition


def open_review():
    repetition.export()


schedule.every().day.at("05:00").do(open_review)
# schedule.every(1).minute.do(repetition.export)
# schedule.every(1).minute.do(open_review)

while True:
    schedule.run_pending()
    time.sleep(1)
