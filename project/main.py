from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from helper.event_helper import EventHelper
from strategys.validate_event import validate_event
from strategys.auth_verify import verify
from strategys.auth_identity import identity
from DAO.insert import Insert
from DAO.list import EventList
from DAO.list_search import EventListSearch
from DAO.create_table import create_table


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True #para o jwt retornar o erro como resposta da requisição
app.config['SECRET_KEY'] = 'desafio_guiabolso'
api = Api(app)

#jwt auth instance

jwt = JWT(app, verify, identity)

#def to the execution of each route

class Index(Resource):
    @jwt_required()
    def get(self):
        response = jsonify({'result':'API is working.'})
        response.status_code = 200
        return response

class Insert_event(Resource):
    # @jwt_required()
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
    # @jwt_required()
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

class List_search(Resource):
    # @jwt_required()
    def get(self):
        self.event_list_search = EventListSearch()
        #to do: json validation
        inputed_json = request.get_json()
        json_list = self.event_list_search.list_events_search(inputed_json)
        if json_list==False:
            response = jsonify({'result':'There\'s no list to return.'})
            response.status_code = 200
        else:
            response = jsonify(json_list)
            response.status_code = 200
        return response



#routes
api.add_resource(Index, '/')
api.add_resource(Insert_event, '/insert_event')
api.add_resource(List_events, '/list_events')
api.add_resource(List_search, '/list_search')

if __name__== '__main__':
    app.run(debug=True)