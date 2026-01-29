from datetime import date

import pandas as pd
from faker import Faker

def e_commerce():
    fk = Faker()
    order_id_list = [i for i in range(50)]
    min_order_date = date(2024,1,1)
    max_order_date = date(2025,2,3)

    customer_id_list = [i for i in range(101,301)]
    product_category_list = ["Electronics",
    "Clothing",
    "Footwear",
    "Home & Kitchen",
    "Beauty & Personal Care",
    "Books",
    "Sports & Fitness",
    "Toys & Games",
    "Grocery",
    "Automotive"]
    min_price = 100
    max_price = 10000

    min_quantity = 1
    max_quantity = 5

    min_discount_per = 5
    max_discount_per = 20

    order_id = []
    order_date = []
    customer_id = []
    product_category = []
    price = []
    quantity = []
    discount_percent = []

    data = {
        'order_id':order_id,
        'order_date':order_date,
        'customer_id':customer_id,
        'product_category':product_category,
        'price':price,
        'quantity':quantity,
        'discount_percent':discount_percent
    }

    for _ in range(500):
        order_id.append(fk.random_element(order_id_list))
        order_date.append(fk.date_between_dates(min_order_date,max_order_date))
        customer_id.append(fk.random_element(customer_id_list))
        product_category.append(fk.random_element(product_category_list))
        price.append(fk.random_int(min_price,max_price))
        quantity.append(fk.random_int(min_quantity,max_quantity))
        discount_percent.append(fk.random_int(min_discount_per,max_discount_per))

    return pd.DataFrame(data)

if __name__ == '__main__':
    print(e_commerce())

