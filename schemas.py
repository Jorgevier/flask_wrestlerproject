from marshmallow import Schema, fields

class WrestlerSchema(Schema):
    id = fields.Str(dump_only = True)
    first_name = fields.Str()
    last_name = fields.Str()
    nickname = fields.Str()
    billing_from= fields.Str()
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True )

class WrestlerLogin(Schema):
    username = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True )

class StatSchema(Schema):
    id = fields.Str(dump_only = True)
    signature_moves = fields.Str(required = True)

class StatSchemaNested(StatSchema):
  user = fields.Nested(WrestlerSchema, dump_only = True)

class WrestlerSchemaNested(WrestlerSchema):
  posts = fields.List(fields.Nested(StatSchema), dump_only=True)

