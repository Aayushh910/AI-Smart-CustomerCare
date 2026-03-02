from app.config.database import database
from app.utils.security import hash_password,verify_password
from bson import ObjectId

users_collection = database["users"]



async def create_user(user_data: dict):
    user_data["password"] = hash_password(user_data["password"])
    result = await users_collection.insert_one(user_data)
    user_data["id"] = str(result.inserted_id)
    del user_data["_id"]
    del user_data["password"]
    return user_data



async def authenticate_user(email: str, password: str):
    user = await users_collection.find_one({"email": email})
    if not user:
        return None
    
    if not verify_password(password, user["password"]):
        return None
    
    user["id"] = str(user["_id"])
    del user["_id"]
    del user["password"]
    return user