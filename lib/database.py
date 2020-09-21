from sqlalchemy import (
    Column,
    String,
    Integer,
    Float,
    DateTime,
    Unicode,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.inspection import inspect
from sqlalchemy import DDL

from config import URI, SCHEMAS, SELECTED_SCHEMA

engine = create_engine(URI)

metadata = MetaData()
Base = declarative_base(metadata=metadata)


for schema in SCHEMAS:
    event.listen(
        Base.metadata,
        "before_create",
        DDL("CREATE SCHEMA IF NOT EXISTS " + schema)
    )

session_factory = sessionmaker(bind=engine)
gen_session = scoped_session(session_factory)
session = gen_session()

__all__ = [
    "Integer",
    "String",
    "Column",
    "DateTime",
    "Float",
    "inspect",
    "Unicode",
    "ForeignKey",
    "relationship",
    "UniqueConstraint",
]
