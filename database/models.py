# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 23, 2025 09:34:14
# Database: sqlite:////tmp/tmp.dxoG2uVy73-01JJ985D42M41MD4F79K9P5C3W/Aviation_System/database/db.sqlite
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



class Airport(Base):  # type: ignore
    """
    description: This class represents an airport entity that includes basic attributes like name, location, construction year, and capacity.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    construction_year = Column(Integer)
    capacity = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    FlightList : Mapped[List["Flight"]] = relationship(back_populates="airport")
    GateList : Mapped[List["Gate"]] = relationship(back_populates="airport")
    StaffList : Mapped[List["Staff"]] = relationship(back_populates="airport")



class Manufacturer(Base):  # type: ignore
    """
    description: Manufacturer details, including the name and originating country.
    """
    __tablename__ = 'manufacturer'
    _s_collection_name = 'Manufacturer'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AirplaneList : Mapped[List["Airplane"]] = relationship(back_populates="manufacturer")



class Passenger(Base):  # type: ignore
    """
    description: Basic passenger data including name and passport number.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    passport_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    LuggageList : Mapped[List["Luggage"]] = relationship(back_populates="passenger")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="passenger")



class Pilot(Base):  # type: ignore
    """
    description: Represents a pilot entity with basic information such as first and last name, and license number.
    """
    __tablename__ = 'pilot'
    _s_collection_name = 'Pilot'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    license_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AssignmentList : Mapped[List["Assignment"]] = relationship(back_populates="pilot")



class Airplane(Base):  # type: ignore
    """
    description: Represents the airplane details with attributes like model, airline, capacity, and manufacturer link.
    """
    __tablename__ = 'airplane'
    _s_collection_name = 'Airplane'  # type: ignore

    id = Column(Integer, primary_key=True)
    airplane_model = Column(String)
    airline = Column(String)
    capacity = Column(Integer)
    manufacturer_id = Column(ForeignKey('manufacturer.id'))

    # parent relationships (access parent)
    manufacturer : Mapped["Manufacturer"] = relationship(back_populates=("AirplaneList"))

    # child relationships (access children)



class Flight(Base):  # type: ignore
    """
    description: This class represents a flight entity, holding details about flight number, departure and arrival times, and the related airport.
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore

    id = Column(Integer, primary_key=True)
    flight_number = Column(String)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    airport_id = Column(ForeignKey('airport.id'))

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("FlightList"))

    # child relationships (access children)
    AssignmentList : Mapped[List["Assignment"]] = relationship(back_populates="flight")
    TicketList : Mapped[List["Ticket"]] = relationship(back_populates="flight")



class Gate(Base):  # type: ignore
    """
    description: Details for gates at the airport and their location.
    """
    __tablename__ = 'gate'
    _s_collection_name = 'Gate'  # type: ignore

    id = Column(Integer, primary_key=True)
    gate_number = Column(String)
    airport_id = Column(ForeignKey('airport.id'))

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("GateList"))

    # child relationships (access children)



class Luggage(Base):  # type: ignore
    """
    description: Represents luggage details associated with passengers.
    """
    __tablename__ = 'luggage'
    _s_collection_name = 'Luggage'  # type: ignore

    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    passenger_id = Column(ForeignKey('passenger.id'))

    # parent relationships (access parent)
    passenger : Mapped["Passenger"] = relationship(back_populates=("LuggageList"))

    # child relationships (access children)



class Staff(Base):  # type: ignore
    """
    description: Represents various staff members, their roles, and assigned airports.
    """
    __tablename__ = 'staff'
    _s_collection_name = 'Staff'  # type: ignore

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)
    airport_id = Column(ForeignKey('airport.id'))

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("StaffList"))

    # child relationships (access children)



class Assignment(Base):  # type: ignore
    """
    description: An assignment connecting pilots to their flights.
    """
    __tablename__ = 'assignment'
    _s_collection_name = 'Assignment'  # type: ignore

    id = Column(Integer, primary_key=True)
    pilot_id = Column(ForeignKey('pilot.id'))
    flight_id = Column(ForeignKey('flight.id'))

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("AssignmentList"))
    pilot : Mapped["Pilot"] = relationship(back_populates=("AssignmentList"))

    # child relationships (access children)



class Ticket(Base):  # type: ignore
    """
    description: Information pertaining to a ticket entity including price, and link to passengers and flights.
    """
    __tablename__ = 'ticket'
    _s_collection_name = 'Ticket'  # type: ignore

    id = Column(Integer, primary_key=True)
    ticket_number = Column(String)
    price = Column(Integer)
    passenger_id = Column(ForeignKey('passenger.id'))
    flight_id = Column(ForeignKey('flight.id'))

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("TicketList"))
    passenger : Mapped["Passenger"] = relationship(back_populates=("TicketList"))

    # child relationships (access children)
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="ticket")



class Booking(Base):  # type: ignore
    """
    description: Holds details about bookings connecting to tickets.
    """
    __tablename__ = 'booking'
    _s_collection_name = 'Booking'  # type: ignore

    id = Column(Integer, primary_key=True)
    booking_number = Column(String)
    booking_date = Column(Date)
    ticket_id = Column(ForeignKey('ticket.id'))

    # parent relationships (access parent)
    ticket : Mapped["Ticket"] = relationship(back_populates=("BookingList"))

    # child relationships (access children)
