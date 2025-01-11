print ( "Welcome")
print("Item Price Calculator")
#Inputs to Program-this is a comment 
#my first python code in class CS 171 
sales_tax = 8
discount = 10
item_price = float(input ("tell me the item price: "))

#Process ( Steps of algorithm)
discount_amount = item_price * (discount/100)
item_price = item_price - discount_amount
tax_amount = item_price * (sales_tax/100)
item_price - item_price + tax_amount
item_price = round(item_price, 2)

#output
print("final price:", item_price)
