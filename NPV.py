# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:06:38 2023

"""

def calculate_npv(initial_cost, annual_savings, annual_maintenance_cost, discount_rate, num_years):
    # Calculate the annual cash flows
    annual_cash_flows = []
    for year in range(1, num_years+1):
        annual_cash_flow = annual_savings - annual_maintenance_cost
        annual_cash_flows.append(annual_cash_flow)

    # Calculate the present value of each annual cash flow
    present_values = []
    for year in range(1, num_years+1):
        pv = annual_cash_flows[year-1] / ((1 + discount_rate) ** year)
        present_values.append(pv)

    # Calculate the total present value of the cash flows
    total_pv = sum(present_values)

    # Calculate the NPV
    npv = total_pv - initial_cost

    return npv

# Inputs and assumptions
initial_cost = 100000
annual_savings = 30000
annual_maintenance_cost = 39200
discount_rate = 0.08
num_years = 20

# Call the function to calculate the NPV
npv = calculate_npv(initial_cost, annual_savings, annual_maintenance_cost, discount_rate, num_years)

# Print the result
print("The NPV of the gas turbine air intake system is:", round(npv, 2))
