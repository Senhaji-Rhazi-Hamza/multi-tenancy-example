import lib.database as db
from datetime import datetime
from lib.utils.unique_identifier import generate_id


class class_property(object):

    # This class property is inspired from the behaviour of flaskSqlAlchemy
    # The behaviour of querying directly a model User.query.. is nice, but
    # the flaskSqlAlchemy dependency is not, so the behaviour is reproduced
    # with this trick of class property
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


class BaseModel(db.Base):

    __abstract__ = True
    creation_timestamp = db.Column(db.DateTime())

    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)
        self.creation_timestamp = datetime.utcnow()

    @classmethod
    def exists(cls, uid):
        return cls.get_by_id(uid) is not None

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def delete_all(cls):
        db.session.query(cls).delete()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, uid):
        return db.session.query(cls).get(uid)

    @classmethod
    def get_by_ids(cls, ids):
        pk_attr = getattr(cls, cls.get_primary_key_name())
        return cls.query.filter(pk_attr.in_(ids)).all()

    @classmethod
    def create(cls, uid=None, **kwargs):
        if not uid and cls.get_primary_key_name() not in kwargs.keys():
            uid = generate_id()
        return cls.create_instance(uid, **kwargs)

    @classmethod
    def get_or_create(cls, uid=None, **kwargs):
        uid = uid or kwargs.get(cls.get_primary_key_name())
        instance = cls.get_by_id(uid) if uid else None
        if not instance:
            instance = cls.create(uid=uid, **kwargs)
        return instance

    @classmethod
    def get_primary_key_name(cls):
        return db.inspect(cls).primary_key[0].name

    @classmethod
    def create_instance(cls, uid, **kwargs):
        if uid:
            kwargs[cls.get_primary_key_name()] = uid
        instance = cls(**kwargs)
        instance.creation_timestamp = datetime.utcnow()
        instance.save()
        return instance

    def get_id(self):
        pk = self.get_primary_key_name()
        return getattr(self, pk)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @class_property
    def query(cls):
        return cls.session.query(cls)

    @class_property
    def session(cls):
        session = db.gen_session()
        if hasattr(cls, 'has_request_context') and cls.has_request_context():
            session.connection(
            execution_options={"schema_translate_map": {None: cls.get_organization_id()}}
            )
        return session
