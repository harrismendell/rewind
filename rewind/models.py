__author__ = 'sunnyharris'
import sqlite3 as sql


def insert_record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go) VALUES (?,?,?,?,?,?,?,?,?,?)", (band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go))
    con.commit()
    con.close()


def select_record(params=()):
    con = sql.connect("database.db")
    cur = con.cursor()
    if params==():
        cur.execute("select * from record")
    else:
        string = "select"
        for i in xrange(len(params)-1):
            string += "%s,"
        string += "%s"
        string += " from record"
        result = cur.execute(string)
        con.close()
        return result.fetchall()