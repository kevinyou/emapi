from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Table(Resource):
    def get(self, game_id):
        r = requests.get(url='https://s3.amazonaws.com/em-gamerecords/' + str(game_id))
        return r.json()

api.add_resource(Table, '/table/<int:game_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
