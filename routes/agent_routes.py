from fastapi import APIRouter
from database.agent_db import AgentDB

router = APIRouter(prefix='/agents')

@router.post('')
def add_new_agent(data:dict):
    AgentDB.create_agent(data)

@router.get('')
def get_all_the_agents():
    AgentDB.get_all_agents()

@router.get('/{id}')
def agent_by_is_id(id:int):
    AgentDB.get_agent_by_id(id)

@router.put('/{id}')
def update_agent_data(id:int,data:dict):
    AgentDB.update_agent(id,data)

@router.put('{id}/deactivate')
def deactivate_an_agent(id:int):
    AgentDB.deactivate_agent(id)

@router.get('{id}/performance')
def how_agent_have_preformed(id):
    AgentDB.get_agent_by_id(id)