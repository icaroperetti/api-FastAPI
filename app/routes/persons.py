from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.models.person import get_all_persons
from app.config.db import get_db

router = APIRouter(
    prefix="/persons",
    tags=["persons"],
)


@router.get("/", response_model=List[dict])
def get_persons(
    offset: int = Query(description="Offset para paginação"),
    limit: int = Query(10),
    db: Session = Depends(get_db),
):
    persons = get_all_persons(db, offset=offset, limit=limit)

    return persons