from flask import Flask
from flask_restful import Resource, Api

from gamerecords import GameRecords

app = Flask(__name__)
api = Api(app)
gamerecords = GameRecords()

class Table(Resource):
    def get(self, game_id):
        return gamerecords.get_records(game_id)

api.add_resource(Table, '/table/<int:game_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
