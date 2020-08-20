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
from sqlalchemy.orm import sessionmaker, relationship
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

gen_session = sessionmaker(bind=engine)
connection = engine.connect().execution_options(
  schema_translate_map={None: SELECTED_SCHEMA}
  )
session = gen_session(bind=connection)

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
