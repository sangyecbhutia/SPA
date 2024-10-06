def calculate_dcf(free_cash_flow, growth_rate, discount_rate, terminal_value_multiple, years=5):
    """
    Function to calculate DCF value based company valuation using the DCF formula
    """
    #calculate future cash flows
    cash_flows = [free_cash_flow * (1 + growth_rate)**i for i in range(1, years+1)]
    #calculate terminal value
    terminal_value = cash_flows[-1] * terminal_value_multiple
    #calculate DCF value
    dcf_value = sum(cf / (1 + discount_rate)**i for i, cf in enumerate(cash_flows, 1))
    #add terminal value to DCF value
    dcf_value += terminal_value / (1 + discount_rate)**years
    return dcf_value

