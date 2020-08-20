from lib.models.base import BaseModel, db


class Order(BaseModel):
    __tablename__ = "orders"

    id = db.Column(db.Unicode(), primary_key=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(
        db.Unicode(), db.ForeignKey("public.users.id", ondelete="CASCADE")
    )
    item_id = db.Column(
        db.Unicode(), db.ForeignKey("items.id", ondelete="CASCADE")
    )
