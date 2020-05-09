# adding records to new.db

import sqlite3

cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 2700000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 1500000)
    ]

with sqlite3.connect("new.db") as conn:
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO population VALUES (?,?,?)", cities)