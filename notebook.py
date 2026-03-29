import sys
import numpy as np
import pandas as pd
bonus_points = 3
import matplotlib.pyplot as plt
sales_data = [{'product': 'Notebook', 'units': 4, 'unit_price': 2.5}, {'product': 'Pen', 'units': 10, 'unit_price': 1.2}, {'product': 'Bag', 'units': 2, 'unit_price': 25.0}]

def summarize_sales_debug(data):
    total_units = 0
    total_revenue = 0.0
    for record in data:
        units = record.get('units', record.get('qty', 0))
        price = record['unit_price']
        total_units += units
        total_revenue += units * price
    avg_price = 0
    if total_units > 0:
        avg_price = total_revenue / total_units
    return (total_units, round(total_revenue, 2), round(avg_price, 2))
