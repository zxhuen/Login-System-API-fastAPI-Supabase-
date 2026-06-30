from sqlalchemy.orm import Session
from app.models.User import User
from app.schema.User import UserCreate, UserResponse

def create_user_repo(db: Session, Users: UserCreate):
    db_user = User(**Users.model_dump())

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_repo(db: Session):
    return db.query(User).all()

def edit_user_repo(db: Session, user_id: int, Users: UserCreate):
    user_from_db = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user_from_db is None:
        return None
    
    user_from_db.last_name = Users.last_name
    user_from_db.first_name = Users.first_name
    user_from_db.middle_name = Users.middle_name
    user_from_db.age = Users.age

    db.commit()
    db.refresh(user_from_db)

    return user_from_db


def delete_user_repo(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None
    
    db.delete(user)
    db.commit()

    return user

def get_user_by_email(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()

    return user