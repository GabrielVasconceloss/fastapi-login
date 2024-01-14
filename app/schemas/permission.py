from typing import Optional
from pydantic import BaseModel, EmailStr


# Shared properties
class PermissionBase(BaseModel):
    descr: Optional[str] = None


# Properties to receive via API on creation
class PermissionCreate(PermissionBase):
    pass




# Properties to receive via API on update
class PermissionUpdate(PermissionBase):
    pass


class PermissionInDBBase(PermissionBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Permission(PermissionInDBBase):
    pass


# Additional properties stored in DB
class PermissionInDB(PermissionInDBBase):
    pass
