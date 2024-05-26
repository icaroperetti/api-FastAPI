from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.models.person_address import get_all_persons_adresses
from app.config.db import get_db


router = APIRouter(
    prefix="/persons_address",
    tags=["persons_address"],
)


@router.get("/", response_model=List[dict])
def get_persons_address(
    offset: int = Query(description="Offset para paginação"),
    limit: int = Query(10),
    db: Session = Depends(get_db),
):
    persons_addresses = get_all_persons_adresses(db, offset=offset, limit=limit)

    return persons_addresses
