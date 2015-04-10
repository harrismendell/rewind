__author__ = 'sunnyharris'
from flask import Flask, flash, redirect, url_for, request, get_flashed_messages
from flask.ext.login import LoginManager, UserMixin, current_user, login_user, logout_user, current_user
from rewind import app, login_manager
import json


class User(UserMixin):

    def __init__(self, name, password, active=True):
        self.id = name
        self.name = name
        self.password = password
        self.active = active
        # self.records = self.get_bought_records()

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    # def get_bought_records(self):
    #     userid = self.id
    #     with sql.connect("/Users/sunnyharris/rewind/rewind/database.db") as con:
    #         cur = con.cursor()
    #         result = cur.execute(
    #             "SELECT * FROM claimed_records WHERE userid=" + str(userid))
    #         return result.fetchall()

    @classmethod
    def get(self_class, user):
        with open('rewind/users.json') as f:
            my_dict = json.load(f)
            user = my_dict['users'][name]


class UserNotFoundError(Exception):
    pass

@login_manager.user_loader
def load_user(name):
    with open('rewind/db.json') as f:
        my_dict = json.load(f)
        user = my_dict['users'][name]
    return User(user['username'], user['password'])


def insert_user(username, password):
    with open('rewind/db.json') as f:
        my_dict = json.load(f)
        my_dict['users'][username] = {"username": username, "password": password}
    with open('rewind/db.json', 'w') as f:
        json.dump(my_dict, f)
    return User(username, password)


def insert_record(band, record, record_cover, price, current_buyers, max_buyers, 
    pitchfork_score, pitchfork_link, review_snippet, days_to_go):
    with open('rewind/db.json') as f: 
        my_dict = json.load(f)
        my_dict['records'].append({"band": band, "record": record, "record_cover": record_cover, "price": price, "current_buyers": current_buyers, "max_buyers": max_buyers, "pitchfork_score": pitchfork_score, "pitchfork_link": pitchfork_link, "review_snippet": review_snippet, "days_to_go": days_to_go})
    with open('rewind/db.json', 'w') as f:
        json.dump(my_dict, f)

def select_record(record):
    with open('rewind/db.json') as f: 
        my_dict = json.load(f)
        for record in my_dict['records']:
            if record['record'] = record:
                return record


def get_shop_info():
    with open('rewind/db.json') as f: 
        my_dict = json.load(f)
        return my_dict['records']


def buy_record(userid, band, record, record_cover, price, days_to_go):
    with open('rewind/db.json') as f: 
        cur = con.cursor()
        cur.execute("INSERT INTO claimed_records(userid, band, record, record_cover, price, days_to_go ) VALUES(?,?,?,?,?,?)",
                    (userid, band, record, record_cover, price, days_to_go))
        con.commit()
