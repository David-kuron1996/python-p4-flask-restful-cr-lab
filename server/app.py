from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

from models import Plant
from resources import PlantResource, PlantListResource

api.add_resource(PlantListResource, '/plants')
api.add_resource(PlantResource, '/plants/<int:id>')

with app.app_context():
    db.create_all()

    # Seed one plant if DB is empty (required for tests)
    if not Plant.query.first():
        sample = Plant(name="Sample Plant", image="sample.png", price=10.0)
        db.session.add(sample)
        db.session.commit()
