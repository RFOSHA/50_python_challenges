#Create a function called my_discount. Asks the user to provide a price and discount (%). Function computes price
#after discount

def my_discount():
    price = float(input("Price:"))
    per_off = float(input("Percentage discount:"))
    return (1-per_off)*price

answer = my_discount()
print(answer)