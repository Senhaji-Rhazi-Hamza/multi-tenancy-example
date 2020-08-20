from lib.models.base import BaseModel, BillableAction, db



class Order(BaseModel):
    __tablename__ = "orders"
    id = db.Column(db.Unicode(), primary_key=True)
    user_id = db.Column(
        db.Unicode(), db.ForeignKey("users.id", ondelete="CASCADE")
    )
    item_id = db.Column(
        db.Unicode(), db.ForeignKey("items.id", ondelete="CASCADE")
    )
