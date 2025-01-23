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
    """description: This table stores information about the airports."""
    __tablename__ = 'airport'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    code = Column(String(3))

class Flight(Base):
    """description: This table stores information about flights including departure and arrival details."""
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String)
    departure_airport_id = Column(Integer, ForeignKey('airport.id'))
    arrival_airport_id = Column(Integer, ForeignKey('airport.id'))
    scheduled_departure = Column(DateTime)
    scheduled_arrival = Column(DateTime)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'))

class Aircraft(Base):
    """description: This table captures details of different aircrafts."""
    __tablename__ = 'aircraft'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    seating_capacity = Column(Integer)

class Passenger(Base):
    """description: This table records the details of passengers."""
    __tablename__ = 'passenger'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    passport_number = Column(String)
    birthdate = Column(Date)
    flight_id = Column(Integer, ForeignKey('flight.id'))

class Pilot(Base):
    """description: This table contains information about pilots."""
    __tablename__ = 'pilot'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    license_number = Column(String)
    years_of_experience = Column(Integer)

class CrewMember(Base):
    """description: This table consists of crew members working on flights."""
    __tablename__ = 'crew_member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    position = Column(String)
    flight_id = Column(Integer, ForeignKey('flight.id'))

class Booking(Base):
    """description: This table stores booking information."""
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    flight_id = Column(Integer, ForeignKey('flight.id'))
    status = Column(String)
    booking_date = Column(Date)

class Baggage(Base):
    """description: This table records baggage details for passengers."""
    __tablename__ = 'baggage'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    weight = Column(Integer)
    baggage_type = Column(String)

class Airline(Base):
    """description: This table provides details about different airlines."""
    __tablename__ = 'airline'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    code = Column(String(3))

class PilotLicense(Base):
    """description: This table contains license details for pilots."""
    __tablename__ = 'pilot_license'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pilot_id = Column(Integer, ForeignKey('pilot.id'))
    license_type = Column(String)
    expiry_date = Column(Date)

class AircraftMaintenance(Base):
    """description: This table logs maintenance details of aircraft."""
    __tablename__ = 'aircraft_maintenance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    aircraft_id = Column(Integer, ForeignKey('aircraft.id'))
    date_of_maintenance = Column(Date)
    next_due_date = Column(Date)
    remarks = Column(String)

class AirportFacility(Base):
    """description: Records various facilities available at airpots."""
    __tablename__ = 'airport_facility'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airport_id = Column(Integer, ForeignKey('airport.id'))
    facility_type = Column(String)
    description = Column(String)


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
    airport_1 = Airport(id=1, name="JFK International", location="New York, USA", code="JFK")
    airport_2 = Airport(id=2, name="Los Angeles International", location="Los Angeles, USA", code="LAX")
    airport_3 = Airport(id=3, name="Heathrow", location="London, UK", code="LHR")
    airport_4 = Airport(id=4, name="Tokyo Haneda", location="Tokyo, Japan", code="HND")
    flight_1 = Flight(id=1, flight_number="AA100", departure_airport_id=1, arrival_airport_id=2, scheduled_departure=date(2023, 10, 1), scheduled_arrival=date(2023, 10, 1), aircraft_id=1)
    flight_2 = Flight(id=2, flight_number="BA256", departure_airport_id=3, arrival_airport_id=1, scheduled_departure=date(2023, 10, 2), scheduled_arrival=date(2023, 10, 2), aircraft_id=2)
    flight_3 = Flight(id=3, flight_number="JL789", departure_airport_id=4, arrival_airport_id=3, scheduled_departure=date(2023, 10, 3), scheduled_arrival=date(2023, 10, 3), aircraft_id=3)
    flight_4 = Flight(id=4, flight_number="QF11", departure_airport_id=2, arrival_airport_id=4, scheduled_departure=date(2023, 10, 4), scheduled_arrival=date(2023, 10, 4), aircraft_id=4)
    aircraft_1 = Aircraft(id=1, model="Boeing 777", seating_capacity=300)
    aircraft_2 = Aircraft(id=2, model="Airbus A380", seating_capacity=500)
    aircraft_3 = Aircraft(id=3, model="Boeing 787", seating_capacity=250)
    aircraft_4 = Aircraft(id=4, model="Airbus A320", seating_capacity=180)
    passenger_1 = Passenger(id=1, name="John Doe", passport_number="A1234567", birthdate=date(1985, 5, 20), flight_id=1)
    passenger_2 = Passenger(id=2, name="Jane Smith", passport_number="B7654321", birthdate=date(1990, 8, 15), flight_id=1)
    passenger_3 = Passenger(id=3, name="Alice Brown", passport_number="C2345678", birthdate=date(1992, 1, 10), flight_id=2)
    passenger_4 = Passenger(id=4, name="Bob Johnson", passport_number="D8765432", birthdate=date(1988, 7, 25), flight_id=2)
    pilot_1 = Pilot(id=1, name="Captain Lewis", license_number="PL789123", years_of_experience=15)
    pilot_2 = Pilot(id=2, name="Captain Clarke", license_number="PL456789", years_of_experience=20)
    pilot_3 = Pilot(id=3, name="Captain Adams", license_number="PL123456", years_of_experience=10)
    pilot_4 = Pilot(id=4, name="Captain Edwards", license_number="PL987654", years_of_experience=5)
    crew_member_1 = CrewMember(id=1, name="Kelly Williams", position="Flight Attendant", flight_id=1)
    crew_member_2 = CrewMember(id=2, name="Peter Clark", position="Co-Pilot", flight_id=2)
    crew_member_3 = CrewMember(id=3, name="Susan Taylor", position="Navigator", flight_id=3)
    crew_member_4 = CrewMember(id=4, name="Tom Hanks", position="Flight Engineer", flight_id=4)
    booking_1 = Booking(id=1, passenger_id=1, flight_id=1, status="Confirmed", booking_date=date(2023, 9, 1))
    booking_2 = Booking(id=2, passenger_id=2, flight_id=1, status="Cancelled", booking_date=date(2023, 9, 5))
    booking_3 = Booking(id=3, passenger_id=3, flight_id=2, status="Confirmed", booking_date=date(2023, 9, 6))
    booking_4 = Booking(id=4, passenger_id=4, flight_id=2, status="Pending", booking_date=date(2023, 9, 10))
    baggage_1 = Baggage(id=1, passenger_id=1, weight=20, baggage_type="Checked")
    baggage_2 = Baggage(id=2, passenger_id=2, weight=15, baggage_type="Carry-On")
    baggage_3 = Baggage(id=3, passenger_id=3, weight=25, baggage_type="Checked")
    baggage_4 = Baggage(id=4, passenger_id=4, weight=17, baggage_type="Carry-On")
    airline_1 = Airline(id=1, name="American Airlines", code="AA")
    airline_2 = Airline(id=2, name="British Airways", code="BA")
    airline_3 = Airline(id=3, name="Japan Airlines", code="JL")
    airline_4 = Airline(id=4, name="Qantas", code="QF")
    pilot_license_1 = PilotLicense(id=1, pilot_id=1, license_type="Commercial", expiry_date=date(2025, 5, 20))
    pilot_license_2 = PilotLicense(id=2, pilot_id=2, license_type="ATPL", expiry_date=date(2026, 8, 15))
    pilot_license_3 = PilotLicense(id=3, pilot_id=3, license_type="Commercial", expiry_date=date(2024, 1, 10))
    pilot_license_4 = PilotLicense(id=4, pilot_id=4, license_type="PPL", expiry_date=date(2025, 7, 25))
    aircraft_maintenance_1 = AircraftMaintenance(id=1, aircraft_id=1, date_of_maintenance=date(2023, 9, 10), next_due_date=date(2024, 9, 10), remarks="Engine check")
    aircraft_maintenance_2 = AircraftMaintenance(id=2, aircraft_id=2, date_of_maintenance=date(2023, 8, 20), next_due_date=date(2024, 8, 20), remarks="Tyre replacement")
    aircraft_maintenance_3 = AircraftMaintenance(id=3, aircraft_id=3, date_of_maintenance=date(2023, 7, 15), next_due_date=date(2024, 7, 15), remarks="Hydraulic system check")
    aircraft_maintenance_4 = AircraftMaintenance(id=4, aircraft_id=4, date_of_maintenance=date(2023, 6, 25), next_due_date=date(2024, 6, 25), remarks="Avionics update")
    airport_facility_1 = AirportFacility(id=1, airport_id=1, facility_type="Lounge", description="VIP Lounge")
    airport_facility_2 = AirportFacility(id=2, airport_id=2, facility_type="Parking", description="Long-term parking")
    airport_facility_3 = AirportFacility(id=3, airport_id=3, facility_type="WiFi", description="Free internet access")
    airport_facility_4 = AirportFacility(id=4, airport_id=4, facility_type="Shopping", description="Duty-free shops")
    
    
    
    session.add_all([airport_1, airport_2, airport_3, airport_4, flight_1, flight_2, flight_3, flight_4, aircraft_1, aircraft_2, aircraft_3, aircraft_4, passenger_1, passenger_2, passenger_3, passenger_4, pilot_1, pilot_2, pilot_3, pilot_4, crew_member_1, crew_member_2, crew_member_3, crew_member_4, booking_1, booking_2, booking_3, booking_4, baggage_1, baggage_2, baggage_3, baggage_4, airline_1, airline_2, airline_3, airline_4, pilot_license_1, pilot_license_2, pilot_license_3, pilot_license_4, aircraft_maintenance_1, aircraft_maintenance_2, aircraft_maintenance_3, aircraft_maintenance_4, airport_facility_1, airport_facility_2, airport_facility_3, airport_facility_4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
