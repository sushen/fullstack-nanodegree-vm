import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


#Restaurant class

class Restaurant(Base):
    # table Information
    __tablename__ = 'restaurant'

    # Mapper
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)

#MenuItem class

class MenuItem(Base):
    # table Information
    __tablename__='menu_item'

    # Mapper
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant_id'))
    restaurant = relationship(Restaurant)

########## insert end of the file ################

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
