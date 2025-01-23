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
    """description: This class represents an airport entity that includes basic attributes like name, location, construction year, and capacity."""
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    construction_year = Column(Integer)
    capacity = Column(Integer)

class Flight(Base):
    """description: This class represents a flight entity, holding details about flight number, departure and arrival times, and the related airport."""
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    airport_id = Column(Integer, ForeignKey('airport.id'))

class Airplane(Base):
    """description: Represents the airplane details with attributes like model, airline, capacity, and manufacturer link."""
    __tablename__ = 'airplane'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airplane_model = Column(String)
    airline = Column(String)
    capacity = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))

class Manufacturer(Base):
    """description: Manufacturer details, including the name and originating country."""
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    country = Column(String)

class Pilot(Base):
    """description: Represents a pilot entity with basic information such as first and last name, and license number."""
    __tablename__ = 'pilot'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    license_number = Column(String)

class Assignment(Base):
    """description: An assignment connecting pilots to their flights."""
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pilot_id = Column(Integer, ForeignKey('pilot.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))

class Staff(Base):
    """description: Represents various staff members, their roles, and assigned airports."""
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)
    airport_id = Column(Integer, ForeignKey('airport.id'))

class Passenger(Base):
    """description: Basic passenger data including name and passport number."""
    __tablename__ = 'passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    passport_number = Column(String)

class Ticket(Base):
    """description: Information pertaining to a ticket entity including price, and link to passengers and flights."""
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ticket_number = Column(String)
    price = Column(Integer)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))

class Booking(Base):
    """description: Holds details about bookings connecting to tickets."""
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_number = Column(String)
    booking_date = Column(Date)
    ticket_id = Column(Integer, ForeignKey('ticket.id'))

class Luggage(Base):
    """description: Represents luggage details associated with passengers."""
    __tablename__ = 'luggage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    weight = Column(Integer)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))

class Gate(Base):
    """description: Details for gates at the airport and their location."""
    __tablename__ = 'gate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    gate_number = Column(String)
    airport_id = Column(Integer, ForeignKey('airport.id'))


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
    airport1 = Airport(name="JFK International", location="New York", construction_year=1948, capacity=60000)
    airport2 = Airport(name="Heathrow", location="London", construction_year=1946, capacity=80000)
    airport3 = Airport(name="Changi Airport", location="Singapore", construction_year=1981, capacity=85300)
    airport4 = Airport(name="Haneda Airport", location="Tokyo", construction_year=1931, capacity=85000)
    flight1 = Flight(flight_number="AA101", departure_time=datetime(2023, 11, 25, 15, 30), arrival_time=datetime(2023, 11, 25, 18, 30), airport_id=1)
    flight2 = Flight(flight_number="BA202", departure_time=datetime(2023, 11, 25, 8, 0), arrival_time=datetime(2023, 11, 25, 10, 30), airport_id=2)
    flight3 = Flight(flight_number="SQ303", departure_time=datetime(2023, 11, 26, 11, 0), arrival_time=datetime(2023, 11, 26, 15, 0), airport_id=3)
    flight4 = Flight(flight_number="JL404", departure_time=datetime(2023, 11, 26, 12, 30), arrival_time=datetime(2023, 11, 26, 16, 30), airport_id=4)
    
    
    
    session.add_all([airport1, airport2, airport3, airport4, flight1, flight2, flight3, flight4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
