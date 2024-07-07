# Write a function called your_vat. The function has no
# parameters. The function asks the user to input the price of an
# item and VAT (VAT should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and the
# VAT is 15%, your code should return a VAT-inclusive price of 253.
# Check to see if your code can handle ValueError and negative
# inputs from the user. Ensure the code runs until valid numbers
# are entered. (Hint: Your code should include a while loop.)

def your_vat():
    while True:
        price = input("Enter the price of the item: ")
        vat = input("Enter the VAT of the item as a decimal: ")

        try:
            price = float(price)
            vat = float(vat)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return print((price * (1+vat)))

your_vat()