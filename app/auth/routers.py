from fastapi import APIRouter, Depends, HTTPException
from auth.schemas import UserCreate, UserLogin, Token, UserOut, RefreshTokenRequest
from auth.service import AuthService
from auth.token_service import TokenService
from auth.dependencies import get_auth_service
router = APIRouter()

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin, service_token: TokenService = Depends(), service: AuthService = Depends(get_auth_service)):
    user = await service.authenticate_user(user_data.username, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = service_token.create_access_token({"sub": user.username})
    refresh_token = service_token.create_refresh_token({"sub": user.username})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/register", response_model=UserOut)
async def register(user_data: UserCreate, service: AuthService = Depends(get_auth_service)) -> UserOut:
    user = await service.create_user(user_data)
    if not user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    return user

@router.post("/refresh", response_model=Token)
async def refresh_token(
    request: RefreshTokenRequest,
    service_token: TokenService = Depends()
):
    payload = service_token.decode_token(request.refresh_token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    username = payload.get("sub")
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    new_access_token = service_token.create_access_token({"sub": username})
    new_refresh_token = service_token.create_refresh_token({"sub": username})

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }