from werkzeug.local import LocalProxy
from flask import request, g, has_request_context
from lib.models import db, BaseModel


def setup(app):
    app.before_request(set_schema)

def get_organization_id():
    if 'organization_id' in g:
        return g.organization_id
    return None

def set_schema():
    organization_id = request.json.get("organization_id") \
      if request.json else None
    if organization_id:
        g.organization_id = organization_id
        BaseModel.has_request_context = has_request_context
        BaseModel.get_organization_id = lambda : LocalProxy(get_organization_id)
 