```python
# lovely_loveseat
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'

lovely_loveseat_price = 254.00


# stylish_settee
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'

stylish_settee_price = 180.50


# luxurious_lamp
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ''

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += '\n' + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax



print(f'Customer One Items: \n{customer_one_itemization}')
print(f'Customer One Total: {customer_one_total}')
```





### Quiz

#### What is the difference between a float and an int?

- A **float** represents decimal quantities. An **int** represents whole numbers.

  

#### Difference between SyntaxError and NameError

* SyntaxError is grammarly wrong code.
* NameError is not exactly defined