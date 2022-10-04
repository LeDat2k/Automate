CREATE TABLE IF NOT EXISTS scheduler (
    subject_name TEXT NOT NULL,
    learned_date TEXT NOT NULL,
    time1 TEXT,
    time2 TEXT,
    time3 TEXT,
    time4 TEXT,
    time5 TEXT,
    time6 TEXT,
    time7 TEXT,
    time8 TEXT
);


-- INSERT INTO
--     scheduler(
--         subject_name,
--         learned_date,
--     )
-- VALUES
--     (
--         "Bash basic",
--         '2022-09-25'
--     );

-- INSERT INTO
--     scheduler (subject_name, learned_date)
-- VALUES
--     ("subject 5", '2022-09-25');

-- INSERT INTO
--     scheduler (subject_name, learned_date)
-- VALUES
--     ("subject 4", '2022-09-23');


-- ALTER TABLE scheduler RENAME COLUMN tim4 TO time4;


-- UPDATE scheduler
-- SET time1 = DATE(JULIANDAY(learned_date)+1)
-- WHERE time1 is NULL;


-- SELECT * FROM scheduler WHERE rowid = '4';

-- SELECT
--     DISTINCT subject_name
-- FROM
--     scheduler
-- WHERE
--     DATE() = scheduler.time1
--     OR (DATE() = scheduler.time2)
--     OR (DATE() = scheduler.time3)
--     OR (DATE() = scheduler.time4)
--     OR (DATE() = scheduler.time5)
--     OR (DATE() = scheduler.time6)
--     OR (DATE() = scheduler.time7)
--     OR (DATE() = scheduler.time8);


-- DELETE FROM scheduler WHERE rowid='6';

-- rowid autoincrements
-- DROP TABLE scheduler;


