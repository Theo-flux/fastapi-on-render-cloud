from fastapi import FastAPI
import uvicorn

from routers.users import route as users_route
from routers.products import route as products_route


app = FastAPI()

#routes
app.include_router(users_route, prefix='/users', tags=['users'])
app.include_router(products_route, prefix='/products', tags=['products'])

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
