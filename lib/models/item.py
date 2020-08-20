from lib.models.base import BaseModel, db


class Item(BaseModel):
    __tablename__ = "items"

    id = db.Column(db.Unicode(), primary_key=True)
    description = db.Column(db.Unicode(), nullable=False)
    price = db.Column(db.Float, nullable=False)
