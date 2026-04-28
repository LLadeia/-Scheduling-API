from app.core.security import verify_password, create_access_token

@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data["email"]).first()

    if not user or not verify_password(data["password"], user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": user.email})

    return {"access_token": token}

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.user import User
from app.core.security import hash_password

router = APIRouter()

@router.post("/register")
def register(data: dict, db: Session = Depends(get_db)):
    user = User(
        email=data["email"],
        password=hash_password(data["password"])
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"msg": "Usuário criado"}