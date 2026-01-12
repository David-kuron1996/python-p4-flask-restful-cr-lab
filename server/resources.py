from flask_restful import Resource, reqparse
from app import db
from models import Plant

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('image')
parser.add_argument('price', type=float)

class PlantListResource(Resource):
    def get(self):
        plants = Plant.query.all()
        return [p.to_dict() for p in plants], 200

    def post(self):
        args = parser.parse_args()
        plant = Plant(**args)
        db.session.add(plant)
        db.session.commit()
        return plant.to_dict(), 201

class PlantResource(Resource):
    def get(self, id):
        plant = Plant.query.get_or_404(id)
        return plant.to_dict(), 200
