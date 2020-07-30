import uvicorn
from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from main.database import Base, engine
from main.web.api import item, user
from main.web.mvc import index
from main.web.mvc import item as item_mvc

from main.common.dto.response import ResponseDto
from main.common.type.sys_code import SysCode
from main.common.exception import SysException

# create database tables
Base.metadata.create_all(bind=engine)

# instance FastAPI
app = FastAPI()


#################### Configuration #################### 

# error handlers
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(ResponseDto.fail(SysCode.INVALID, exc.errors()))
    )

@app.exception_handler(SysException)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(ResponseDto.fail(exc.code, exc.data))
    )

@app.exception_handler(Exception)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(ResponseDto.fail())
    )


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
