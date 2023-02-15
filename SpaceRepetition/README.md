# Requirements

- Create 1 table:scheduler in SQLite
  - Saved subject_name, today, time1, time2, ....
  - ? Saved insert || sql update after insert

```sql
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
```

- export to txt file: today_review.md, daily and then open it


## Have GUI to add new subject 
- PyQT or Web
- The review report can be viewed on web

# How to use

run by command line:
```commandline
learn.py xich tam tuan thien
```


# Exception:

1. 

