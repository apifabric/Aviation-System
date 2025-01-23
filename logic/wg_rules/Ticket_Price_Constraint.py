
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.constraint(validate=Ticket,
                  as_condition=lambda row: row.price > 0,
                  error_msg="Ticket price ({row.price}) must be greater than zero")
