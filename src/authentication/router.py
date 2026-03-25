from fastapi import APIRouter, Depends, HTTPException, status

from .auth import (
    authenticate_user,
    create_access_token,
    create_user,
    get_current_user,
)
from .models import Token, UserCreate, UserLogin, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=UserOut)
async def register(data: UserCreate):
    user = create_user(data)
    return UserOut(id=user["id"], name=user["name"], email=user["email"])


@router.post("/login", response_model=Token)
async def login(data: UserLogin):
    user = authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    token = create_access_token(data={"sub": user["id"], "email": user["email"], "name": user["name"]})
    return Token(access_token=token)


@router.get("/me", response_model=UserOut)
async def me(current_user: UserOut = Depends(get_current_user)):
    return current_user
