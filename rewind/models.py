__author__ = 'sunnyharris'
import sqlite3 as sql
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
from rewind import app, login_manager

class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
            cur = con.cursor()
            self.active = cur.execute("SELECT is_authenticated FROM user_login WHERE user_name =" + self.name)
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        pass

    def get(self, user):
        with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
            cur = con.cursor()
            u = cur.execute("SELECT is_authenticated FROM user_login WHERE user_name =" + user)
            return User(u.name, u.id, u.active)


class UserNotFoundError(Exception):
    pass


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        u = cur.execute("SELECT * FROM user_login WHERE id =" + id)
    return User(u.name, u.id, u.active)


def insert_user(user_name, password):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user_login(user_name, password) VALUES(?,?)", (user_name, password))
        con.commit()
    return User.get(user_name)

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