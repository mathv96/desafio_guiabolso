import DAO.conn as connection
from datetime import datetime

from config import * 

class Insert():
    def insert_event(self, event):
        conn = connection.connection_mysql() 
        query = "INSERT INTO {} (component, version, responsible, status, date) VALUES('{}', '{}', '{}', '{}', '{}')".format(
                table_name, event.component, event.version, event.responsible, event.status, event.date
            )
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query)
                conn.commit()
                conn.close()
            except Exception as e:
                conn.rollback()
                conn.close()
                print(e.__context__)
                return False
            return True
        else:
            return False
