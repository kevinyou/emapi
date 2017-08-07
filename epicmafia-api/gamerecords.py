import requests
import json
import os

class GameRecords:
    def __init__(self):
        self.folder = './data/gamerecords/'
        self.url = 'https://s3.amazonaws.com/em-gamerecords/'

    def get_records(self, game_id):
        file_path = self.folder + str(game_id)
        if os.path.isfile(file_path):
            with open(file_path) as infile:
                return json.load(infile)
        # TODO: only proceed on successful request
        r = requests.get(url=self.url + str(game_id))
        if r.status_code == 200:
            game_data = r.json()
            with open(file_path, 'w') as outfile:
                json.dump(game_data, outfile)
            # save
            return game_data
        else:
            # TODO: return 400?
            return {'message':'Game does not exist.'}
