from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from validation.validate_event import validate_event
from DAO.insert import Insert
from DAO.list import EventList
from DAO.create_table import create_table
from helper.event_helper import EventHelper


app = Flask(__name__)
api = Api(app)

#def to the execution of each route

class Index(Resource):
    def get(self):
        response = jsonify({'result':'API is working.'})
        response.status_code = 200
        return response

# class Login(Resource):
#     def get(self):
#         return ''


class Insert_event(Resource):
    def post(self):
        self.evh = EventHelper()
        self.insert = Insert()

        inputed_json = request.get_json()
        response_validation = validate_event(inputed_json)
        if response_validation == False:
            response = jsonify(result="Please, send a request with the right json structure.")
            response.status_code = 200
            return response
        else:    
            response_creation = create_table()
            if response_creation:
                ev = self.evh.return_event(inputed_json)
                response_insert = self.insert.insert_event(ev)
                if response_insert:
                    response = jsonify({'result':'Event saved.'})
                    response.status_code = 201
                    return response
                else:
                    response = jsonify({'result':'Event was not saved.'})
                    response.status_code = 400
                    return response    
            else:
                response = jsonify({'result':'Was not possible to create table, verify if the database is avaible.'})
                response.status_code = 400
                return response    


class List_events(Resource):
    def get(self):
        self.event_list = EventList()
        json_list = self.event_list.list_events()
        if json_list==False:
            response = jsonify({'result':'There\'s no list to return.'})
            response.status_code = 200
        else:
            response = jsonify(json_list)
            response.status_code = 200
        return response

# class List_search(Resource):
#     def get(self):
#         self.event_list = EventList()
#         json_list = self.event_list.list_events()
#         if json_list==False:
#             response = jsonify({'result':'There\'s no list to return.'})
#             response.status_code = 200
#         else:
#             response = jsonify(json_list)
#             response.status_code = 200
#         return response



#routes
api.add_resource(Index, '/')
# api.add_resource(Login, '/login')
api.add_resource(Insert_event, '/insert_event')
api.add_resource(List_events, '/list_events')

if __name__== '__main__':
    app.run(debug=True)