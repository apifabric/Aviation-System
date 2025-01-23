# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 23, 2025 10:42:36
# Database: sqlite:////tmp/tmp.eBwT6bNzmS/Aviation_System_iter_1_3/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Airplane(Base):  # type: ignore
    """
    description: Represents an airplane entity.
    """
    __tablename__ = 'airplane'
    _s_collection_name = 'Airplane'  # type: ignore

    id = Column(Integer, primary_key=True)
    model = Column(String)
    seating_capacity = Column(Integer)
    passenger_count = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    PassengerList : Mapped[List["Passenger"]] = relationship(back_populates="airplane")



class Airport(Base):  # type: ignore
    """
    description: Represents an airport entity.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    city = Column(String)
    country = Column(String)
    latitude : DECIMAL = Column(DECIMAL)
    longitude : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)

    # child relationships (access children)



class Passenger(Base):  # type: ignore
    """
    description: Represents a passenger entity with a link to airplane.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    luggage_weight_total : DECIMAL = Column(DECIMAL)
    airplane_id = Column(ForeignKey('airplane.id'))

    # parent relationships (access parent)
    airplane : Mapped["Airplane"] = relationship(back_populates=("PassengerList"))

    # child relationships (access children)
    LuggageList : Mapped[List["Luggage"]] = relationship(back_populates="passenger")



class Luggage(Base):  # type: ignore
    """
    description: Represents luggage linked to a passenger.
    """
    __tablename__ = 'luggage'
    _s_collection_name = 'Luggage'  # type: ignore

    id = Column(Integer, primary_key=True)
    passenger_id = Column(ForeignKey('passenger.id'))
    weight : DECIMAL = Column(DECIMAL)

    # parent relationships (access parent)
    passenger : Mapped["Passenger"] = relationship(back_populates=("LuggageList"))

    # child relationships (access children)
