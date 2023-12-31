from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List, Any
from pydantic import BaseSettings, BaseModel
from models.users import User
from models.events import Event
from beanie import PydanticObjectId

class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(),
            document_models=[Event, User]
        )
        return False

    class Config:
        env_file = ".env"

class Database:
    def __init__(self, model):
        self.model = model

    """Create"""
    async def save(self, document) -> None:
        print("It is here")
        await document.create()
        return
    
    """"Read one"""
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    """Read all"""
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    """Udpate"""
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k, v in des_body.items() if v is not None}
        update_query = {
            "$set": {
                field: value for field, value in des_body.items()
            }
        }
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    
    """Delete"""
    async def delete(self, id: PydanticObjectId) ->bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
