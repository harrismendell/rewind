__author__ = 'sunnyharris'
import sqlite3 as sql
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user
from rewind import app, login_manager

class User(UserMixin):
    def __init__(self, id, name, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @classmethod
    def get(self_class, user):
        with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
            cur = con.cursor()
            user1 = cur.execute("SELECT * FROM user_login WHERE user_name=?", (user,)).fetchall()
            import ipdb; ipdb.set_trace()
            return User(user1[0][0], user1[0][1])


class UserNotFoundError(Exception):
    pass


# Flask-Login use this to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        user1 = cur.execute("SELECT * FROM user_login WHERE id =" + id).fetchall()
    return User(user1[0][0], user1[0][1])


def insert_user(user, password):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user_login(user_name, password) VALUES(?,?)", (user, password))
        con.commit()
    return User.get(user)

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