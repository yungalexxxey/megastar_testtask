from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import PlainTextResponse
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import ProgrammingError

from service.db.db_actions import get_writer
from service.db.alchemy import get_db
from service.schemas import OutputSchema

app = FastAPI()


@app.exception_handler(OperationalError)
async def raise_sql_conn_error(request, exc):
    return PlainTextResponse(f"Be sure u launched docker-compose file\nException data: {exc}")


@app.exception_handler(ProgrammingError)
async def raise_sql_conn_error(request, exc):
    return PlainTextResponse(f"Be sure u created valid tables\nException data:\n{exc}")


@app.get("/writers/{writer_id}", response_model=OutputSchema)
async def get_writer_data(writer_id: int, db: Session = Depends(get_db)) -> dict:
    return get_writer(writer_id, db)
