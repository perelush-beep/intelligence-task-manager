from fastapi import APIRouter
from database.mission_db import MissionDB
from database.agent_db import AgentDB

router = APIRouter(prefix='/reports')

@router.get('/summary')
def get_summary():
    summary = {}
    summary['all agents'] = AgentDB.get_all_agents()
    summary['active_agents_count'] = AgentDB.count_active_agents()
    summary['total_missions'] = MissionDB.get_all_missions()
    summary['open_missions'] = MissionDB.count_open_missions()
    summary['completed_missions'] = MissionDB.count_by_status('COMPLETE')
    summary['failed_missions'] = MissionDB.count_by_status('FAILED')
    summary['critical_missions'] = MissionDB.count_by_status('critical')
    return summary

@router.get('/missions-by-status')
def status_summary(status:str):
    summary = {}
    summary['open'] = MissionDB.count_by_status(status)
    summary['in_progress'] = MissionDB.count_by_status(status)
    summary['completed'] = MissionDB.count_by_status(status)
    summary['failed'] = MissionDB.count_by_status(status)
    summary['critical'] = MissionDB.count_critical_missions()
    return summary


@router.get('/top-agent')
def top_agent():
    return MissionDB.get_top_agent()