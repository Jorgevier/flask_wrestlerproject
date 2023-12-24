from marshmallow import Schema, fields

class WrestlerSchema(Schema):
    id = fields.Str(dump_only = True)
    first_name = fields.Str()
    last_name = fields.Str()
    nickname = fields.Str()
    billing_from= fields.Str()

class StatSchema(Schema):
    id = fields.Str(dump_only = True)
    signature_moves = fields.Str(required = True)



