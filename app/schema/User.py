from pydantic import BaseModel, EmailStr, Field 

class UserCreate(BaseModel):
    username: str = Field(
        min_length=5,
        max_length=20,
        pattern=r"^[a-zA-Z0-9_]+$"
    )
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128
    )

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
    class Config:
        from_attributes = True