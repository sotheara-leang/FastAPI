import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from main.database import Base, engine
from main.web.api import item, user
from main.web.mvc import index
from main.web.mvc import item as item_mvc

# create database tables
Base.metadata.create_all(bind=engine)

# instance FastAPI
app = FastAPI()

# static files
app.mount("/static", StaticFiles(directory="webapp/public"), name="static")

# routes - api
app.include_router(user.router, prefix="/api/user")
app.include_router(item.router, prefix="/api/role")

# routes - mvc
app.include_router(index.router)
app.include_router(item_mvc.router, prefix="/item")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
