
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Passenger.luggage_weight_total, as_sum_of=Luggage.weight)
