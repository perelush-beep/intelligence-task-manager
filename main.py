from fastapi import FastAPI
from routes.agent_routes import router as agent_router
from routes.mission_routes import router as mission_router
from routes.report_routes import router as report_router
from database.db_connection import DB_connection
from routes.agent_routes import *
from routes.mission_routes import *
from routes.report_routes import *
from logs.logger_config import logger

app = FastAPI()
app.include_router(agent_router)
app.include_router(mission_router)
app.include_router(report_router)
DB_connection.create_database()
DB_connection.create_tables()
logger.info('server runing, database and tables created')


#overall info
get_summary()
status_summary()
top_agent()

# modifiictaion function for agent table
add_new_agent()
get_all_the_agents()
agent_by_is_id()
update_agent_data()
deactivate_an_agent()
how_agent_have_preformed()

# modifiictaion function for mission table
create_a_mission()
show_all_missions()
assign_mission_to_agent()
start_mission()
finish_successfuly()
failed_mission()
cancel_mission()
