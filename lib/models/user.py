from lib.models.base import BaseModel, db
from lib.models.item import Item
from lib.models.order import Order


class User(BaseModel):
    __tablename__ = "users"
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Unicode(), primary_key=True)
    name = db.Column(db.Unicode(), nullable=False)
    mail = db.Column(db.Unicode(), nullable=False)
    password = db.Column(db.Unicode(), nullable=False)
    organization_id = db.Column(db.Unicode(), nullable=False)

    @classmethod
    def _get_user_priced_orders(cls):
        return cls.session.query(
            User.name,
            Item.description,
            Item.price,
            Order.quantity,
            (Order.quantity * Item.price).label('Total')
            ).join(Order).join(Item)

    def get_my_priced_orders(self):
        query = self._get_user_priced_orders()
        return query.filter(User.id == self.id).all()

    def get_my_priced_orders_jsonified(self):
        return [
            {
                "user name": result[0],
                "item name": result[1],
                "item price": result[2],
                "item quantity": result[3],
                "total fee": result[4]
            } for result in self.get_my_priced_orders()
            ]
