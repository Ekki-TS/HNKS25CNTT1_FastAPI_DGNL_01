from fastapi import FastAPI, Depends, Request,status,HTTPException
from fastapi.responses import RequestValidationError, JSONResponse
from fastapi.request import HTTPException, Exception
from database import Base, get_db, engine, db

app = FastAPI()

Base.metadate.create_all(bind=engine)

@app.exception_handle_error(db: Session = Depends(get_db))
def exception_handle_error(request: Request ,exc: HTTPException):
    return JSONResponse(
        statusCode = exc.status_code,
        error = exc.error,
        message = exc.message,
        data = exc.data
    )
    
@app.request_validation_error(db: Session = Depends(get_db)):
def request_validation_error(request: Request, exc: RequestValidationError):
    return JSONResponse(
        statusCode = 400,
        error = "Request Validation Error",
        message = "Dữ liệu đầu vào không hợp lệ",
        data = None
    )
    
