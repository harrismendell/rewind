__author__ = 'sunnyharris'
import sqlite3 as sql


def insert_record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go) VALUES (?,?,?,?,?,?,?,?,?,?)", (band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go))
        con.commit()

def select_record(record_id):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute(''.join(("SELECT * FROM record WHERE id=", str(record_id))))
        return result.fetchall()