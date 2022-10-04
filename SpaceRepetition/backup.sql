PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE scheduler (
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
INSERT INTO scheduler VALUES('Trach nhat phi thang','2022-10-04','2022-10-05','2022-10-08','2022-10-11','2022-10-20','2022-11-05','2022-12-07','2023-02-09','2023-06-17');
COMMIT;
