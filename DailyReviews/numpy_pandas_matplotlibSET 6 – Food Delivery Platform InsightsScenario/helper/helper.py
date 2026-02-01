from datetime import date

from faker import Faker
import pandas as pd

def helper():
    order_id_list = [i for i in range(101,201)]
    restaurant_list = [
        'Ragvendra',
        'Sai hotel',
        'ganesh cantneen',
        'ram hotel',
        'burj mastani',
        'taj hotel',
        'tarangan',
        'kundan'

    ]

    min_order_value = 200
    max_order_value = 1000

    
