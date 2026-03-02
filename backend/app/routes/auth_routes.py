from fastapi import APIRouter,HTTPException
from app.schemas.user_schema import UserCreate, UserResponse , UserLogin, TokenResponse
from app.models.user_model import create_user , authenticate_user
from app.utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])



@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    new_user = await create_user(user.dict())
    return new_user




@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    db_user = await authenticate_user(user.email, user.password)
    
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": db_user["email"]})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }