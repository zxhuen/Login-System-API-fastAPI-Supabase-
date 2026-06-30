from sqlalchemy.orm import Session
from app.repository.user_repo import create_user_repo, get_user_repo, edit_user_repo, delete_user_repo, get_user_by_email
from app.schema.User import UserCreate, UserResponse
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def add_user_services(db: Session, Create: UserCreate):
    existing_user =  get_user_by_email(db, Create.email)

    if existing_user:
        raise HTTPException(
        status_code=409,
        detail="Email already exists."
    )

    try: 
        return create_user_repo(db, Create)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
        status_code=409,
        detail="Email already exists."
    )

def list_user_services(db: Session):
    return get_user_repo(db)

def edit_user_services(db: Session, person_id: int, user: UserCreate):
    return edit_user_repo(db, person_id, user)

def delete_user_services(db: Session, user_id: int):
    return delete_user_repo(db, user_id)