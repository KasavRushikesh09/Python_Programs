import numpy as np
sales = np.random.randint(-20,100,size = (30,5))
print("original sales data\n",sales)

sales[sales<0] = 0
print("Replace neg with 0\n",sales)

# avg_weekly_sales_per_product = sales[sales>0].mean()
# sales[sales<0] = avg_weekly_sales_per_product
#
# print("avg values:\n",avg_weekly_sales_per_product)

weekly_sales = sales[:28].reshape(4,7,5)

avg_weekly_sales = weekly_sales.mean(axis = 1)
print("avg:\n",avg_weekly_sales)

pro_avg = avg_weekly_sales.mean(axis=0)
best_product = np.argmax(pro_avg)
print("Average Sales per Product:", pro_avg)
print("Product with highest average weekly sales: Product", best_product + 1)



