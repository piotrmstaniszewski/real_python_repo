import sqlite3
from pathlib import Path
import csv

root_pth = Path("S:/python_venv/real_python_repo")
csv_pth = root_pth / "sql/employees.csv"
db_path = root_pth / "sql/new.db"

cities = [
('Boston', 'MA', 600000),
('Los Angeles', 'CA', 38000000),
('Houston', 'TX', 2100000),
('Philadelphia', 'PA', 1500000),
('San Antonio', 'TX', 1400000),
('San Diego', 'CA', 130000),
('Dallas', 'TX', 1200000),
('San Jose', 'CA', 900000),
('Jacksonville', 'FL', 800000),
('Indianapolis', 'IN', 800000),
('Austin', 'TX', 800000),
('Detroit', 'MI', 700000)
]

sql_dict = {
    "average": "SELECT avg(population) FROM population",
    "minimum": "SELECT min(population) FROM population",
    "maximum": "SELECT max(population) FROM population",
    "count": "SELECT count(population) FROM population",
    }

# with csv_pth.open(mode="r", encoding="utf-8") as f, sqlite3.connect(db_path) as conn:
with sqlite3.connect(db_path) as conn:
    c = conn.cursor()
    # c.execute("CREATE TABLE Employees ('FirstName' TEXT, 'LastName' TEXT)")
    try:
        # c.executemany("INSERT INTO population VALUES (?, ?, ?)", cities) # csv.reader(f)
        # rows = c.execute("UPDATE population SET population = 9000000 WHERE city = 'New York City' ")
        # print(rows)
        for key, value in sql_dict.items():
            c.execute(value)
            outpt = c.fetchone()[0]
            print(f"{key}: {outpt}")
    except sqlite3.OperationalError as err:
        print(f"Ooops, something went wrong - {err}")
    
