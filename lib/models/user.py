from lib.models.base import BaseModel, db


class User(BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Unicode(), primary_key=True)
    name = db.Column(db.Unicode(), nullable=False)
    mail = db.Column(db.Float, nullable=False)
    password = db.Column(db.Unicode(), nullable=False)
    organization_id = db.Column(db.Unicode(), nullable=False)
