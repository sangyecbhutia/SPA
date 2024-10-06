import openpyxl

def load_inputs_from_excel(file_name='valuation_inputs.xlsx'):
    """
    Load financial metrics from the users excel file
    """
    wb = openpyxl.load_workbook(file_name) #load the workbook
    sheet = wb.active #load the active sheet
    
    free_cash_flow = sheet['B2'].value #load the free cash flow
    growth_rate = sheet['B3'].value #load the growth rate
    discount_rate = sheet['B4'].value #load the discount rate 
    terminal_value_multiple = sheet['B5'].value #load the terminal value multiple
    
    return free_cash_flow, growth_rate, discount_rate, terminal_value_multiple