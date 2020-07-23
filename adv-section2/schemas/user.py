from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta:
        load_only = ("password", ) #Password will only be used on load (deserialize)
        dump_only = ("id",) #Id will only be used on dump (serialize)
    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)