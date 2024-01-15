#!/usr/bin/env python3

from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Hero

import os

abs_path = os.getcwd()

db_path = f"sqlite:///{abs_path}/db/app.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

all_heroes = [
  { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
  { "name": "Doreen Green", "super_name": "Squirrel Girl" },
  { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
  { "name": "Janet Van Dyne", "super_name": "The Wasp" },
  { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
  { "name": "Carol Danvers", "super_name": "Captain Marvel" },
  { "name": "Jean Grey", "super_name": "Dark Phoenix" },
  { "name": "Ororo Munroe", "super_name": "Storm" },
  { "name": "Kitty Pryde", "super_name": "Shadowcat" },
  { "name": "Elektra Natchios", "super_name": "Elektra" }
]

db.init_app(app)

@app.route('/')
def home():
    return ''

@app.route('/add_seed')
def add_seed():
    hero = Hero(name="Jotaro", super_name="Star Platinum" )
    db.session.add(hero)
    db.session.commit()

    return "Hero Added"

@app.route('/heroes')
def heroes():
    return jsonify(all_heroes)


if __name__ == '__main__':
    app.run(port=3000, debug=True)
