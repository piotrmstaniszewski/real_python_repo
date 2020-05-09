import sqlite3
from pathlib import Path
import csv

root_pth = Path("S:/python_venv/real_python_repo")
csv_pth = root_pth / "sql/employees.csv"
db_path = root_pth / "sql/new.db"

with csv_pth.open(mode="r", encoding="utf-8") as f, sqlite3.connect(db_path) as conn:
    c = conn.cursor()
    # c.execute("CREATE TABLE Employees ('FirstName' TEXT, 'LastName' TEXT)")
    try:
        c.executemany("INSERT INTO Employees VALUES (?, ?)", csv.reader(f))
    except sqlite3.OperationalError as err:
        print(f"Ooops, something went wrong - {err}")
    
