# Ask for id, price, discount, and VAT (IVA).
customer_id = input("Enter customer ID: ")
price = float(input("Enter item price: "))
discount = float(input("Enter discount percentage: "))
vat = float(input("Enter VAT percentage: "))

# Calculate discounted price
discounted_price = price - (price * discount / 100)

# Calculate final price
final_price = discounted_price + (discounted_price * vat / 100)

# Show results
print(customer_id)
print(final_price)