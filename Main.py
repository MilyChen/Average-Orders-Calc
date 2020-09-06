'''
Created on Sep 5, 2020

@author: Mily
'''
import pandas as pd

shoe_data = pd.read_csv("../AOVCalc/rawdata.csv")

print (shoe_data.head(1))  ## check first row

# calculate shoe Prices in a new column
shoe_data["shoe_price"] = shoe_data["order_amount"]/shoe_data["total_items"]

#quick stats on all columns of the dataset or specific column
print(shoe_data.describe())
#print(shoe_data["shoe_price"].describe())

#find the medians to caculate the final average order value
average_shoe_price = shoe_data["shoe_price"].median()
average_shoes_sold = shoe_data["total_items"].median()

#print out results
print( 'Average Shoe Price: ${0:,.2f}' .format(average_shoe_price))
print( 'Average Shoes Sold: {0:2,.0f}' .format(average_shoes_sold))
print( 'Average Order Value: ${0:,.2f}' .format(average_shoes_sold*average_shoe_price))