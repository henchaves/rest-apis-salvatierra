from ma import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_only = ("password", ) #Password will only be used on load (deserialize)
        dump_only = ("id",) #Id will only be used on dump (serialize)
        load_instance = True