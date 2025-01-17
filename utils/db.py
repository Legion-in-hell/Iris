from beanie import *
from interactions import *
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from beanie import Document, init_beanie


class Sanctions(BaseModel):
    id : PydanticObjectId()
    user_id : str
    user_name : str
    reason : str
    mod_id : str
    mod_name : str
    s_type : str
    date : str


class DB_User(BaseModel):
    user_id : str
    user_name : str
    user_perms : list[str] = []
    user_roles : list[str] = []


class DB_Roles(BaseModel):
    role_id : str
    role_name : str
    role_perms : list[str] = []


class Ticket(BaseModel):
    ticket_id : str
    ticket_user : str
    ticket_status : str
    allowed_users : list[str] = []


class Server(Document):
    srv_id : str
    name : str
    owner_id : int
    owner_name : str
    sanctions : list[Sanctions] = []
    member_count : int
    role : list[DB_Roles] = []
    user : list[DB_User] = []
    tickets : list[Ticket] = []

