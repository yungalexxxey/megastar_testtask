from fastapi import HTTPException
from sqlalchemy.orm import Session
from service.db.database_schema import DbWriter
from tools.logger import logger

local_storage = {}


def get_writer(writer_id: int, db: Session):
    if writer_id not in local_storage:
        logger.debug("got from db")
        writer_from_db = db.query(DbWriter).filter(DbWriter.id == writer_id).first()
        if not writer_from_db:
            raise HTTPException(status_code=404, detail='Writed not found\n')
        local_storage[writer_id] = writer_from_db
        return writer_from_db
    logger.debug("got from local")
    return local_storage[writer_id]
