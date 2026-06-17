import mysql.connector

class MissionDB:

    #connect to data base, execute sql, auto conmmit, fetchall. print exception in case of error and close connection and cursor afterward
    def sql_executer(query):
        try:
            connection = mysql.connector.connect()
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            connection.close()

    def create_mission(self,data):
        query = """"
                INSERT INTO mission (title, description, location, difficulty, importance) 
                values (%s,%s,%s,%s,%s);""",(data['title'],data['description'],data['location'],data['fifficulty'],data['importance'])
        query2 = """"
                SELECT * FROM mission WHERE description=%s AND location=%s;
                """,(data['description'],data['location'])
        self.sql_executer(query)
        return self.sql_executer(query2)
    
    def get_all_missions(self):
        query = """"
                SELECT * FROM mission;
                """
        return self.sql_executer(query)
    
    def get_mission_by_id(self,id):
        query = """"
                SELECT * FROM mission
                WHERE id=%s;
                """,(id,)
        return self.sql_executer(query)
    
    def update_mission(self,m_id,a_id):
        query = """"
                UPDATE assigned_agent_id=%s WHERE id=%s;
                """,(a_id,m_id)
        self.sql_executer(query)