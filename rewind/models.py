__author__ = 'sunnyharris'
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user, current_user
from rewind import app, login_manager
import json


class User(UserMixin):

    def __init__(self, name, password, active=True):
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
            result = cur.execute(
                "SELECT * FROM claimed_records WHERE userid=" + str(userid))
            return result.fetchall()

    @classmethod
    def get(self_class, user):
        with open('rewind/users.json') as f:
            my_dict = json.load(f)
            user = my_dict['users'][name]


class UserNotFoundError(Exception):
    pass


# Flask-Login use this to reload the user object from the user ID stored
# in the session
@login_manager.user_loader
def load_user(name):
    with open('rewind/users.json') as f:
        my_dict = json.load(f)
        user = my_dict['users'][name]
    return User(user['username'], user['password'])


def insert_user(username, password):
    with open('rewind/users.json') as f:
        my_dict = json.load(f)
        my_dict[username] = {"username": username, "password": password}
    return User(user['username'], user['password'])


def insert_record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO record(band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (band, record, record_cover, price, current_buyers, max_buyers, pitchfork_score, pitchfork_link, review_snippet, days_to_go))
        con.commit()


def select_record(record_id):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        result = cur.execute(
            ''.join(("SELECT * FROM record WHERE id=", str(record_id))))
        return result.fetchall()


def get_shop_info():
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        result = cur.execute(
            "SELECT band,record,price,current_buyers,max_buyers FROM record")
        return result.fetchall()


def buy_record(userid, band, record, record_cover, price, days_to_go):
    with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO claimed_records(userid, band, record, record_cover, price, days_to_go ) VALUES(?,?,?,?,?,?)",
                    (userid, band, record, record_cover, price, days_to_go))
        con.commit()
