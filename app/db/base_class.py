from typing import Any
import re
from sqlalchemy.ext.declarative import as_declarative, declared_attr

camel_to_snake_ptr = re.compile(r'(?<!^)(?=[A-Z])')

def camel_to_snake(name):
    return camel_to_snake_ptr.sub('_', name).lower()

@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)
