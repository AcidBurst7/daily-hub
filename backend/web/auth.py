from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials


router = APIRouter(prefix="/auth", tags=["Авторизация"])

username: str = "me"
password: str = "password"
basic: HTTPBasicCredentials = HTTPBasic()

@router.get("/who")
def get_user(
    creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if creds.username == username and creds.password == password:
        return {
            "username": creds.username,
            "password": creds.password
        }
    raise HTTPException(status_code=401, detail="Логин или пароль введены неверно")