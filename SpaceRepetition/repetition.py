#!/usr/bin/env python3
from datetime import date
import math
import os
import sqlite3
from sys import argv

DB_PATH = r'/media/dat/DISK/Dev/Automation/SpaceRepetition/repetition.db'


def submit():
    conn = sqlite3.connect(DB_PATH)

    repetition_rule = {
        "time1": math.pow(2, 0),
        "time2": math.pow(2, 2),
        "time3": 7,
        "time4": 16,
        "time5": 32,
        "time6": 64,
        "time7": 128,
        "time8": 256,
    }
    # create cursor
    c = conn.cursor()

    # Saved new thing
    if (len(argv) == 1):
        print("Nothing to saved!")
        return

    learned_subject = ' '.join(argv[1:])
    # print(argv[1])
    # print(' '.join(argv[1:]))
    today = date.today()

    c.execute("""
    INSERT INTO
        scheduler (subject_name, learned_date)
    VALUES
        (?, ?);
    """, (str(learned_subject), str(today), ))

    for index in range(1, 9, 1):
        c.execute(f"""
        UPDATE scheduler
        SET time{index} = DATE(JULIANDAY(learned_date)+{repetition_rule[f'time{index}']})
        WHERE time{index} is NULL; 
        """)

    conn.commit()
    conn.close()


def export():
    review_file = 'today_review.md'

    conn = sqlite3.connect(DB_PATH)

    # create cursor
    c = conn.cursor()

    c.execute("""
    SELECT
        DISTINCT subject_name
    FROM
        scheduler
    WHERE
        DATE() = scheduler.time1
        OR (DATE() = scheduler.time2)
        OR (DATE() = scheduler.time3)
        OR (DATE() = scheduler.time4)
        OR (DATE() = scheduler.time5)
        OR (DATE() = scheduler.time6)
        OR (DATE() = scheduler.time7)
        OR (DATE() = scheduler.time8);
    """)
    items = c.fetchall()

    with open(review_file, 'w') as file:
        now = str(date.today())
        file.write(now+'\n')
        for item in items:
            file.write('- [ ] '+str(item)[2:-3]+'\n')

    # open report file
    report_file = os.path.join(os.path.dirname(__file__), review_file)
    os.system(f'subl {report_file}')

    conn.commit()
    conn.close()


# submit()

# export()
