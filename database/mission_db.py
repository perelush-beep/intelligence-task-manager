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
                values (%s,%s,%s,%s,%s);""",(data['title'],data['description'],data['location'],data['difficulty'],data['importance'])
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
    
    def assign_mission(self,m_id,a_id):
        query = """"
                UPDATE mission SET assigned_agent_id=%s WHERE id=%s;
                """,(a_id,m_id)
        self.sql_executer(query)

    def update_mission_status(self,id,status):
        query = """"
                UPDATE mission SET status=%s WHERE id=%s;
                """,(status,id)
        self.sql_executer(query)

    def get_open_misssions_by_agent(self,id):
        filter_by_status = """"
                SELECT * FROM mission 
                WHERE status=%s OR WHERE status=%s;
                """,("ASSIGNED","IN_PROGRESS")
        
        data = self.sql_executer(filter_by_status)
        filter_missions_by_id = """"
                SELCTE * FROM %s WHERE id=%s;
                """,(data,id)
        return self.sql_executer(filter_missions_by_id)
    

    def count_all_missions(self):
        query = """"
                SELECT COUNT(*)
                FROM mission;
                """
        return self.sql_executer(query)
    
    def count_by_status(self,status):
        query = """"
                SELECT COUNT(*)
                FROM mission
                WHERE status=%s;
                """,(status,)
        return self.sql_executer(query)
        
    def count_open_missions(self):
        query = """"
                SELECT COUNT(*)
                FROM mission
                WHERE status=%s OR WHERE status=%s OR WHERE status=%s;
                """,("NEW","ASSIGNED","PROGRESS_IN")
        return self.sql_executer(query)
    
    def count_critical_missions(self):
        query = """"
                SELECT COUNT(*)
                FROM mission 
                WHERE status=%s;
                """,("CRITICAL",)
        return self.sql_executer(query)
    
    def get_top_agent(self):
        fetch_query = """"
                SELECT completed_missions FROM agents;
                """
        completed_missions_list = self.sql_executer(fetch_query)
        most = 0
        for mission in completed_missions_list:
            if mission > most:
                most = mission
        final_query = """"
                        SELECT * FROM agents 
                        WHERE completed_missions=%s;
                        """,(most,)
        return self.sql_executer(final_query)
