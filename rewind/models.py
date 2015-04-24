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
        self.records = self.get_bought_records()

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_bought_records(self):
        records = []
        with open('rewind/db2.json') as f:
            my_dict = json.load(f)
            for rec in my_dict['bought_records']:
                if rec['username'] == self.name:
                    records.append(rec)
        return records

    def is_admin(self):
        if self.name == 'harrismendell':
            return True
        return False

    @classmethod
    def get(self_class, user):
        with open('rewind/db.json') as f:
            my_dict = json.load(f)
            u = my_dict['users'][user]
            return User(u['username'], u['password'])


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
        for rec in my_dict['records']:
            if rec['record'] == record:
                return rec


def get_shop_info():
    with open('rewind/db.json') as f: 
        my_dict = json.load(f)
        return my_dict['records']


def buy_record(username, band, record, record_cover, price, days_to_go):
    with open('rewind/db2.json') as f:
        my_dict = json.load(f)
    with open('rewind/db2.json', 'w') as f:
        my_dict['bought_records'].append({"username": username, "band": band, "record": record, "record_cover": record_cover, "price": price, "days_to_go": days_to_go})
        json.dump(my_dict, f)

def search_for_record(search_term):
    with open ('rewind/db.json') as f:
        my_dict = json.load(f)
        for record in my_dict['records']:
            if search_term.lower() == record['record'].lower():
                return "/record/" + record['record']
    return ''

def add_blog_post(data):
    blog_body = data['blog_body']
    blog_title =data['blog_title']

    with open('rewind/blog.json') as f: 
        my_dict = json.load(f)
        my_dict.append({"title": blog_title, "body": blog_body})
    with open('rewind/blog.json', 'w') as f:
        json.dump(my_dict, f)

    return my_dict

def get_blogs():
    with open('rewind/blog.json') as f: 
        my_dict = json.load(f)
    return my_dict


