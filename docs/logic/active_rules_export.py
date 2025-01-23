def declare_logic():
    # Ticket Price Constraint 
    # Ensure ticket prices are above a reasonable threshold.
    Rule.constraint(validate=Ticket,
                    as_condition=lambda row: row.price > 0,
                    error_msg="Ticket price ({row.price}) must be greater than zero")
    