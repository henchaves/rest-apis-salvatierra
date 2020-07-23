from ma import ma
from models.item import ItemModel
from models.store import StoreModel

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel
        load_only = ("store", ) #Password will only be used on load (deserialize)
        dump_only = ("id",) #Id will only be used on dump (serialize)
        load_instance = True
        include_fk = True