from fastapi import APIRouter

route = APIRouter()

@route.get('/', response_description='shows lists of users')
async def list_users():
    return {'users': 'list of users'}
