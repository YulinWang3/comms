import sqlite3
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class wyw_select_all(Resource):
    def get(self):
        rows = query("SELECT * FROM location_values")
        return rows

class wyw_select_one(Resource):
    def get(self, location_id):
        rows = query("SELECT * FROM location_values WHERE location_id={}".format(location_id))
        return rows

class wyw_select_locations(Resource):
    def get(self):
        rows = query("SELECT * FROM locations")
        return rows

# site dict_factory, got it from the sqlite3 docs
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
    
def query(queryString):
        db = None
        try:
            db = sqlite3.connect('./location.db')
        except Error as e:
            print(e)

        if not db:
            return "Failed to connect"
        else:
            db.row_factory = dict_factory
            cur = db.cursor()
            cur.execute(queryString)
            rows = cur.fetchall()
            return rows

api.add_resource(wyw_select_all, '/')
api.add_resource(wyw_select_one, '/location/<location_id>')
api.add_resource(wyw_select_locations, '/locations')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
