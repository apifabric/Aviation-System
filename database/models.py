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
# Created:  January 23, 2025 09:39:07
# Database: sqlite:////tmp/tmp.uGaZDtBmSz/Aviation_System_iter_1/database/db.sqlite
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



class Aircraft(Base):  # type: ignore
    """
    description: This table captures details of different aircrafts.
    """
    __tablename__ = 'aircraft'
    _s_collection_name = 'Aircraft'  # type: ignore

    id = Column(Integer, primary_key=True)
    model = Column(String)
    seating_capacity = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    AircraftMaintenanceList : Mapped[List["AircraftMaintenance"]] = relationship(back_populates="aircraft")
    FlightList : Mapped[List["Flight"]] = relationship(back_populates="aircraft")



class Airline(Base):  # type: ignore
    """
    description: This table provides details about different airlines.
    """
    __tablename__ = 'airline'
    _s_collection_name = 'Airline'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String(3))

    # parent relationships (access parent)

    # child relationships (access children)



class Airport(Base):  # type: ignore
    """
    description: This table stores information about the airports.
    """
    __tablename__ = 'airport'
    _s_collection_name = 'Airport'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    code = Column(String(3))

    # parent relationships (access parent)

    # child relationships (access children)
    AirportFacilityList : Mapped[List["AirportFacility"]] = relationship(back_populates="airport")
    FlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.arrival_airport_id]', back_populates="arrival_airport")
    departureFlightList : Mapped[List["Flight"]] = relationship(foreign_keys='[Flight.departure_airport_id]', back_populates="departure_airport")



class Pilot(Base):  # type: ignore
    """
    description: This table contains information about pilots.
    """
    __tablename__ = 'pilot'
    _s_collection_name = 'Pilot'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    license_number = Column(String)
    years_of_experience = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    PilotLicenseList : Mapped[List["PilotLicense"]] = relationship(back_populates="pilot")



class AircraftMaintenance(Base):  # type: ignore
    """
    description: This table logs maintenance details of aircraft.
    """
    __tablename__ = 'aircraft_maintenance'
    _s_collection_name = 'AircraftMaintenance'  # type: ignore

    id = Column(Integer, primary_key=True)
    aircraft_id = Column(ForeignKey('aircraft.id'))
    date_of_maintenance = Column(Date)
    next_due_date = Column(Date)
    remarks = Column(String)

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("AircraftMaintenanceList"))

    # child relationships (access children)



class AirportFacility(Base):  # type: ignore
    """
    description: Records various facilities available at airpots.
    """
    __tablename__ = 'airport_facility'
    _s_collection_name = 'AirportFacility'  # type: ignore

    id = Column(Integer, primary_key=True)
    airport_id = Column(ForeignKey('airport.id'))
    facility_type = Column(String)
    description = Column(String)

    # parent relationships (access parent)
    airport : Mapped["Airport"] = relationship(back_populates=("AirportFacilityList"))

    # child relationships (access children)



class Flight(Base):  # type: ignore
    """
    description: This table stores information about flights including departure and arrival details.
    """
    __tablename__ = 'flight'
    _s_collection_name = 'Flight'  # type: ignore

    id = Column(Integer, primary_key=True)
    flight_number = Column(String)
    departure_airport_id = Column(ForeignKey('airport.id'))
    arrival_airport_id = Column(ForeignKey('airport.id'))
    scheduled_departure = Column(DateTime)
    scheduled_arrival = Column(DateTime)
    aircraft_id = Column(ForeignKey('aircraft.id'))

    # parent relationships (access parent)
    aircraft : Mapped["Aircraft"] = relationship(back_populates=("FlightList"))
    arrival_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.arrival_airport_id]', back_populates=("FlightList"))
    departure_airport : Mapped["Airport"] = relationship(foreign_keys='[Flight.departure_airport_id]', back_populates=("departureFlightList"))

    # child relationships (access children)
    CrewMemberList : Mapped[List["CrewMember"]] = relationship(back_populates="flight")
    PassengerList : Mapped[List["Passenger"]] = relationship(back_populates="flight")
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="flight")



class PilotLicense(Base):  # type: ignore
    """
    description: This table contains license details for pilots.
    """
    __tablename__ = 'pilot_license'
    _s_collection_name = 'PilotLicense'  # type: ignore

    id = Column(Integer, primary_key=True)
    pilot_id = Column(ForeignKey('pilot.id'))
    license_type = Column(String)
    expiry_date = Column(Date)

    # parent relationships (access parent)
    pilot : Mapped["Pilot"] = relationship(back_populates=("PilotLicenseList"))

    # child relationships (access children)



class CrewMember(Base):  # type: ignore
    """
    description: This table consists of crew members working on flights.
    """
    __tablename__ = 'crew_member'
    _s_collection_name = 'CrewMember'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    flight_id = Column(ForeignKey('flight.id'))

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("CrewMemberList"))

    # child relationships (access children)



class Passenger(Base):  # type: ignore
    """
    description: This table records the details of passengers.
    """
    __tablename__ = 'passenger'
    _s_collection_name = 'Passenger'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String)
    passport_number = Column(String)
    birthdate = Column(Date)
    flight_id = Column(ForeignKey('flight.id'))

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("PassengerList"))

    # child relationships (access children)
    BaggageList : Mapped[List["Baggage"]] = relationship(back_populates="passenger")
    BookingList : Mapped[List["Booking"]] = relationship(back_populates="passenger")



class Baggage(Base):  # type: ignore
    """
    description: This table records baggage details for passengers.
    """
    __tablename__ = 'baggage'
    _s_collection_name = 'Baggage'  # type: ignore

    id = Column(Integer, primary_key=True)
    passenger_id = Column(ForeignKey('passenger.id'))
    weight = Column(Integer)
    baggage_type = Column(String)

    # parent relationships (access parent)
    passenger : Mapped["Passenger"] = relationship(back_populates=("BaggageList"))

    # child relationships (access children)



class Booking(Base):  # type: ignore
    """
    description: This table stores booking information.
    """
    __tablename__ = 'booking'
    _s_collection_name = 'Booking'  # type: ignore

    id = Column(Integer, primary_key=True)
    passenger_id = Column(ForeignKey('passenger.id'))
    flight_id = Column(ForeignKey('flight.id'))
    status = Column(String)
    booking_date = Column(Date)

    # parent relationships (access parent)
    flight : Mapped["Flight"] = relationship(back_populates=("BookingList"))
    passenger : Mapped["Passenger"] = relationship(back_populates=("BookingList"))

    # child relationships (access children)
