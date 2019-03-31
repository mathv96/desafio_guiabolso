import DAO.conn as connection

from config import * 

def create_table():
    conn = connection.connection_mysql() 
    query = "CREATE TABLE IF NOT EXISTS {} (id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, {} VARCHAR (200) NOT NULL,{} VARCHAR (20) NOT NULL,{} VARCHAR (200) NOT NULL,{} VARCHAR (20) NOT NULL, {} DATETIME NOT NULL)".format(
            table_name, 'component', 'version', 'responsible', 'status', 'date')
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.close()
        except Exception as e:
            conn.close()
            print(e.__context__)
            return False
        return True
    else:
        return False