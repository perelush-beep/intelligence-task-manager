import mysql.connector
class AgebtDB:
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
        
    def create_agent(self,data):
        query = """
            INSERT INTO agents (name,speciality) values (%s,%s);
        """, (data['name'],data['speciality'])
        self.sql_executer(query)
    
    def get_all_agents(self):
        query = "SELECT * FROM agents;"
        return self.sql_executer(query)

    def get_agent_by_id(self,id):
        query = """
            SELECT * FROM agents where id=%s;
                """(id,)
        return self.sql_executer(query)
    
    def update_agent(self,id,data):
        query = """
                UPDATE name=%s, speciality=%s, is_active=%s, completed_missions=%s, faild_mission=%s, agent_rank=%s where id=%s;
                """, (data['name'],data['speciality'],data['is_active'],data['completed_missions'],data['faild_missions'],data['agent_rank'],id)
        
    def deactivate_agent(self,id):
        query ="""
                UPDATE agents
                SET is_active=%s where id=%s;""",("false",id)
        self.sql_executer(query)
    
    #updates completed_missions column
    def increment_completed(self,id):
        query = """"
                UPDATE agents
                SET comleted_missions+%s
                WHERE id=%s;""",(1,id)
        self.sql_executer(query)

    #updates failed_missions column
    def increment_failed(self,id):
        query = """
                UPDATE agents
                SET failed_missions=%s
                WHERE id=%s;
                """,(1,id)
        self.sql_executer(query)
    
    def get_agent_preformance(self,id):
        query = """"
                SELECT completed_missions,failed_missions 
                FROM agents 
                WHERE id=%s;
                """(id,)
        data = self.sql_executer(query)
        preformances = {}
        preformances['completed'] = data[0]
        preformances['failed'] = data[1]
        preformances['total'] = data[0] + data[1]
        preformances['success_rate'] = (preformances['completed'] / preformances['total']) * 100
        return preformances
    
    def count_active_agents(self):
        query = """"
                SELECT is_active 
                FROM agents 
                WHERE is_active=true
                """
        data = self.sql_executer(query)
        return sum(data)
    