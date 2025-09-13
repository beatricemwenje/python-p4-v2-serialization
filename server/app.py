# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return make_response({'message': 'Welcome to the pet directory!'}, 200)

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.get(id)
    if pet:
        return make_response(pet.to_dict(), 200)
    else:
        return make_response({'message': f'Pet {id} not found.'}, 404)

@app.route('/species/<string:species>')
def pet_by_species(species):
    pets = [pet.to_dict() for pet in Pet.query.filter_by(species=species).all()]
    return make_response({'count': len(pets), 'pets': pets}, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
