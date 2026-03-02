from fastapi import FastAPI, Depends
from app.routes import auth_routes
from app.services.auth_dependency import get_current_user

app = FastAPI(
    title="AI Smart Reply API",
    version="1.0.0"
)

app.include_router(auth_routes.router)

@app.get("/")
async def health_check():
    return {"status": "running"}

@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "logged_in_user": current_user
    }