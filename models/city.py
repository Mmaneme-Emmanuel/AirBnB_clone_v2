#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), nullable=False, Foreignkey('states.id'))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
