from fastapi import APIRouter
from database.agent_db import AgentDB
from database.mission_db import MissionDB

router = APIRouter(prefix='/missions')

@router.post('')
def create_a_mission():
    MissionDB.create_mission()

@router.get('')
def show_all_missions():
    MissionDB.get_all_missions()

@router.get('/{id}')
def show_mission_by_id(id:int):
    MissionDB.get_mission_by_id(id)

@router.put('{id}/assign/{agent_id}')
def assign_mission_to_agent(mission_id, agent_id):
    MissionDB.assign_mission(mission_id, agent_id)

@router.put('/{id}/start')
def start_mission(mission_id:int , new_status: str):
    MissionDB.update_mission_status(mission_id, new_status)

@router.put('/{id}/complete')
def finish_successfuly(mission_id:int , new_status: str, agent_id: int):
    MissionDB.update_mission_status(mission_id, new_status)
    AgentDB.increment_completed(agent_id)

@router.put('/{id}/fail')
def failed_mission(mission_id:int , new_status: str, agent_id: int):
    MissionDB.update_mission_status(mission_id, new_status)
    AgentDB.increment_failed(agent_id)

@router.put('/{id}/cancel')
def cancel_mission(mission_id:int , new_status: str,agent_id, updated_data):
    MissionDB.update_mission_status(mission_id, new_status)
    AgentDB.update_agent(agent_id,updated_data)