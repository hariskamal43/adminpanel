from enum import unique
from fastapi import status,  Depends, APIRouter, File, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
    prefix= "/users",
    tags=['Users']
)


@router.post("/", status_code= status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db) ):
    
    #hash the password
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    
    #get_user(user.username, db)
    if db.query(models.User).filter(models.User.username == user.username).first():    
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED,
        detail="username already exist")

    elif db.query(models.User).filter(models.User.email == user.email).first():    
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED,
        detail="email already exist")

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return{"details": "Your account has been created"}

    
'''@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"user with id: {id} doesnot exist")

    return user'''

'''@router.post("/upload_file")
def create_upload_file(file: bytes | None = File(None), db: Session = Depends(get_db)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}'''