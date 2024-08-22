#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload storage
storage.reload()

"""storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()

A unique FileStorage/DBStorage instance for all models.

storage.reload()"""
