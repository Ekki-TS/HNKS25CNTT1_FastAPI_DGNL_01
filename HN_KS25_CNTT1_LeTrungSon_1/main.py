from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database import Base, engine
from routers import room_router, room_type_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(room_router.router)
app.include_router(room_type_router.router)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "statusCode": exc.status_code,
            "error": str(exc.detail),
            "message": str(exc.detail),
            "data": None,
        },
    )


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "statusCode": 400,
            "error": "Request Validation Error",
            "message": "Dữ liệu đầu vào không hợp lệ",
            "data": None,
        },
    )
