def calculate_bill(price,qty):
    total = price * qty 
    discount = total * 0.10
    final_amount = total - discount
    return final_amount

amount = calculate_bill(20,5)
print(amount)