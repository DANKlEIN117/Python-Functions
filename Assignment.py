Is_running = True
while Is_running:

    try:
        def create_discount(price,discount_percent):
            if discount_percent >= 20:
                return price - (price *discount_percent/100)
            else:
                return price
            
        price = int(input("Enter the original price of the item: "))
        discount_percent = int(input("Enter the discount Percentage: "))

        print(create_discount(price=price, discount_percent=discount_percent))
    except ValueError:
        print("Please Enter only Numbers IDIOT!")