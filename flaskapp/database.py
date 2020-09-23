import sqlite3, csv

db = sqlite3.connect("data.db")

c = db.cursor()

def create_table():
    c.execute(""""CREATE TABLE chess_data
            first_name text,
            last_name text,
            win_percentage integer,
            loss_percentage integer,
            draw_percentage integer
    """)
    db.commit()

def insert_csv_data(filename):
    with open(filename + ".csv", "r") as file:
        counter = 0

        for i in file:
            cursor.execute("INSERT INTO chess_data (?,?,?,?,?)", row.split(","))
            db.commit()
            counter += 1

db.close()