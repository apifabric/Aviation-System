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
        if not 551213934113077998 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport1 = Airport(name="Heathrow", code="LHR", city="London", country="UK", latitude=Decimal('51.47'), longitude=Decimal('-0.454'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(551213934113077998)
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
        if not 5728750706896768380 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport2 = Airport(name="JFK", code="JFK", city="New York", country="USA", latitude=Decimal('40.6413'), longitude=Decimal('-73.7781'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5728750706896768380)
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
        if not 5216075133246106556 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport3 = Airport(name="Haneda", code="HND", city="Tokyo", country="Japan", latitude=Decimal('35.5522'), longitude=Decimal('139.7798'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5216075133246106556)
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
        if not 6627830779999437737 in succeeded_hashes:  # avoid duplicate inserts
            instance = airport4 = Airport(name="Schiphol", code="AMS", city="Amsterdam", country="Netherlands", latitude=Decimal('52.3105'), longitude=Decimal('4.7683'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6627830779999437737)
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
        if not 2846566314885507724 in succeeded_hashes:  # avoid duplicate inserts
            instance = airplane1 = Airplane(model="Boeing 777-200", seating_capacity=300, passenger_count=290)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2846566314885507724)
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
        if not 215318399422096404 in succeeded_hashes:  # avoid duplicate inserts
            instance = airplane2 = Airplane(model="Airbus A320", seating_capacity=150, passenger_count=148)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(215318399422096404)
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
        if not 8034508885884281815 in succeeded_hashes:  # avoid duplicate inserts
            instance = airplane3 = Airplane(model="Boeing 737", seating_capacity=200, passenger_count=198)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8034508885884281815)
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
        if not -3092369608073351193 in succeeded_hashes:  # avoid duplicate inserts
            instance = airplane4 = Airplane(model="Airbus A380", seating_capacity=500, passenger_count=480)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3092369608073351193)
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
        if not -8947441501065694885 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger1 = Passenger(name="John Doe", email="johndoe@example.com", luggage_weight_total=Decimal('25.5'), airplane_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-8947441501065694885)
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
        if not -3578708456150804589 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger2 = Passenger(name="Jane Smith", email="janesmith@example.com", luggage_weight_total=Decimal('22.0'), airplane_id=1)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-3578708456150804589)
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
        if not 5132504091257146408 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger3 = Passenger(name="Alice Brown", email="alicebrown@example.com", luggage_weight_total=Decimal('30.0'), airplane_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5132504091257146408)
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
        if not 6063352197359043645 in succeeded_hashes:  # avoid duplicate inserts
            instance = passenger4 = Passenger(name="Bob White", email="bobwhite@example.com", luggage_weight_total=Decimal('18.0'), airplane_id=2)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6063352197359043645)
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
        if not 788912287179671787 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage1 = Luggage(passenger_id=1, weight=Decimal('5.5'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(788912287179671787)
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
        if not -9050887353415901475 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage2 = Luggage(passenger_id=1, weight=Decimal('3.0'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-9050887353415901475)
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
        if not 3451642031570248053 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage3 = Luggage(passenger_id=2, weight=Decimal('8.0'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3451642031570248053)
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
        if not -2916037213486577849 in succeeded_hashes:  # avoid duplicate inserts
            instance = luggage4 = Luggage(passenger_id=2, weight=Decimal('14.0'))
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-2916037213486577849)
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
