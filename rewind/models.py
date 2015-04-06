__author__ = 'sunnyharris'
import sqlite3 as sql
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user, current_user
from rewind import app, login_manager

class User(UserMixin):
    def __init__(self, id, name, password, active=True):
        self.id = id
        self.name = name
        self.password = password
        self.active = active
        self.records = self.get_bought_records()

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_bought_records(self):
        userid = self.id
        with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
            cur = con.cursor()
            result = cur.execute("SELECT * FROM claimed_records WHERE userid=" + str(userid))
            return result.fetchall()

    @classmethod
    def get(self_class, user):
        with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
            cur = con.cursor()
            user1 = cur.execute("SELECT * FROM user_login WHERE user_name=?", (user,)).fetchone()
            return User(user1[0], user1[1], user1[2])


class UserNotFoundError(Exception):
    pass


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        user1 = cur.execute("SELECT * FROM user_login WHERE id=?", (id,)).fetchone()
    return User(user1[0], user1[1], user1[2])


def insert_user(user, password):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user_login(user_name, password) VALUES(?,?)", (user, password))

        # this is ugly and should use getter but i'm just trying to get it to work.
        user = cur.execute("SELECT * FROM user_login WHERE user_name=?", (user,)).fetchone()
        con.commit()
    return User(user[0], user[1], user[2])

def insert_record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go) VALUES (?,?,?,?,?,?,?,?,?,?)", (band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go))
        con.commit()


def select_record(record_id):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        result = cur.execute(''.join(("SELECT * FROM record WHERE id=", str(record_id))))
        return result.fetchall()


def get_shop_info():
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        result = cur.execute("SELECT band,record,price,current_buyers,max_buyers FROM record")
        return result.fetchall()


def buy_record(userid, band, record, record_cover, price, days_to_go):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO claimed_records(userid, band, record, record_cover, price, days_to_go ) VALUES(?,?,?,?,?,?)", (userid, band, record, record_cover, price, days_to_go))
        con.commit()


