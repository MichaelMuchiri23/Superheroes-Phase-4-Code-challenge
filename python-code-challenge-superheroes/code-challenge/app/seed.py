from app import app, db
from datetime import datetime
from models import Hero, Power, HeroPower
from faker import Faker

fake = Faker()

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

def seed_powers():
    powers_data = [
        {"name": fake.word(), "description": fake.text()[:20]} for _ in range(10)
    ]

    for power_info in powers_data:
        power = Power(**power_info, created_at=datetime.now(), updated_at=datetime.now())
        db.session.add(power)

def seed_hero_powers():
    strengths = ["Strong", "Weak", "Average"]

    heroes = Hero.query.all()

    for hero in heroes:
        for _ in range(1, 4):
            power = Power.query.order_by(db.func.random()).first()
            hero_power = HeroPower(
                hero_id=hero.id,
                power_id=power.id,
                strength=fake.random_element(elements=strengths),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            db.session.add(hero_power)
            db.session.commit()

def seed_data():
    seed_powers()
    seed_heroes()
    seed_hero_powers()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding started -----")
        seed_data()
        print("Seeded successfully")
      