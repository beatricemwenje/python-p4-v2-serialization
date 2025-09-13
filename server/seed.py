#!/usr/bin/env python3
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    fake = Faker()
    Pet.query.delete()

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = [Pet(name=fake.first_name(), species=rc(species)) for _ in range(10)]

    db.session.add_all(pets)
    db.session.commit()
