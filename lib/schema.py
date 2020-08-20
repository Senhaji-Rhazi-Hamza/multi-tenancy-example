from config import SELECTED_SCHEMA, SCHEMAS
from flask import request
from lib.models import db


def setup(app):
    app.before_request(set_schema)


def set_schema():
    organization_id = request.json.get("organization_id") \
      if request.json else None
    if organization_id:
        db.session.connection(
            execution_options={"schema_translate_map": {None: organization_id}}
        )
