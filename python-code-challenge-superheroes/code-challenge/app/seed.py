from app import app, db
from models import Hero

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

def seed_heroes():
    with app.app_context():
        # hero = Hero(name="Dio", super_name="The World" )
        # db.session.add(hero)
        # db.session.commit()
        for heroes in all_heroes:
            new_hero = Hero(name=heroes["name"], super_name=heroes["super_name"])
            db.session.add(new_hero)
        db.session.commit()    

seed_heroes()        