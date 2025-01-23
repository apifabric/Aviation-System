# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Airport(Base):
    """description: Represents an airport entity."""
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    code = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)

class Airplane(Base):
    """description: Represents an airplane entity."""
    __tablename__ = 'airplane'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    seating_capacity = Column(Integer)
    passenger_count = Column(Integer)

class Passenger(Base):
    """description: Represents a passenger entity with a link to airplane."""
    __tablename__ = 'passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    luggage_weight_total = Column(DECIMAL)
    airplane_id = Column(Integer, ForeignKey('airplane.id'))

class Luggage(Base):
    """description: Represents luggage linked to a passenger."""
    __tablename__ = 'luggage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    weight = Column(DECIMAL)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    airport1 = Airport(name="Heathrow", code="LHR", city="London", country="UK", latitude=Decimal('51.47'), longitude=Decimal('-0.454'))
    airport2 = Airport(name="JFK", code="JFK", city="New York", country="USA", latitude=Decimal('40.6413'), longitude=Decimal('-73.7781'))
    airport3 = Airport(name="Haneda", code="HND", city="Tokyo", country="Japan", latitude=Decimal('35.5522'), longitude=Decimal('139.7798'))
    airport4 = Airport(name="Schiphol", code="AMS", city="Amsterdam", country="Netherlands", latitude=Decimal('52.3105'), longitude=Decimal('4.7683'))
    airplane1 = Airplane(model="Boeing 777-200", seating_capacity=300, passenger_count=290)
    airplane2 = Airplane(model="Airbus A320", seating_capacity=150, passenger_count=148)
    airplane3 = Airplane(model="Boeing 737", seating_capacity=200, passenger_count=198)
    airplane4 = Airplane(model="Airbus A380", seating_capacity=500, passenger_count=480)
    passenger1 = Passenger(name="John Doe", email="johndoe@example.com", luggage_weight_total=Decimal('25.5'), airplane_id=1)
    passenger2 = Passenger(name="Jane Smith", email="janesmith@example.com", luggage_weight_total=Decimal('22.0'), airplane_id=1)
    passenger3 = Passenger(name="Alice Brown", email="alicebrown@example.com", luggage_weight_total=Decimal('30.0'), airplane_id=2)
    passenger4 = Passenger(name="Bob White", email="bobwhite@example.com", luggage_weight_total=Decimal('18.0'), airplane_id=2)
    luggage1 = Luggage(passenger_id=1, weight=Decimal('5.5'))
    luggage2 = Luggage(passenger_id=1, weight=Decimal('3.0'))
    luggage3 = Luggage(passenger_id=2, weight=Decimal('8.0'))
    luggage4 = Luggage(passenger_id=2, weight=Decimal('14.0'))
    
    
    
    session.add_all([airport1, airport2, airport3, airport4, airplane1, airplane2, airplane3, airplane4, passenger1, passenger2, passenger3, passenger4, luggage1, luggage2, luggage3, luggage4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
