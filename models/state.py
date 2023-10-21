#!/usr/bin/python3
""" State Module for HBNB project """
import models
import shlex
import sqlalchemy
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete=opphan",
                                backref="state")

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

        if getenv("HBNB_TYPE_STORAGE") != 'db':
            @property
            def cities(self):
                """getter for cities"""
                var = models.storage.all()
                city_list = []
                result = []
                for city in var:
                    city = key.replace('.', ' ')
                    city = shlex.split(city)
                    if city.state_id == self.id:
                        city_list.append(var[key])
                for elem in city_list:
                    result.append(elem)
                return city_list
