from lib.models.base import db, BaseModel
from lib.models.user import User
from lib.models.item import Item
from lib.models.order import Order

from lib.utils.classes import all_subclasses


# create the tables if not creae


db.Base.metadata.create_all(db.engine)
db.session.commit()

all_BaseModel_subclasses = all_subclasses(BaseModel)

__all__ = [
  "db",
  "all_BaseModel_subclasses",
  "Item",
  "Order",
  "User"
  ]
