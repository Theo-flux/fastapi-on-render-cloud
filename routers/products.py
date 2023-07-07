from fastapi import APIRouter

route = APIRouter()

@route.get('/', response_description='list of products')
async def list_products():
    return {'products': 'list of produtcs'}
