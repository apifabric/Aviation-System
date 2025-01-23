
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.constraint(validate=Flight, as_condition=lambda row: row.passenger_count <= row.aircraft.seating_capacity, error_msg="Flight passenger count ({row.passenger_count}) exceeds aircraft seating capacity ({row.aircraft.seating_capacity})")
