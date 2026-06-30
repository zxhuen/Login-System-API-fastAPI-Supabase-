from sqlalchemy.orm import Session
from app.repository.user_repo import create_user_repo, get_user_repo, edit_user_repo, delete_user_repo
from app.schema.User import UserCreate, UserResponse

def add_user_services(db: Session, Create: UserCreate):
    return create_user_repo(db, Create)

def list_user_services(db: Session):
    return get_user_repo(db)

def edit_user_services(db: Session, person_id: int, user: UserCreate):
    return edit_user_repo(db, person_id, user)

def delete_user_services(db: Session, user_id: int):
    return delete_user_repo(db, user_id)