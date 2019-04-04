import json

import DAO.conn as connection
from config import * 

class EventListSearch():

    def list_events_search(self, search):
        conn = connection.connection_mysql() 
        query = "SELECT * FROM {} where {} = '{}'".format(table_name, search['campo'], search['valor'])

        if conn:
            cursor = conn.cursor()
            json_result = None
            try:
                cursor.execute(query)
                result_list = [list(line) for line in cursor.fetchall()]
                result_dict={}
                result_dict['result']=[]
                for line in result_list:
                    result_dict['result'].append({"id": str(line[0]), "component": str(line[1]),"version": str(line[2]), "responsible": str(line[3]), "status": str(line[4]), "date": str(line[5])})
                json_result = result_dict
                conn.close()
            except Exception:
                conn.close()
                return False
            return json_result
        else:
            return False