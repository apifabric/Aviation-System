import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 2754442381945711730 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_1 = Airport(id=1, name="JFK International", location="New York, USA", code="JFK")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2754442381945711730)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3619293378404388350 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_2 = Airport(id=2, name="Los Angeles International", location="Los Angeles, USA", code="LAX")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3619293378404388350)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -535588445232476101 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_3 = Airport(id=3, name="Heathrow", location="London, UK", code="LHR")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-535588445232476101)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8245716919172235268 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_4 = Airport(id=4, name="Tokyo Haneda", location="Tokyo, Japan", code="HND")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8245716919172235268)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6463677349804580839 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight_1 = Flight(id=1, flight_number="AA100", departure_airport_id=1, arrival_airport_id=2, scheduled_departure=date(2023, 10, 1), scheduled_arrival=date(2023, 10, 1), aircraft_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6463677349804580839)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7343225245551492039 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight_2 = Flight(id=2, flight_number="BA256", departure_airport_id=3, arrival_airport_id=1, scheduled_departure=date(2023, 10, 2), scheduled_arrival=date(2023, 10, 2), aircraft_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7343225245551492039)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -7286140527089550720 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight_3 = Flight(id=3, flight_number="JL789", departure_airport_id=4, arrival_airport_id=3, scheduled_departure=date(2023, 10, 3), scheduled_arrival=date(2023, 10, 3), aircraft_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-7286140527089550720)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8171618588742082813 in succeeded_hashes:  # avoid duplicate inserts
            instance = flight_4 = Flight(id=4, flight_number="QF11", departure_airport_id=2, arrival_airport_id=4, scheduled_departure=date(2023, 10, 4), scheduled_arrival=date(2023, 10, 4), aircraft_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8171618588742082813)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5665293099833956941 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_1 = Aircraft(id=1, model="Boeing 777", seating_capacity=300)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5665293099833956941)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7742394960130165808 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_2 = Aircraft(id=2, model="Airbus A380", seating_capacity=500)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7742394960130165808)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5647936268062921529 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_3 = Aircraft(id=3, model="Boeing 787", seating_capacity=250)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5647936268062921529)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2801426302363592417 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_4 = Aircraft(id=4, model="Airbus A320", seating_capacity=180)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2801426302363592417)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6852669887533676667 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger_1 = Passenger(id=1, name="John Doe", passport_number="A1234567", birthdate=date(1985, 5, 20), flight_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6852669887533676667)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2112257836852178778 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger_2 = Passenger(id=2, name="Jane Smith", passport_number="B7654321", birthdate=date(1990, 8, 15), flight_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2112257836852178778)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1180391706465522560 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger_3 = Passenger(id=3, name="Alice Brown", passport_number="C2345678", birthdate=date(1992, 1, 10), flight_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1180391706465522560)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3210285804393852076 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger_4 = Passenger(id=4, name="Bob Johnson", passport_number="D8765432", birthdate=date(1988, 7, 25), flight_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3210285804393852076)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4115133985950816096 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_1 = Pilot(id=1, name="Captain Lewis", license_number="PL789123", years_of_experience=15)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4115133985950816096)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6966525446045278158 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_2 = Pilot(id=2, name="Captain Clarke", license_number="PL456789", years_of_experience=20)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6966525446045278158)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2280638151922036089 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_3 = Pilot(id=3, name="Captain Adams", license_number="PL123456", years_of_experience=10)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2280638151922036089)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7230574596424126262 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_4 = Pilot(id=4, name="Captain Edwards", license_number="PL987654", years_of_experience=5)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7230574596424126262)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2356660607082067734 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member_1 = CrewMember(id=1, name="Kelly Williams", position="Flight Attendant", flight_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2356660607082067734)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8909269416274080808 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member_2 = CrewMember(id=2, name="Peter Clark", position="Co-Pilot", flight_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8909269416274080808)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7408182543527484446 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member_3 = CrewMember(id=3, name="Susan Taylor", position="Navigator", flight_id=3)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7408182543527484446)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6438687085768475984 in succeeded_hashes:  # avoid duplicate inserts
            instance = crew_member_4 = CrewMember(id=4, name="Tom Hanks", position="Flight Engineer", flight_id=4)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6438687085768475984)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4032281386367961556 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking_1 = Booking(id=1, passenger_id=1, flight_id=1, status="Confirmed", booking_date=date(2023, 9, 1))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4032281386367961556)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5090789021468925534 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking_2 = Booking(id=2, passenger_id=2, flight_id=1, status="Cancelled", booking_date=date(2023, 9, 5))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5090789021468925534)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8485729457979759681 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking_3 = Booking(id=3, passenger_id=3, flight_id=2, status="Confirmed", booking_date=date(2023, 9, 6))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8485729457979759681)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1045845622867349250 in succeeded_hashes:  # avoid duplicate inserts
            instance = booking_4 = Booking(id=4, passenger_id=4, flight_id=2, status="Pending", booking_date=date(2023, 9, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1045845622867349250)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4451086687315031646 in succeeded_hashes:  # avoid duplicate inserts
            instance = baggage_1 = Baggage(id=1, passenger_id=1, weight=20, baggage_type="Checked")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4451086687315031646)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3320456132096708475 in succeeded_hashes:  # avoid duplicate inserts
            instance = baggage_2 = Baggage(id=2, passenger_id=2, weight=15, baggage_type="Carry-On")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3320456132096708475)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5184366364540701191 in succeeded_hashes:  # avoid duplicate inserts
            instance = baggage_3 = Baggage(id=3, passenger_id=3, weight=25, baggage_type="Checked")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5184366364540701191)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4844466652209484770 in succeeded_hashes:  # avoid duplicate inserts
            instance = baggage_4 = Baggage(id=4, passenger_id=4, weight=17, baggage_type="Carry-On")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4844466652209484770)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8499811127517486863 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline_1 = Airline(id=1, name="American Airlines", code="AA")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8499811127517486863)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3108588483433803091 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline_2 = Airline(id=2, name="British Airways", code="BA")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3108588483433803091)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6608949702577696026 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline_3 = Airline(id=3, name="Japan Airlines", code="JL")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6608949702577696026)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -6437151953172259010 in succeeded_hashes:  # avoid duplicate inserts
            instance = airline_4 = Airline(id=4, name="Qantas", code="QF")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-6437151953172259010)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1747762507803237959 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_license_1 = PilotLicense(id=1, pilot_id=1, license_type="Commercial", expiry_date=date(2025, 5, 20))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1747762507803237959)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 1568309803651437877 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_license_2 = PilotLicense(id=2, pilot_id=2, license_type="ATPL", expiry_date=date(2026, 8, 15))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(1568309803651437877)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4238787653409015655 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_license_3 = PilotLicense(id=3, pilot_id=3, license_type="Commercial", expiry_date=date(2024, 1, 10))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4238787653409015655)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -5876590865970965788 in succeeded_hashes:  # avoid duplicate inserts
            instance = pilot_license_4 = PilotLicense(id=4, pilot_id=4, license_type="PPL", expiry_date=date(2025, 7, 25))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-5876590865970965788)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4627644473428608179 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_maintenance_1 = AircraftMaintenance(id=1, aircraft_id=1, date_of_maintenance=date(2023, 9, 10), next_due_date=date(2024, 9, 10), remarks="Engine check")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4627644473428608179)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8202608691062206681 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_maintenance_2 = AircraftMaintenance(id=2, aircraft_id=2, date_of_maintenance=date(2023, 8, 20), next_due_date=date(2024, 8, 20), remarks="Tyre replacement")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8202608691062206681)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 73209183686926092 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_maintenance_3 = AircraftMaintenance(id=3, aircraft_id=3, date_of_maintenance=date(2023, 7, 15), next_due_date=date(2024, 7, 15), remarks="Hydraulic system check")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(73209183686926092)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6476099530252141640 in succeeded_hashes:  # avoid duplicate inserts
            instance = aircraft_maintenance_4 = AircraftMaintenance(id=4, aircraft_id=4, date_of_maintenance=date(2023, 6, 25), next_due_date=date(2024, 6, 25), remarks="Avionics update")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6476099530252141640)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4614683965399851321 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_facility_1 = AirportFacility(id=1, airport_id=1, facility_type="Lounge", description="VIP Lounge")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4614683965399851321)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6248321400664752548 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_facility_2 = AirportFacility(id=2, airport_id=2, facility_type="Parking", description="Long-term parking")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6248321400664752548)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -8013354157407079435 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_facility_3 = AirportFacility(id=3, airport_id=3, facility_type="WiFi", description="Free internet access")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8013354157407079435)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -2680888014128049158 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport_facility_4 = AirportFacility(id=4, airport_id=4, facility_type="Shopping", description="Duty-free shops")
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2680888014128049158)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
